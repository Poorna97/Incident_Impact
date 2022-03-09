import streamlit as st
import numpy as np
import pickle 
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()

Model= pickle.load(open('project_incident_impact.pkl','rb'))

def predict_impact(incident_state,active,reassignment_count,reopen_count,
       sys_mod_count,resolved_in_months,made_sla,contact_type,location,category,
       subcategory,u_symptom,knowledge,u_priority_confirmation,notify):
    
    input=np.array([[fun1(incident_state),fun2(active),reassignment_count,reopen_count,
       sys_mod_count,resolved_in_months,fun3(made_sla),fun4(contact_type),fun5(location),fun6(category),
       fun7(subcategory),fun8(u_symptom),fun9(knowledge),fun10(u_priority_confirmation),fun11(notify)]])
          
    prediction = Model.predict(input)
    return prediction
    
def fun1(incident_state):
    if incident_state=='Active':
        return 1
    elif incident_state=='Awaiting Evidence':
        return 2
    elif incident_state=='Awaiting Problem':
        return 3
    elif incident_state=='Awaiting User info':
        return 4
    elif incident_state=='Awaiting Vendor':
        return 5
    elif incident_state=='Closed':
        return 6
    elif incident_state=='New':
        return 7
    elif incident_state=='Resolved':
        return 8
    return 0
    
def fun2(active):
    if active=='Active':
        return 1
    return 0

def fun3(made_sla):
    if made_sla=='Yes':
        return 1
    return 0

def fun4(contact_type):
    if contact_type=='Direct Opening':
        return 0
    elif contact_type=='IVR':
        return 1
    elif contact_type=='Email':
        return 2
    elif contact_type=='Self service':
        return 3
    return 4

loc=['Location '+str(i) for i in range(2,224,1)]
value1=np.array([[j] for j in range(0,224,1)])
value1=scaler.fit_transform(value1)
dic1={ i:j for i,j in zip(loc,value1) }

def fun5(location):
    if location in dic1.keys():
        location=dic1[location]
        return location
    
cat=['Category '+str(i) for i in range(2,58,1)]
value2=np.array([[j] for j in range(0,58,1)])
value2=scaler.fit_transform(value2)
dic2={ i:j for i,j in zip(cat,value2) }

def fun6(category):
    if category in dic2.keys():
        category=dic2[category]
        return category
    
subcat=['Subcategory '+str(i) for i in range(2,254,1)]
value3=np.array([[j] for j in range(0,254,1)])
value3=scaler.fit_transform(value3)
dic3={ i:j for i,j in zip(subcat,value3) }

def fun7(subcategory):
    if subcategory in dic3.keys():
        subcategory=dic3[subcategory]
        return subcategory

symptom=['u_symptom '+str(i) for i in range(2,525,1)]
value4=np.array([[j] for j in range(0,525,1)])
value4=scaler.fit_transform(value4)
dic4={ i:j for i,j in zip(symptom,value4) }

def fun8(u_symptom):
    if u_symptom in dic4.keys():
        u_symptom=dic4[u_symptom]
        return u_symptom

def fun9(knowledge):
    if knowledge=='Yes':
        return 1
    return 0

def fun10(u_priority_confirmation):
    if u_priority_confirmation=='Yes':
        return 1
    return 0

def fun11(notify):
    if notify=='Send Email':
        return 1
    return 0

def main():
    st.title('Incident Impact Prediction ')
    html_temp="""
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Used Incident Impact Prediction ML app </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    incident_state=st.selectbox("what is the incident state ?",('Active','Awaiting Evidence','Awaiting Problem','Awaiting User info','Awaiting Vendor','Closed','New','Resolved','Not Available')) 
    active=st.selectbox("Incident is active or not ?",('Active','Not Active'))
    reassignment_count=st.number_input("How many times has Incident been reassigned ?",min_value=0,step=1)
    reopen_count=st.number_input("How many times has Incident been reopened ?",min_value=0,step=1)
    sys_mod_count=st.number_input("How many times has Incident been updated ?",min_value=0,step=1)
    resolved_in_months=st.number_input("In how many months has Incident been resolved ?")
    made_sla=st.selectbox("Has SLA-(Service Level Agreement) met ?",('Yes','No'))
    contact_type=st.selectbox("Mode of contact ?",('Direct Opening','Email','IVR','Phone','Self Service'))
    location=st.selectbox("Location ?",(['Location '+str(i) for i in range(2,224,1)]))
    category=st.selectbox("Category ?",(['Category '+str(i) for i in range(2,58,1)]))
    subcategory=st.selectbox("Subcategory ?",(['Subcategory '+str(i) for i in range(2,254,1)]))
    u_symptom=st.selectbox("Symptom/Issue type ?",(['u_symptom '+str(i) for i in range(2,525,1)]))
    knowledge=st.selectbox("Knowledge base ?",('Yes','No'))
    u_priority_confirmation=st.selectbox("Priority Confirmation ?",('Yes','No'))
    notify=st.selectbox("Notified Through ?",('Send Email','Do Not Notify'))
        
    if st.button("Predict"):
        output=predict_impact(incident_state, active, reassignment_count, reopen_count, sys_mod_count, resolved_in_months, made_sla, contact_type, location, category, subcategory, u_symptom, knowledge, u_priority_confirmation, notify)
        st.success("Incident will be impacted approximately {}".format(output))

if __name__=="__main__":
    main()

#!pip install -q streamlit





