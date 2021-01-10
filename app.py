import streamlit as st
import numpy as np
#from streamlit_func import ShowVideo, VideoToAudio, ShowAudio, Generate_summary, clear_file
import io
import joblib

#page = st.sidebar.selectbox("Select a page", ["App"])
st.set_option('deprecation.showfileUploaderEncoding', False)



    
st.title('Activity Detection')
st.markdown('<h2> Write the X, Y and Z co-ordinates and get the activity  </h2>',unsafe_allow_html=True)
user_input = st.text_input("Input X, Y and Z value separated by a space")
if user_input:
    x,y,z=user_input.split(' ')
    
    try:
        x=int(x)
        y=int(y)
        z=int(z)
        
        a=[x,y,z]
        a=np.array(a)
        a=a.reshape(1, -1)
        clf3=joblib.load('model/knn.pkl')
        answer=clf3.predict(a)
        if answer==1:
            activity='Working at Computer'
        elif answer==3:
            activity='Standing'
        elif answer==4:
            activity='Walking'
        elif answer==6:
            activity='Walking and Talking with Someone'
        elif answer==7:
            activity='Talking while Standing'

        print(activity,answer)
        final_answer='<h3> The predicted activity is - '+activity+' (Code - '+str(answer[0])+')</h3>'
        st.markdown(final_answer,unsafe_allow_html=True)
        

        
    except:
        st.markdown('Enter valid numbers.',unsafe_allow_html=True)
    
    

    

    