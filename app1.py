import streamlit as st
import numpy as np
import pickle 
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()

Model= pickle.load(open('project_incident_impact.pkl','rb'))

def predict_impact(incident_state,active,reassignment_count,reopen_count,
       sys_mod_count,resolved_in_months,made_sla,contact_type,
                   knowledge,u_priority_confirmation,notify):
    
    input=np.array([[fun1(incident_state),fun2(active),reassignment_count,reopen_count,
       sys_mod_count,resolved_in_months,fun3(made_sla),fun4(contact_type)
                     ,fun9(knowledge),fun10(u_priority_confirmation),fun11(notify)]])
          
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
    <h2 style="color:white;text-align:center;"> Streamlit Incident Impact Prediction </h2>
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
    knowledge=st.selectbox("Knowledge base ?",('Yes','No'))
    u_priority_confirmation=st.selectbox("Priority Confirmation ?",('Yes','No'))
    notify=st.selectbox("Notified Through ?",('Send Email','Do Not Notify'))
        
    if st.button("Predict"):
        output=predict_impact(incident_state, active, reassignment_count, reopen_count, sys_mod_count, resolved_in_months, made_sla, contact_type, knowledge, u_priority_confirmation, notify)
        st.success("Incident will be impacted approximately {}".format(output))

if __name__=="__main__":
    main()

#!pip install -q streamlit





