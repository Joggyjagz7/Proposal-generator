pip install openai

import openai as ai
import json
import streamlit as st 


print("** Loading API Key")
ai.api_key = "API KEY HERE"

st.title("Jagz Generator")
st.markdown("# Proposal Generator 📄📃")
st.sidebar.markdown("# Proposal Generator 📄📃")

with st.sidebar: 
    model_used = st.selectbox(
     'GPT-3 Model',
    #  ('DaVinci', 'Curie', 'Babbage', 'Ada'))
    ('text-davinci-002', 'text-curie-001', 'text-babbage-001', 'text-ada-001'))

    if model_used == 'text-davinci-002': 
        st.markdown("""[Davinci](https://beta.openai.com/docs/models/davinci) is the most capable model family and can perform any task the other 
        models can perform and often with less instruction. For applications requiring a lot of 
        understanding of the content, like summarization for a specific audience and creative content
         generation, Davinci is going to produce the best results. These increased 
         capabilities require more compute resources, so Davinci costs more per API call and is not as fast as the other models.
        """)
        # st.markdown("""
        # Good at: 
        #     * Complex intent
        #     * cause and effects
        #     * summarization for audience
        # """)
    elif model_used == 'text-curie-001': 
        st.markdown("""[Curie](https://beta.openai.com/docs/models/curie) is extremely powerful, yet very fast. While Davinci is stronger when it 
        comes to analyzing complicated text, Curie is quite capable for many nuanced tasks like sentiment 
        classification and summarization. Curie is also quite good at answering questions and performing 
        Q&A and as a general service chatbot.
        """)
    elif model_used == 'text-babbage-001': 
        st.markdown("""[Babbage](https://beta.openai.com/docs/models/babbage) can perform straightforward tasks like simple classification. It’s also quite 
        capable when it comes to Semantic Search ranking how well documents match up with search queries.
        """)
    else: 
        st.markdown("""[Ada](https://beta.openai.com/docs/models/ada) is usually the fastest model and can perform tasks like parsing text, address 
        correction and certain kinds of classification tasks that don’t require too much nuance. 
        da’s performance can often be improved by providing more context.
        """)
    st.markdown("**Note:** Model descriptions are taken from the [OpenAI](https://beta.openai.com/docs) website")

