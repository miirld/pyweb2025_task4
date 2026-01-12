## Отчёт. Задание 4. RPC. gRPC. Protobuf

> Дисциплина "Проектирование и развертывание веб-решений в эко-системе Python"

### Выполнение работы

1. Разработка приложения

<img width="2560" height="1464" alt="image" src="https://github.com/user-attachments/assets/9c16a1b7-355a-423f-aee2-900143c0f3c8" />

2. Подготовка к работе

<img width="1920" height="608" alt="image" src="https://github.com/user-attachments/assets/a31d2188-b93a-4ecd-832a-4c3e6534c52a" />

3. Генерация кода из protobuf

<img width="1915" height="33" alt="image" src="https://github.com/user-attachments/assets/a49ca2e9-07cc-4739-8819-9d640509ba0a" />

4. Запуск скрипта сервера

<img width="1914" height="86" alt="image" src="https://github.com/user-attachments/assets/6f35bcaa-c0a5-4293-a6a8-691f90246e5b" />

5. Запуск скрипта клиента

<img width="1920" height="932" alt="image" src="https://github.com/user-attachments/assets/423c4424-340c-4865-a827-14618d3ebfa4" />

### Исследование
**Подборка статей**
1. [Performance evaluation of microservices
communication with REST, GraphQL, and gRPC](https://journals.pan.pl/Content/131803/PDF/22_4436_Niswar_sk_NEW.pdf#:~:text=REST%20maintained%20the%20lowest%20utilization,of%2090.30%25%20for%20500%20requests.)
2. [Impact of Protocol Selection on Performance and Scalability in Microservices: A Comparison of gRPC, REST, and GraphQL](https://www.researchgate.net/publication/392507557_Impact_of_Protocol_Selection_on_Performance_and_Scalability_in_Microservices_A_Comparison_of_gRPC_REST_and_GraphQL#:~:text=REST%20consistently%20proved%20slower%20than,flexibility%20in%20distributed%20microservice%20architectures.)
3. [Comparative Analysis of RESTful, GraphQL, and gRPC APIs: Perfomance Insight from Load and Stress Testing](https://www.researchgate.net/publication/391024991_Comparative_Analysis_of_RESTful_GraphQL_and_gRPC_APIs_Perfomance_Insight_from_Load_and_Stress_Testing#:~:text=By%20presenting%20a%20comprehensive%20analysis,balanced%20performance%20across%20diverse%20workloads.)

**Результаты исследований:**
1. Производительность
- gRPC является безусловным лидером по скорости
- REST стабилен, обеспечивает более высокую пропускную способность, чем GraphQL
- GraphQL часто оказывается медленнее конкурентов
2. Данные
- GraphQL позволяет сократить объем передаваемых данных и уменьшить количество сетевых вызовов
- преимущество gRPC в бинарной сериализации
3. Потребление ресурсов
- GraphQL потребляет значительно больше ресурсов CPU в сравнении с конкурентами

**Резюме по исследованиям**

Идеального протокола не существует, выбор зависит от сценария использования. 

gRPC рекомендуется как основной стандарт для внутреннего взаимодействия между микросервисами. Он обеспечивает максимальную производительность, стабильность при масштабировании.

GraphQL идеален для BFF. Несмотря на высокое потребление ресурсов, он устраняет проблему избыточной выборки данных и позволяет минимизировать количество запросов от клиента.

REST - стандрат для внешних API из-за простоты, предсказуемости масштабирования и широкой поддержки.

