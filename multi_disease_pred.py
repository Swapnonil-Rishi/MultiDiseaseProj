from fpdf import FPDF
import pickle
import streamlit as st

st.set_page_config(
    page_title="AmIWell?",
    page_icon="chart_with_upwards_trend",
    layout="wide",
   
)


heart_model=pickle.load(open('fin_mod_heart.sav','rb'))
diabe_model=pickle.load(open('fin_mod_diabetes.sav','rb'))
parkins_model=pickle.load(open('parkinsons_model.sav','rb'))

st.title('Multiple Disease Prediction System')

    
tab1, tab2, tab3 = st.tabs(["Heart Disease Report", "Diabates Report", "Parkinson's Report"],
                         )


#HEART DISEASE PREDICTION
with tab1:
   st.header('Heart Disease Prediction System')
   col1, col2, col3 = st.columns(3)
   with col1:
       name = st.text_input('Your Name')
   with col2:
       age = int(st.text_input('Your Age',value=0))
   with col3:
       sex = 1 if(st.selectbox('Specify your gender',("Male","Female"))=="Male") else 0
   with col1:
       levels = {
       'None': 0, 
       'Minor': 1,
       'Major': 2,
       'Serious': 3,
       }
  
       cp=levels.get(st.selectbox("Chest pain type",("None","Minor","Major","Serious")))
   with col2:
       trestbps=st.number_input("Resting Blood Pressure")
   with col3:
       chol=st.number_input("serum cholestoral in mg/dl")
   with col1:
       fbs=st.number_input("fasting blood sugar")
   with col2:
       restecg=st.number_input("resting electrocardiographic results")	
   with col3:
       thalach=st.number_input("maximum heart rate achieved")
   with col1:
       exang=0 if(st.selectbox("Exercise Induced Angina",("Yes","No"))=="No")else 1
   with col2:
       oldpeak=st.number_input("ST depression induced by exercise relative to rest")
   with col3:
        sl={
       '0-1':0,
       '1-2':1,
       '2':2,
       }
        slope=sl.get(st.selectbox("the slope of the peak exercise ST segment",("0-1","1-2","2")))
   with col1:
        ca=st.selectbox("number of major vessels (0-3) colored by flourosopy",(0,1,2,3))
   with col2:
        thp={
       'Null':0,
       'normal':1,
       'fixed defect':2,
       'reversable defect':3,
       }
        thal=thp.get(st.selectbox("Thal",("Null","normal","fixed defect","reversable defect")))
   heart_pred=''
   column1 ,column2=st.columns(2)
   with column1:
     if st.button('Heart test Result'):
         predH=heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
         heart_pred='Healthy' if (predH==0) else 'Unhealthy'

     st.info(heart_pred)

   with column2:
#PDF REPORT HEART DISEASE
      pdf = FPDF('P', 'mm', 'A4')
     
    
      pdf.add_page()
      
      pdf.set_font('Arial', 'B', 24)
      pdf.cell(190, 10, txt = "Heart test Report",ln = 1, align = 'C')
      pdf.line(x1 = 10, y1 = 27.5, x2 = 200, y2 = 27.5)
    
      pdf.set_font('Arial', 'B', 14)
      pdf.cell(20, 30, txt = "Name : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial',size=14)
      pdf.cell(10, 30, txt = name,
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(15, 0, txt = "Age : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(10, 0, txt = str(age),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(15, 30, txt = "Sex : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(15, 30, txt = "Male"if (sex==1)else"Female",
             ln = 1, align = 'L')
      
      lev = {
       0: 'None', 
       1:'Minor',
       2:'Major',
       3:'Serious',
      }
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(45, 0, txt = "Chest pain Type : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(10, 0, txt = lev.get(cp),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(65, 30, txt = "Resting Blood Pressure : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(15, 30, txt = str(trestbps),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(50, 0, txt = "serum cholestoral : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(20, 0, txt = str(chol),
             ln = 0, align = 'L')
      pdf.cell(15, 0, txt = "mg/dl",
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(55, 30, txt = "fasting blood sugar : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(15, 30, txt = str(fbs),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(90, 0, txt = "resting electrocardiographic results : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(20, 0, txt = str(restecg),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(55, 30, txt = "Maximum heart rate : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(15, 30, txt = str(thalach),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(65, 0, txt = "Exercise Induced Angina : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(20, 0, txt = str(exang),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(125, 30, txt = "ST depression induced by exercise relative to rest : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(15, 30, txt = str(oldpeak),
             ln = 1, align = 'L')
      
     
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(105, 0, txt = "the slope of the peak exercise ST segment : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(20, 0, txt = str(slope),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(65, 30, txt = "Number of Major Vessels : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(20,30, txt = str(ca),
             ln = 1, align = 'L')
      
      th={
      0:'Null',
      1:'normal',
      2:'fixed defect',
      3:'reversable defect',
     }
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(15, 0, txt = "Thal : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(20, 0, txt = th.get(thal),
             ln = 1, align = 'L')
      
      pdf.line(x1 = 10, y1 = 235.5, x2 = 200, y2 = 235.5)
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(25, 30, txt = "Status : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(20,30, txt = heart_pred,
             ln = 1, align = 'L')
    # save the pdf with name .pdf
      pdf.output("Hp.pdf") 
      
      
      
      with open("Hp.pdf", "rb") as pdf_file:
          PDFbyte = pdf_file.read()

      st.download_button(label="Download Report", 
        data=PDFbyte,
        file_name="Heart_report.pdf",
        mime='application/octet-stream') 

#DIABETES PREDICTION SYSTEM
with tab2:
   st.header('Diabetes Prediction System')
   
   col1, col2, col3 = st.columns(3)
   
   with col1:
       Name = st.text_input('Name')
   
   with col2:
        Pregnancies = int(st.text_input('Number of Pregnancies',value=0))
   with col3:
       Glucose = int(st.text_input('Glucose Level',value=0))
   
   with col1:
       BloodPressure = int(st.text_input('Blood Pressure value',value=0))
   
   with col2:
       SkinThickness = int(st.text_input('Skin Thickness value',value=0))
   
   with col3:
       Insulin = int(st.text_input('Insulin Level',value=0))
   
   with col1:
       BMI = st.number_input('BMI value')
   
   with col2:
       DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value',format="%.3f")
   
   with col3:
       Age = int(st.text_input('Age of the Person',value=0))
   
   
   
   diab_diagnosis = ''
   
   column1 ,column2=st.columns(2)
   with column1:
       if st.button('Diabetes test Result'):
           diab_prediction = diabe_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
       
           
           diab_diagnosis = 'Diabetic' if (diab_prediction[0] == 1) else 'Non Diabetic'
      
       st.info(diab_diagnosis)
   with column2:
      
      
      
#PDF REPORT DIBETES
      pdf = FPDF('P', 'mm', 'A4')
     
     
      pdf.add_page()
      
      pdf.set_font('Arial', 'B', 24)
      pdf.cell(190, 10, txt = "Diabetes Report",ln = 1, align = 'C')
      pdf.line(x1 = 10, y1 = 27.5, x2 = 200, y2 = 27.5)
    
     
    
      pdf.set_font('Arial', 'B', 14)
      pdf.cell(20, 30, txt = "Name : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial',size=14)
      pdf.cell(10, 30, txt = Name,
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(15, 0, txt = "Age : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(10, 0, txt = str(Age),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(35, 30, txt = "Pregnancies : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(15, 30, txt = str(Pregnancies),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(25, 0, txt = "Glucose : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(10, 0, txt = str(Glucose),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(45, 30, txt = "BloodPressure : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(35, 30, txt = str(BloodPressure),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(40, 0, txt = "SkinThickness : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(20, 0, txt = str(SkinThickness),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(20, 30, txt = "Insulin : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(10, 30, txt = str(Insulin),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(20, 0, txt = "BMI : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(10, 0, txt = str(BMI),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(75, 30, txt = "Diabetes Pedigree Function : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(30, 30, txt = str(DiabetesPedigreeFunction),
             ln = 1, align = 'L')
      
      pdf.line(x1 = 10, y1 = 160.5, x2 = 200, y2 = 160.5)
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(20, 0, txt = "Status : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(10, 0, txt = str(diab_diagnosis),
             ln = 1, align = 'L')
    # save the pdf with name .pdf
      pdf.output("Dp.pdf") 
      
      
      
      with open("Dp.pdf", "rb") as pdf_file:
          PDFbyte = pdf_file.read()

      st.download_button(label="Download Report", 
        data=PDFbyte,
        file_name="Diabetes_report.pdf",
        mime='application/octet-stream') 
      
   
with tab3:
   st.header("Parkinson's Prediction System")
   
   col1, col2, col3 = st.columns(3)
   
   with col1:
       Nm = st.text_input('Name',key="N")
   
   with col2:
        Age = int(st.text_input('Ag',value=0))
   with col3:
       Fo = st.number_input('MDVP:Fo(Hz)',format="%.5f")
   
   with col1:
       MDVPFhi = st.number_input('MDVP:Fhi(Hz)',key="l1",format="%.5f")
   
   with col2:
       MDVPFlo = st.number_input('MDVP:Flo(Hz)',key="l2",format="%.5f")
   
   with col3:
       MDVPJitterpercent= st.number_input('MDVP:Jitter(%)',key="l3",format="%.5f")
   
   with col1:
       MDVPJitterAbs = st.number_input('MDVP:Jitter(Abs)',key="l4",format="%.5f")
   
   with col2:
       MDVPRAP= st.number_input('MDVP:RAP',key="l5",format="%.5f")
   
   with col3:
       MDVPPPQ = st.number_input('MDVP:PPQ',key="l6",format="%.5f")
   with col1:
       JitterDDP = st.number_input('Jitter:DDP',key="l7",format="%.5f")
   
   with col2:
       MDVPShimmer= st.number_input('MDVP:Shimmer',key="l8",format="%.5f")
   
   with col3:
       MDVPShimmerdB = st.number_input('MDVP:Shimmer(dB)',key="l9",format="%.5f")
   with col1:
       ShimmerAPQ3 = st.number_input('Shimmer:APQ3',key="l10",format="%.5f")
   
   with col2:
       ShimmerAPQ5= st.number_input('Shimmer:APQ5',key="l11",format="%.5f")
   
   with col3:
       MDVPAPQ = st.number_input('MDVP:APQ',key="l12",format="%.5f")
   with col1:
       NShimmerDDA = st.number_input('Shimmer:DDA',key="l13",format="%.5f")
   
   with col2:
       NHR= st.number_input('NHR',key="l14",format="%.5f")
   
   with col3:
       HNR = st.number_input('HNR',key="l15",format="%.5f")
   with col1:
       RPDE = st.number_input('RPDE',key="l16",format="%.6f")
   
   with col2:
       DFA= st.number_input('DFA',format="%.6f")
   
   with col3:
       spread1 = st.number_input('Spread1',format="%.6f")
   with col1:
       spread2 = st.number_input('Spread2',format="%.6f")
   
   with col2:
       D2 = st.number_input('D2',format="%.6f")
   
   with col3:
       PPE = st.number_input('PPE',format="%.6f")
   
   
   
   
   
   
   parkinson_diagnosis = ''
   
   column1 ,column2=st.columns(2)
   with column1:
       if st.button("Parkinson's Prediction Result"):
           parkinson_prediction = parkins_model.predict([[Fo, MDVPFhi, MDVPFlo, MDVPJitterpercent, MDVPJitterAbs, MDVPRAP, MDVPPPQ, JitterDDP,MDVPShimmer,MDVPShimmerdB,ShimmerAPQ3,ShimmerAPQ5,MDVPAPQ,NShimmerDDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
       
           
           parkinson_diagnosis = 'Positive' if (parkinson_prediction[0] == 1) else 'Negative'
      
       st.info(parkinson_diagnosis)
   with column2:
      
      
      
#PDF REPORT PARKINSON'S
      pdf = FPDF('P', 'mm', 'A4')
     
     
      pdf.add_page()
      
      pdf.set_font('Arial', 'B', 24)
      pdf.cell(190, 10, txt = "Parkinson's Report",ln = 1, align = 'C')
      pdf.line(x1 = 10, y1 = 27.5, x2 = 200, y2 = 27.5)
    
     
    
      pdf.set_font('Arial', 'B', 14)
      pdf.cell(20, 30, txt = "Name : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial',size=14)
      pdf.cell(10, 30, txt = Nm,
             ln = 0, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(85, 30, txt = "Age : ",
             ln = 0, align = 'R')
      pdf.set_font('Arial')
      pdf.cell(10, 30, txt = str(Age),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(35, 0, txt = "MDVP:Fo(Hz): ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(10, 0, txt = str(Fo),
             ln = 0, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(93, 0, txt = "MDVP:Fhi(Hz) : ",
             ln = 0, align = 'R')
      pdf.set_font('Arial')
      pdf.cell(10, 0, txt = str(MDVPFhi),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(40, 30, txt = "MDVP:Flo(Hz) : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(35, 30, txt = str(MDVPFlo),
             ln = 0, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(66, 30, txt = "MDVP:Jitter(%) : ",
             ln = 0, align = 'R')
      pdf.set_font('Arial')
      pdf.cell(20, 30, txt = str(MDVPJitterpercent),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(45, 0, txt = "MDVP:Jitter(Abs) : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(10, 0, txt = str(MDVPJitterAbs),
             ln = 0, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(77, 0, txt = "MDVP:RAP : ",
             ln = 0, align = 'R')
      pdf.set_font('Arial')
      pdf.cell(10, 0, txt = str(MDVPRAP),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(35, 30, txt = "MDVP:PPQ : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(30, 30, txt = str(MDVPPPQ),
             ln = 0, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(65, 30, txt = "Jitter:DDP : ",
             ln = 0, align = 'R')
      pdf.set_font('Arial')
      pdf.cell(10, 30, txt = str(JitterDDP),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(45, 0, txt = "MDVP:Shimmer : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(30, 0, txt = str(MDVPShimmer),
             ln = 0, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(78, 0, txt = "MDVP:Shimmer(dB) : ",
             ln = 0, align = 'R')
      pdf.set_font('Arial')
      pdf.cell(10, 0, txt = str(MDVPShimmerdB),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(45, 30, txt = "Shimmer:APQ3 : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(30, 30, txt = str(ShimmerAPQ3),
             ln = 0, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(68, 30, txt = "Shimmer:APQ5 : ",
             ln = 0, align = 'R')
      pdf.set_font('Arial')
      pdf.cell(10, 30, txt = str(ShimmerAPQ5),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(35, 0, txt = "MDVP:APQ : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(10, 0, txt = str(MDVPAPQ),
             ln = 0, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(95, 0, txt = "Shimmer:DDA : ",
             ln = 0, align = 'R')
      pdf.set_font('Arial')
      pdf.cell(10, 0, txt = str(NShimmerDDA),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(20, 30, txt = "NHR : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(10, 30, txt = str(NHR),
             ln = 0, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(87, 30, txt = "HNR : ",
             ln = 0, align = 'R')
      pdf.set_font('Arial')
      pdf.cell(10, 30, txt = str(HNR),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(20, 0, txt = "RPDE : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(10, 0, txt = str(RPDE),
             ln = 0, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(87, 0, txt = "DFA : ",
             ln = 0, align = 'R')
      pdf.set_font('Arial')
      pdf.cell(10, 0, txt = str(DFA),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(25, 30, txt = "Spread1 : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(10, 30, txt = str(spread1),
             ln = 0, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(91, 30, txt = "Spread2 : ",
             ln = 0, align = 'R')
      pdf.set_font('Arial')
      pdf.cell(10, 30, txt = str(spread2),
             ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(15, 0, txt = "D2 : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(10, 0, txt = str(D2),
             ln = 0, align = 'L')
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(92, 0, txt = "PPE : ",
             ln = 0, align = 'R')
      pdf.set_font('Arial')
      pdf.cell(10, 0, txt = str(PPE),
             ln = 1, align = 'L')
      
      pdf.line(x1 = 10, y1 = 210, x2 = 200, y2 = 210)
      
      
      pdf.set_font('Arial', 'B',size=14)
      pdf.cell(20, 30, txt = "Status : ",
             ln = 0, align = 'L')
      pdf.set_font('Arial')
      pdf.cell(10, 30, txt = str(parkinson_diagnosis),
             ln = 1, align = 'L')
    
      pdf.output("Pp.pdf") 
      
      
      
      with open("Pp.pdf", "rb") as pdf_file:
          PDFbyte = pdf_file.read()

      st.download_button(label="Download Report", 
        data=PDFbyte,
        file_name="Parkinson's_report.pdf",
        mime='application/octet-stream')                       


