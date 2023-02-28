from flask import Flask, jsonify
from py2neo import Graph

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

graph = Graph("bolt://localhost:7687", auth=("neo4j", "0123456789"))


@app.route('/person/<name>', methods=['GET'])
def get_person(name):
    query = (
        "MATCH (p:Person {name: $name})-[:PARTICIPATED_IN]->(b:Person)"
        "RETURN p.name AS person, COLLECT(b.name) AS related_people"
    )
    results = graph.run(query, name=name).data()

    if not results:
        return jsonify({'error': 'Person not found'}), 404

    return jsonify(results[0])


if __name__ == '__main__':
    app.run(debug=True)


"""
127.0.0.1 - - [28/Feb/2023 17:16:14] "GET /person/Ахромеева%20Алина%20Ивановна HTTP/1.1" 200 -

{
  "person": "Ахромеева Алина Ивановна",
  "related_people": [
    "Салагаев Иван Рамилевич",
    "Акодес Ефим Анатольевич",
    "Гужов Глеб Данилович",
    "Расулев Никита Петрович",
    "Ларищев Илья Александрович",
    "Шовковская Наталья Николаевна",
    "Айдамирова Карина Антоновна",
    "Сарсадских Алена Геннадьевна",
    "Толкунова Валентина Маратовна",
    "Шальнова Ольга Владимировна",
    "Щурупова Алла Филипповна",
    "Белогорлов Дамир Кириллович",
    "Нетужилова Елена Викторовна",
    "Аксанова Кристина Григорьевна",
    "Чечин Рамиль Константинович",
    "Селин Федор Ильич",
    "Жубанов Анатолий Иванович",
    "Бодрякова Евгения Яновна",
    "Близняков Иван Артемович",
    "Бугаенкова Карина Аркадьевна",
    "Бобрецова Светлана Артемовна",
    "Непомнящих Илья Дамирович",
    "Арбачаков Филипп Андреевич",
    "Бекрева Виктория Яковлевна",
    "Преображенская Кира Альбертовна",
    "Старухин Дамир Маратович",
    "Домогаров Антон Максимович",
    "Бордачев Никита Васильевич",
    "Камилов Дамир Павлович",
    "Урманцева Евгения Олеговна",
    "Кутасов Константин Сергеевич",
    "Яникеев Вячеслав Русланович",
    "Чикирева Мария Романовна",
    "Думлер Людмила Вячеславовна",
    "Андриевская Марина Ринатовна",
    "Борголов Евгений Маратович",
    "Алипичев Евгений Тимурович",
    "Вохменцев Владимир Владиславович",
    "Соловейчиков Олег Павлович",
    "Ковшов Глеб Германович",
    "Абаренов Ильдар Робертович",
    "Музалевская Ангелина Федоровна",
    "Сайденов Иван Валерьевич",
    "Камчадалов Артем Ярославович",
    "Щенников Дмитрий Григорьевич",
    "Дудыкина Мария Романовна",
    "Соломеина Кристина Георгиевна",
    "Тяжлов Ринат Владиславович",
    "Ящукова Любовь Ефимовна"
  ]
}
"""