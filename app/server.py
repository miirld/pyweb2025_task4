from concurrent import futures

import logging
import grpc

from .generated import glossary_pb2
from .generated import glossary_pb2_grpc


class GlossaryService(glossary_pb2_grpc.GlossaryServiceServicer):
    def __init__(self):
        self.data = {
            "Event loop": glossary_pb2.Term(
                title="Event loop",
                definition="Механизм, который управляет выполнением асинхронных задач, распределяя время процессора между ними.",
                source_link="https://docs.python.org/3/library/asyncio-eventloop.html"
            ),
            "Coroutine": glossary_pb2.Term(
                title="Coroutine",
                definition="Функция, которая может приостанавливать своё выполнение и передавать управление event loop для других задач.",
                source_link="https://docs.python.org/3/library/asyncio-task.html#coroutines"
            ),
            "Future": glossary_pb2.Term(
                title="Future",
                definition="Объект, представляющий результат асинхронной операции, который станет доступен в будущем.",
                source_link="https://docs.python.org/3/library/asyncio-future.html"
            ),
            "Concurrency": glossary_pb2.Term(
                title="Concurrency",
                definition="Способность программы выполнять несколько задач одновременно, используя асинхронные механизмы.",
                source_link="https://en.wikipedia.org/wiki/Concurrency_(computer_science)"
            ),
            "Parallelism": glossary_pb2.Term(
                title="Parallelism",
                definition="Выполнение нескольких задач одновременно на разных ядрах процессора для повышения производительности.",
                source_link="https://en.wikipedia.org/wiki/Parallel_computing"
            ),
        }

    def GetAllTerms(self, request, context):
        return glossary_pb2.GetAllTermsResponse(terms=self.data)

    def GetTerm(self, request, context):
        title = request.title
        term = self.data.get(title)

        if not term:
            context.abort(
                grpc.StatusCode.NOT_FOUND,
                "Термин не найден",
            )

        return glossary_pb2.TermResponse(term=term)

    def CreateTerm(self, request, context):
        term = request.term
        title = term.title

        if title in self.data:
            context.abort(
                grpc.StatusCode.BAD_REQUEST,
                "Термин уже существует",
            )

        self.data[title] = term
        return glossary_pb2.TermResponse(term=term)

    def UpdateTerm(self, request, context):
        title = request.title
        term = self.data.get(title)

        if not term:
            context.abort(
                grpc.StatusCode.NOT_FOUND,
                "Термин не найден",
            )

        if request.definition:
            term.definition = request.definition
        if request.source_link:
            term.source_link = request.source_link

        return glossary_pb2.TermResponse(term=term)

    def DeleteTerm(self, request, context):
        title = request.title
        term = self.data.pop(title, None)

        if not term:
            context.abort(
                grpc.StatusCode.NOT_FOUND,
                "Термин не найден",
            )

        return glossary_pb2.TermResponse(term=term)


def serve():
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )

    glossary_pb2_grpc.add_GlossaryServiceServicer_to_server(
        GlossaryService(),
        server,
    )

    server.add_insecure_port("[::]:50051")
    server.start()

    print("Server started on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
