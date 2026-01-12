from __future__ import print_function

import grpc

from .generated import glossary_pb2
from .generated import glossary_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = glossary_pb2_grpc.GlossaryServiceStub(channel)

        print("--- Получение списка всех терминов ---")
        try:
            response = stub.GetAllTerms(glossary_pb2.GetAllTermsRequest())
            for title, term in response.terms.items():
                print(f"{title}: {term.title}")
                print(f"Определение: {term.definition}")
                if term.source_link:
                    print(f"Источник: {term.source_link}")
                print()
        except grpc.RpcError as e:
            print(f"Ошибка: {e.details()}")

        print("\n--- Получение одного термина ---")
        try:
            response = stub.GetTerm(
                glossary_pb2.GetTermRequest(title="Event loop"))
            print(f"Найден термин: {response.term.title}")
            print(f"Определение: {response.term.definition}")
        except grpc.RpcError as e:
            print(f"Ошибка: {e.details()}")

        print("\n--- Добавление нового термина с описанием ---")
        try:
            new_term = glossary_pb2.Term(
                title="Asynchronous I/O",
                definition="Метод выполнения операций ввода-вывода без блокировки выполнения программы, позволяющий обрабатывать другие задачи одновременно.",
                source_link="https://en.wikipedia.org/wiki/Asynchronous_I/O",
            )
            response = stub.CreateTerm(
                glossary_pb2.CreateTermRequest(term=new_term))
            print(f"Создан термин: {response.term.title}")
        except grpc.RpcError as e:
            print(f"Ошибка: {e.details()}")

        print("\n--- Обновление существующего термина ---")
        try:
            response = stub.UpdateTerm(glossary_pb2.UpdateTermRequest(
                title="Asynchronous I/O",
                definition="Метод выполнения операций ввода-вывода без блокировки выполнения программы, позволяющий обрабатывать другие задачи одновременно.(new)",
            ))
            print(f"Обновлен термин: {response.term.title}")
            print(f"Новое определение: {response.term.definition}")
        except grpc.RpcError as e:
            print(f"Ошибка: {e.details()}")

        print("\n--- Удаление термина из глоссария ---")
        try:
            response = stub.DeleteTerm(
                glossary_pb2.DeleteTermRequest(title="Asynchronous I/O"))
            print(f"Удален термин: {response.term.title}")
        except grpc.RpcError as e:
            print(f"Ошибка: {e.details()}")


if __name__ == "__main__":
    run()
