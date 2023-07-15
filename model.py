 # Burada risk faktörlerine dayalı basit bir risk hesaplama işlemi gerçekleştiriyoruz.
 
    # Örneğin, belirli yaş, cinsiyet, fiziksel aktivite düzeyi, diyet, aile geçmişi ve bmi değerlerine göre risk seviyesini artırabilir veya azaltabiliriz.
    
    # ÖNEMLİ!!
    # Bu risk faktörlerinin ağırlıklarını belirlemek için daha fazla bilimsel veriye ve analize ihtiyaç olduğunu lütfen unutmayın bu nedenle aşağıdaki kod, örnek amaçlıdır ve gerçek yaşam verilerine dayalı bir model oluşturmak için kullanılmamalıdır.

def calculate_risk(age, gender, physical_activity_level, diet, family_history, bmi):
    risk = 0
    max_risk = 60  # Maksimum risk puanı

    if age > 60:
        risk += 10
    elif age > 40:
        risk += 5

    if gender.lower() == 'erkek':
        risk += 5

    if physical_activity_level.lower() == 'düşük':
        risk += 10

    if diet.lower() == 'sağlıksız':
        risk += 10

    if family_history.lower() == 'evet':
        risk += 10

    if bmi > 30:
        risk += 10
    elif bmi > 25:
        risk += 5

    risk_percentage = (risk / max_risk) * 100  # Risk yüzdesini hesaplıyoruz

    return risk, risk_percentage
