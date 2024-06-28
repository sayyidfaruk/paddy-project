from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret_key'

class ExpertSystem:
    def __init__(self):
        self.facts = []
        self.rules = [
            {"if": ["G001", "G002", "G003", "G004", "G005"], "then": "Tungro"},
            {"if": ["G006", "G007", "G008", "G009", "G010", "G011"], "then": "Kerdil Rumput (Grassy Stunt)"},
            {"if": ["G012", "G013", "G014", "G015", "G016"], "then": "Kerdil Hampa (Ragged Stunt)"},
            {"if": ["G003", "G017", "G018", "G019"], "then": "Daun Jingga (Orange Leaf)"},
            {"if": ["G020", "G021", "G022", "G023", "G024"], "then": "Kerdil Kuning (Yellow Dwarf)"},
            {"if": ["G025", "G026", "G027", "G028"], "then": "Hawar Daun Bakteri (Bacterial Leaf Blight)"}
        ]

    def add_fact(self, fact):
        if fact not in self.facts:
            self.facts.append(fact)

    def infer(self):
        highest_prob_rule = None
        highest_prob = 0
        for rule in self.rules:
            match_count = sum(1 for fact in rule["if"] if fact in self.facts)
            total_count = len(rule["if"])
            probability = (match_count / total_count) * 100
            if probability > highest_prob:
                highest_prob = probability
                highest_prob_rule = {"penyakit": rule["then"], "probabilitas": probability}
        return highest_prob_rule

questions = [
    {"code": "G001", "question": "Ada kehadiran wereng?"},
    {"code": "G002", "question": "Terdapat bintik-bintik coklat bekas tusukan wereng?"},
    {"code": "G003", "question": "Pertumbuhan tanaman kerdil?"},
    {"code": "G004", "question": "Daun menguning hingga jingga dari pucuk daun ke arah pangkal daun?"},
    {"code": "G005", "question": "Malai yang dihasilkan sedikit, bintik-bintik coklat pada bulir padi?"},
    {"code": "G006", "question": "Pertumbuhan tanaman kerdil?"},
    {"code": "G007", "question": "Pertumbuhan tanaman padi sangat tegak?"},
    {"code": "G008", "question": "Seperti rerumputan dan bundar?"},
    {"code": "G009", "question": "Anakan berlebihan?"},
    {"code": "G010", "question": "Daun hijau kekuningan lebih pendek dan sempit dari biasanya?"},
    {"code": "G011", "question": "Tanaman tidak dapat memproduksi?"},
    {"code": "G012", "question": "Tanaman kerdil parah selama tahap awal panen?"},
    {"code": "G013", "question": "Daun hijau lebih gelap dibanding daun normal?"},
    {"code": "G014", "question": "Daun bergerigi melingkar berwarna kuning kecoklatan?"},
    {"code": "G015", "question": "Pembungaan tertunda?"},
    {"code": "G016", "question": "Pertumbuhan malai terhambat dan bulir tidak terisi?"},
    {"code": "G017", "question": "Anakan banyak daunnya yang lemas?"},
    {"code": "G018", "question": "Daun berwarna hijau muda atau kuning pucat?"},
    {"code": "G019", "question": "Dapat menghasilkan sedikit malai namun dengan bulir yang tidak sempurna atau tidak sama sekali?"},
    {"code": "G020", "question": "Mula-mula warna jingga tampak pada daun bagian bawah?"},
    {"code": "G021", "question": "Seluruh permukaan daun berwarna jingga mencolok?"},
    {"code": "G022", "question": "Tanaman mati sebelum berbunga?"},
    {"code": "G023", "question": "Pertumbuhan malai terhambat dan bulir tidak terisi?"},
    {"code": "G024", "question": "Akar tanaman jumlahnya lebih sedikit dari tanaman normal?"},
    {"code": "G025", "question": "Daun menguning, menggulung, mengering dan menjadi layu?"},
    {"code": "G026", "question": "Bibit menjadi layu (kresek) tapi sulit dicabut?"},
    {"code": "G027", "question": "Warna luka bercak menjadi jingga kekuningan dari ujung daun ke pangkal daun?"},
    {"code": "G028", "question": "Ada bulatan kecil berwarna kuning pada pelepah daun?"}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'current_question' not in session:
        session['current_question'] = 0
        session['facts'] = []

    if request.method == 'POST':
        answer = request.form['answer']
        code = request.form['code']

        if answer == 'iya':
            session['facts'].append(code)

        session['current_question'] += 1

        if session['current_question'] >= len(questions):
            expert_system = ExpertSystem()
            for fact in session['facts']:
                expert_system.add_fact(fact)
            diagnosis = expert_system.infer()
            session.pop('current_question', None)
            session.pop('facts', None)
            return render_template('result.html', diagnosis=diagnosis)

    current_question = questions[session['current_question']]
    return render_template('question.html', question=current_question['question'], code=current_question['code'])

if __name__ == '__main__':
    app.run(debug=True)
