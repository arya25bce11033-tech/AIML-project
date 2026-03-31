#HEALTH REPORT ANALYSIS TOOL 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier   

#using ML for model training and prediction of healt risks 
data_set = {
    "BMI":[25,19,23,17,30,26,29,19,20,27],
    "sugar_level":[100,80,120,90,150,110,140,85,95,130],
    "systolic":[130,120,125,110,140,135,145,115,118,138],
    "diastolic":[85,80,82,75,90,88,110,78,80,89],
    "haemoglobin":[14,12,13,10,15,13.5,9.0,18,7.0,16],
    "cholesterol":[220,180,200,150,250,230,270,190,210,240],
    "hdl":[40,50,45,60,35,42,30,55,38,33],
    "ldl":[130,100,120,80,160,140,180,110,125,150],
    "triglycerides":[160,120,140,100,200,180,250,130,150,220],
    "thyroid_level":[4.5,1.0,3.0,9.0,5.0,4.0,13.0,1.5,0.3,7.0],
    "t3":[150,100,120,80,200,180,250,90,70,300],
    "t4":[10,8,9,5,12,11,15,7,4,20],
    "health_risk":[1,0,0,0,1,1,1,0,1,1]
}


df = pd.DataFrame(data_set)
a = df[["BMI", "sugar_level", "systolic", "diastolic", "haemoglobin", "cholesterol", "hdl", "ldl", "triglycerides", "thyroid_level", "t3", "t4"]]
b = df["health_risk"]
model = DecisionTreeClassifier(random_state=50 , max_depth=4)
model.fit(a,b)

#CALCULATION BMI using height and weight 
def BMI_calculator(weight, height):
    BMI =weight/(height ** 2)
    return BMI
#ANALYSZING AND SCALING BMI
def analyze_bmi (BMI):
    if BMI < 18.5:
        return "you are underweight"
    elif 18.5 <= BMI < 25:
        return "you have normal weight"
    elif 25 <= BMI < 30:
        return "you are overweight"
    else:
        return "you are obese, focus on your health "
    

    # TAKING NECESSARY INPUTS FROM USER 
height =float(input("enter your height in meters: "))
weight =  float(input("enter your weight in kg: "))
BMI =BMI_calculator(weight, height)
print(analyze_bmi(BMI))

BMI_value = BMI_calculator(weight, height)

#SCALING SUGAR LEVELS
def analyze_sugarlevel(sugar_level):
    if sugar_level < 70:
        return "you are hypoglycemic , low sugar level"
    elif 70 <= sugar_level <= 99:
        return " you have normal sugar level"
    elif 100 <= sugar_level <= 125:
        return "you are prediabetic , control your sugar level"
    elif 126 <= sugar_level <= 199:
        return "you might have diabetes , high sugar level "
    else: 
        return "you might have diabetes , very high sugar level"
    
    #taking necessary input from user
sugar_level =  float(input("enter your fasting blood sugar level : "))
print(analyze_sugarlevel(sugar_level))

sugar_level_status = analyze_sugarlevel(sugar_level)

#SCALING BLOOD PRESSURE
def analyze_bp(systolic, diastolic):
    if systolic < 120 and diastolic < 80:
        return "you have normal blood pressure"
    elif 120 <= systolic <= 129 and diastolic < 80:
        return "you have elevated blood pressure"
    elif (130 <= systolic <= 139) or (80 <= diastolic <= 89):
        return "you have hypertension stage 1"
    elif (140 <= systolic) or (90 <= diastolic):
        return "you have hypertension stage 2"
    else:
        return "you have hypertensive crisis, consult your doctor immediately or call an ambulance"

# Taking necessary inputs from user
systolic =float(input("enter your systolic blood pressure : "))
diastolic =   float(input("enter your diastolic blood pressure : "))
print(analyze_bp(systolic, diastolic))

blood_pressure_status = analyze_bp(systolic, diastolic)

#SCALING HAEMOGLOBIN LEVELS
def analyze_hb(haemoglobin_level):
    if haemoglobin_level < 8:
        return "you have severe anemia, very low haemoglobin level, consult your doctor immediately "
    elif 8 <= haemoglobin_level < 13.5:
        return "you have mild anemia, low haemoglobin level"
    elif 13.5 <= haemoglobin_level <= 17.5:
        return "you have normal haemoglobin level"
    else:
        return "you have high haemoglobin level, consult your doctor"
    
    #taking necessary input from user
haemoglobin_level =float(input("enter your haemoglobin level: "))
print(analyze_hb(haemoglobin_level))

haemoglobin_status = analyze_hb(haemoglobin_level)

#SCALING CHOLESTEROL LEVELS INCLUDING hdl ldl and triglycerides also
def analyze_cholesterol(cholesterol_level, hdl, ldl, triglycerides):
    
    if cholesterol_level < 200:
        chol_result = "you have normal cholesterol level"
    elif 200 <= cholesterol_level <= 239:
        chol_result ="you have borderline high cholesterol level, control your cholesterol level"
    else:
        chol_result ="you have high cholesterol level, consult your doctor"

        #hdl

    if hdl < 40:
        hdl_result ="you have low HDL cholesterol level, consult your doctor"
    elif 40 <= hdl < 60:
        hdl_result ="you have normal HDL cholesterol level"
    else:
        hdl_result ="you have high HDL cholesterol level, which is good" 

        #ldl

    if ldl < 100:
        ldl_result ="you have normal LDL cholesterol level"
    elif 100 <= ldl < 129:
        ldl_result ="you have near normal LDL cholesterol level"
    elif 130 <= ldl < 159:
        ldl_result ="you have borderline high LDL cholesterol level, control your LDL cholesterol level"
    elif 160 <= ldl < 189:
        ldl_result ="you have high LDL cholesterol level, consult your doctor"
    else:
        ldl_result ="you have very high LDL cholesterol level, consult your doctor immediately"   

    # Triglycerides

    if triglycerides < 150:
        triglycerides_result ="you have normal triglycerides level"
    elif 150 <= triglycerides < 199:
        triglycerides_result = "you have borderline high triglycerides level, control your triglycerides level"
    elif 200 <= triglycerides < 499:
        triglycerides_result = "you have high triglycerides level, consult your doctor"
    else:
        triglycerides_result ="you have very high triglycerides level, consult your doctor immediately"

    return f"{chol_result} \n  {hdl_result} \n{ldl_result} \n{triglycerides_result}"    

    
    #taking necessary input from user
cholesterol_level =  float(input("enter your total cholesterol level : "))
hdl =float(input("enter your HDL cholesterol level  : "))
ldl = float(input("enter your LDL cholesterol level : "))
triglycerides =   float(input("enter your triglycerides level : "))
print(analyze_cholesterol(cholesterol_level, hdl, ldl, triglycerides))

cholesterol_status = analyze_cholesterol(cholesterol_level, hdl, ldl, triglycerides)


#SCALING THYROID LEVELS including t 3 and t 4 also
def thyroid_analyzer(thyroid_level, t3, t4):
    if thyroid_level < 0.4:
        tsh =  "you have hypothyroidism, low thyroid level, consult your doctor"
    elif 0.4 <= thyroid_level <= 4.0:
        tsh ="you have normal thyroid level"
    else:
        tsh ="you have hyperthyroidism, high thyroid level, consult your doctor"
    
    #t3

    if t3 < 80:
        t3_result =   "you have low T3 level, consult your doctor"
    elif 80 <= t3 <= 200:
        t3_result =  "you have normal T3 level"
    else:
        t3_result ="you have high T3 level, consult your doctor"    
      # t4

    if t4 < 5.0:
        t4_result = "you have low T4 level, consult your doctor"
    elif 5.0 <= t4 <= 12.0:
        t4_result =   "you have normal T4 level"
    else:
        t4_result = "you have high T4 level, consult your doctor"

    if tsh =="you have hypothyroidism, low thyroid level, consult your doctor" or t3_result =="you have low T3 level, consult your doctor" or t4_result =="you have low T4 level, consult your doctor":  
        return "you have possible hypothyroidism, consult your doctor"
    elif tsh =="you have hyperthyroidism, high thyroid level, consult your doctor" or t3_result =="you have high T3 level, consult your doctor" or t4_result =="you have high T4 level, consult your doctor":
        return "you have hyperthyroidism, consult your doctor"
    else:
        return "you have normal thyroid function"
    
    #taking necessary input from user
thyroid_level =float(input("enter your thyroid level: "))
T3 =   float(input("enter your T3 level: "))
T4 =float(input("enter your T4 level: "))
print(thyroid_analyzer(thyroid_level, T3, T4))

thyroid_status = thyroid_analyzer(thyroid_level, T3, T4)


#DISPLAY OF FINAL REPORT AND REVIEW IN MINIMALISTIC MANNER
print("YOUR FINAL HEALTH REPORT ANALYSIS IS:")
print(f"BMI: {BMI_value}")
print(f"Sugar Level: {sugar_level_status}")
print(f"Blood Pressure: {blood_pressure_status}")
print(f"Haemoglobin: {haemoglobin_status}")
print(f"Cholesterol: {cholesterol_status}")
print(f"Thyroid: {thyroid_status}")


health_results = {
    "BMI": BMI_value,
    "Sugar Level": sugar_level_status,
    "Blood Pressure": blood_pressure_status,
    "Haemoglobin": haemoglobin_status,
    "Cholesterol": cholesterol_status,
    "Thyroid": thyroid_status,
    "thyroid_level": thyroid_level,
    "t3": T3,
    "t4": T4,
    "ldl": ldl,
    "hdl": hdl,
    "triglycerides": triglycerides
}


# prediction from user input
user_ml_data = [[
    BMI,
    sugar_level,
    systolic,
    diastolic,
    haemoglobin_level,
    cholesterol_level,
    hdl,
    ldl,
    triglycerides,
    thyroid_level,
    T3,
    T4
]]

ml_prediction = model.predict(user_ml_data)[0]
if ml_prediction == 1:
    print("ML Predicted Health Risk: High Risk")
else:
    print("ML Predicted Health Risk: Low Risk")



# risk calculator for warnings 

def risk_calculator(health_results):
    risk_score = 0
    
    if health_results["BMI"] < 18.5 or health_results["BMI"] >= 25:
        risk_score += 1
    if health_results["Sugar Level"] != "you have normal sugar level":
        risk_score += 1
    if health_results["Blood Pressure"] != "you have normal blood pressure":
        risk_score += 1
    if health_results["Haemoglobin"] != "you have normal haemoglobin level":
        risk_score += 1
    if health_results["Cholesterol"] != "you have normal cholesterol level":
        risk_score += 1
    if health_results["Thyroid"] != "you have normal thyroid function":
        risk_score += 1
        if health_results["t3"] < 80 or health_results["t3"] > 200:
            risk_score += 1
        if health_results["t4"] < 5.0 or health_results["t4"] > 12.0:
            risk_score += 1
    if health_results["ldl"] <=130 and health_results["hdl"] <40 :
        risk_score += 1
    if health_results["triglycerides"] >= 200 and health_results["hdl"] <40 :
        risk_score += 1
    if health_results["hdl"] < 40:
        risk_score += 1
    
    return risk_score

risk_score = risk_calculator(health_results)
print(f"your overall health risk score is :{risk_score} out of 6")
print(f" Predicted Health Risk: {ml_prediction}")

if risk_score >=3:
    print("you have high health risk, consult your doctor and follow up!")
elif risk_score >1:
    print("you have moderate health risk , focus on your health and brig some healthy life style changes")
else:
    print("you have very low health risk, maintain your healthy lifestyle and have regular checkups")

    #warning system after analysing report and giving probable specific health risk 
def warning(health_results):
        warnings = []
        if health_results["BMI"] < 18.5 and health_results["Sugar Level"] != "you have normal sugar level":
            warnings.append("you are underweight and have abnormal sugar level, " \
            "you could be at risk of malnutrition and diabetes, consult your doctor and get your tests done then follow up with a nutritionist for a balanced diet")
        if health_results["Blood Pressure"] != "you have normal blood pressure" and health_results["Cholesterol"] != "you have normal cholesterol level":
            warnings.append("you have abnormal blood pressure and cholesterol levels, " \
                "you may be at risk of heart disease, consult your doctor immediately  and get your tests done then follow up with exercise and healthy diet recommended by doc or nutritionist")
        if health_results["Haemoglobin"] != "you have normal haemoglobin level" and health_results["Thyroid"] != "you have normal thyroid function":
            warnings.append("you have abnormal haemoglobin and thyroid levels, " \
                "you may be at risk of anemia and thyroid disorders, consult your doctor immediately and get your tests done then follow up with a nutritionist for a balanced diet and thyroid specialist")
        if health_results["Sugar Level"] != "you have normal sugar level" and health_results["Blood Pressure"] != "you have normal blood pressure":
            warnings.append("you have abnormal sugar level and blood pressure, " \
                "you may be at risk of diabetes and hypertension, consult your doctor immediately and get your tests done then follow up with exercise and healthy diet recommended by doc or nutritionist")
        if health_results["Cholesterol"] not in "you have normal cholesterol level" and health_results["Thyroid"] != "you have normal thyroid function":
            warnings.append("you have abnormal cholesterol and thyroid levels, " \
                "you may be at risk of heart disease and thyroid disorders, consult your doctor immediately and get your tests done then follow up with a nutritionist for a balanced diet and thyroid specialist")
        if health_results["ldl"] <=130 and health_results["hdl"] <40 :
            warnings.append("you have high bad cholestrol and low good cholestrol, " \
                "you may be at risk of heart disease, consult your doctor immediately and get your tests done then follow up with exercise and healthy diet recommended by doc or nutritionist")
        if health_results["triglycerides"] >= 200 and health_results["hdl"] <40 :
            warnings.append("you have high triglycerides and low good cholestrol, " \
                "you may be at risk of heart disease, consult your doctor immediately and get your tests done then follow up with exercise and healthy diet recommended by doc or nutritionist")
        if health_results["thyroid_level"]>4.0 and health_results["t3"] > 200 and health_results["t4"] > 12.0:
            warnings.append("you have high thyroid level, high T3 and high T4 levels, " \
                "you may be at risk of hyperthyroidism, consult your doctor immediately and get your tests done then follow up with a thyroid specialist")
        if health_results["thyroid_level"]<0.4 and health_results["t3"] < 80 and health_results["t4"] < 5.0:
            warnings.append("you have low thyroid level, low T3 and low T4 levels, " \
                "you may be at risk of hypothyroidism, consult your doctor immediately and get your tests done then follow up with a thyroid specialist")
        if health_results["thyroid_level"]<0.4 and health_results["t3"] > 80 and health_results["t4"] > 5.0:
            warnings.append("you have low thyroid level, high T3 and high T4 levels, " \
                "you may be at risk of hyperthyroidism, consult your doctor immediately and get your tests done then follow up with a thyroid specialist")
            if not warnings:
                warnings.append("your health report is normal, maintain your healthy lifestyle and have regular checkups")

            return warnings
        
        health_warnings = warning(health_results)
        print("HEALTH WARNINGS BASED ON YOUR REPORT:")
        for item in health_warnings:
            print(f"- {item}")
#actimight on steps based on report analysis and risk assessment
def new_action_steps(health_results, risk_score):
    action_steps = []
    print("action steps:...")
    if health_results["Sugar Level"] in [ "you might have diabetes , high sugar level " , "you have diabetes , very high sugar level"]:
        print("Action Step: Consult your doctor for diabetes management and follow a healthy diet and add a 30 - 45 minutes of brisk walking or exercise in your daily routine")
    if health_results["Blood Pressure"] in [ "you might have hypertension stage 1" ,  "you have hypertension stage 2"] or health_results["Blood Pressure"] in ["you have hypertensive crisis, consult your doctor immediately or call an ambulance"]:
        print("Action Step: Consult your doctor for blood pressure management and follow a healthy diet which have less salt and do light exercises. take as less stress as possible")
    if health_results["Cholesterol"] in [ "you might have high cholesterol level, consult your doctor" , "you have very high cholesterol level, consult your doctor immediately"]:
        print("Action Step: Consult your doctor for cholesterol management and follow a healthy diet rich in fibre and avoid fried or oily foods and exercise routine , try to involve foods like nuts which increase good cholestrol in body")
    if health_results["Thyroid"] in [ "you might have possible hypothyroidism, consult your doctor" , "you have hyperthyroidism, consult your doctor"]:
        print("Action Step: Consult your doctor for thyroid management and follow a healthy diet and exercise routine recommended by your doctor or nutritionist.")
    if health_results["Haemoglobin"] in [ "you might have severe anemia, very low haemoglobin level, consult your doctor immediately " , "you have mild anemia, low haemoglobin level"]:
        print("Action Step: Consult your doctor for anemia management and follow a healthy diet rich in iron and maintain proper meal timings ")
    if health_results["BMI"] < 18.5:
        print("Action Step: Consult your doctor for underweight management and follow a healthy balanced diet and  do not skipp meals ")
    if health_results["BMI"] >= 25:
        print("Action Step: Consult your doctor for overweight or obesity management and control calorie and reduce junk food , eatc food rich in fibre and protien and add exercise in daily routine ")
    if risk_score >= 3:
        print("Action Step: You have high health risk, consult your doctor for health evaluation and follow a healthy diet and exercise routine recommended by your doctor and monitor health throuhg tests regularly")
    elif risk_score > 1:
        print("Action Step: You have moderate health risk, focus on your health and bring some healthy lifestyle changes, consult your doctor for personalized recommendations , and maintain proper meal and sleep timngs")
    else:
        print("Action Step: You have very low health risk, maintain your healthy lifestyle and have regular checkups with your doctor.")

    return action_steps
series_steps = new_action_steps(health_results, risk_score)

print("RECOMMENDED ACTION STEPS BASED ON YOUR REPORT:")
for step in series_steps:
    print(f"- {step}")

    