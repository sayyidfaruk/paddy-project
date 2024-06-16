from flask import Flask, render_template, request

app = Flask(__name__)

class ExpertSystem:
    def __init__(self):
        self.facts = []
        self.rules = [
            {"if": ["daun kuning", "bercak coklat"], "then": "Hawar Daun"},
            {"if": ["tanaman kerdil", "bercak hitam"], "then": "Penyakit Tungro"},
            {"if": ["akar busuk", "daun layu"], "then": "Busuk Akar"},
            {"if": ["bulir kosong", "tanaman menguning"], "then": "Hawar Bakteri"},
            {"if": ["daun bergaris", "tanaman mengering"], "then": "Virus Kerdil"}
        ]

    def add_fact(self, fact):
        if fact not in self.facts:
            self.facts.append(fact)

    def infer(self):
        for rule in self.rules:
            if all(fact in self.facts for fact in rule["if"]):
                return rule["then"]
        return "Penyakit tidak diketahui"

@app.route('/', methods=['GET', 'POST'])
def index():
    diagnosis = None
    if request.method == 'POST':
        gejala = request.form.getlist('gejala')
        expert_system = ExpertSystem()
        for g in gejala:
            expert_system.add_fact(g)
        diagnosis = expert_system.infer()
    return render_template('index.html', diagnosis=diagnosis)

if __name__ == '__main__':
    app.run(debug=True)
