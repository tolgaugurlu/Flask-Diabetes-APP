from flask import Flask, render_template, request
from model import calculate_risk

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        age = int(request.form.get('age')) # string değerini tam sayıya çeviriyorum
        gender = request.form.get('gender')
        physical_activity_level = request.form.get('physical_activity_level')
        diet = request.form.get('diet')
        family_history = request.form.get('family_history')
        bmi = float(request.form.get('bmi')) # string değerini ondalıklı sayıya çeviriyorum

        risk, risk_percentage = calculate_risk(age, gender, physical_activity_level, diet, family_history, bmi) # risk ve risk yüzdesini ayrı ayrı alıyoruz

        advice = ""
        if risk > 30:
            advice = "Risk faktörlerinizi azaltmak için yaşam tarzınızda önemli değişiklikler yapmayı düşünmelisiniz."
        elif risk > 20:
            advice = "Bazı risk faktörleriniz var, bu konuda dikkatli olmalısınız."
        else:
            advice = "Risk faktörleriniz düşük, ancak sağlıklı bir yaşam tarzını sürdürmeye devam etmelisiniz."

        return render_template('result.html', result=risk, risk_percentage=risk_percentage, advice=advice) # risk yüzdesini de template'e gönderiyoruz

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
