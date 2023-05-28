import openai as ai
import json
import streamlit as st 


print("** Loading API Key")
ai.api_key = st.secrets["pass"]

st.markdown("# Proposal Letter Generator 📄")
st.sidebar.markdown("# What is a Proposal Letter 📄")

with st.sidebar: 
    """  A proposal letter is a formal document that is written to present a specific idea, project, product, or service to a potential client, partner, investor, or organization. It serves as an introduction and provides a summary of the proposed concept, highlighting its benefits, objectives, and value proposition.

A well-crafted proposal letter aims to persuade the recipient to consider the proposal and take further action, such as scheduling a meeting, providing funding, entering into a partnership, or accepting a business proposal.

Here are some key components typically included in a proposal letter:

Sender's Information: The letter should begin with the sender's contact information, including their name, title, company name, address, phone number, and email address.

Date: The date when the letter is written.

Recipient's Information: The letter should include the recipient's name, title, company name, and address. If possible, address the letter to a specific person rather than using a generic salutation.

Salutation: A formal greeting, such as "Dear Mr./Ms. [Recipient's Last Name],"

Introduction: Begin the letter by introducing yourself and your company. Provide a brief overview of your background and establish credibility.

Purpose: Clearly state the purpose of the letter and the proposal you are presenting. Explain the problem or opportunity you have identified and how your proposal can address it.

Proposal Details: Provide a comprehensive description of your proposal, including the key features, benefits, and advantages it offers. Use persuasive language and supporting evidence to make your case.

Implementation Plan: Outline the steps and timeline for implementing the proposal. Explain how the recipient will benefit from your proposal and any specific actions required from their end.

Call to Action: Clearly state the desired next steps or actions you want the recipient to take, such as scheduling a meeting, requesting additional information, or providing feedback.

Closing: Thank the recipient for their time and consideration. Include your contact information once again and express your willingness to answer any questions or provide further details.

Sincerely: End the letter with a formal closing, such as "Sincerely" or "Best regards," followed by your name and signature.

A well-written proposal letter should be concise, persuasive, and tailored to the recipient's needs and interests. It should highlight the value and uniqueness of your proposal while addressing any potential concerns or objections.
"""



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



# Define the conversation history

conversation = []
model_name = 'gpt-3.5-turbo'
model_name_2 = 'davinci'

# # Input form for user's proposal topic
# user_input = st.text_input("Enter the proposal topic:")
# if user_input:
#     # Add user's proposal topic to conversation history
#     conversation.append({'role': 'user', 'content': user_input})

#     # Generate a response from the model
#     response = ai.Completion.create(
#         model=model_name,
#         messages=conversation,
#         max_tokens=100,
#         n=1,
#         stop=None,
#         temperature=0.7
#     )

#     # Add model's response to conversation history
#     conversation.append({'role': 'assistant', 'content': response.choices[0].text.strip()})

# # Display conversation history
# for message in conversation:
#     if message['role'] == 'user':
#         st.text_input("User:", message['content'], key=message['content'])
#     else:
#         st.text_input("Assistant:", message['content'], key=message['content'])


# New Proposal Gen
#Write a proposal that starts with an introduction, backgorund, pitch, our apporach, proposed services, about us

with st.form(key='my_form_to_submit'):    
    your_name = st.text_input("Full Name ", "Maggie")
    your_title = st.text_input("Title ", "Director")
    receipent_name=st.text_input("Recipient Name")
    company_name = st.text_input("Recipient Company Name")
    brand = st.text_input("What kind of proposal is it?" )
    #contact_person = st.text_input("Who are you sending this too? ", "Commuincations Manager, CEO")
    value_proposition= st.text_input("What is your value propostion?")
    submit_button = st.form_submit_button(label="Generate")
    # 
    # personal_exp = st.text_input("I have experience in...", "natural language processing, fraud detection, statistical modeling, and machine learning algorithms. ")
    # job_desc = st.text_input("I am excited about the job because...", "this role will allow me to work on technically challenging problems and create impactful solutions while working with an innovative team. " )
    # passion = st.text_input("I am passionate about...", "solving problems at the intersection of technology and social good.")
    # job_specific = st.text_input("What do you like about this job? (Please keep this brief, one sentence only.) ")
    # specific_fit = st.text_input("Why do you think your experience is a good fit for this role? (Please keep this brief, one sentence only.) ")
    

prompt = ("Write a Proposal Letter to " + receipent_name + " from " + your_name + " and " + your_title + " for a " +  brand + "propsal for " + company_name +"." + "Incude the "+ value_proposition +" The proposal should an introduction, a background, a proposal pitch, a concise call to action,  and it should end with greeting. Think about each step properly and write it accurately and well ")

if submit_button:
    # The Model
    response = ai.Completion.create(
        engine = model_name,
        # engine="text-davinci-002", # OpenAI has made four text completion engines available, named davinci, ada, babbage and curie. We are using davinci, which is the most capable of the four.
        prompt=prompt, # The text file we use as input (step 3)
        max_tokens= 1000, # how many maximum characters the text will consists of.
        temperature=0.99,
        # temperature=int(temperature), # a number between 0 and 1 that determines how many creative risks the engine takes when generating text.,
        top_p= 10, # an alternative way to control the originality and creativity of the generated text.
        n=1, # number of predictions to generate
        frequency_penalty=0.3, # a number between 0 and 1. The higher this value the model will make a bigger effort in not repeating itself.
        presence_penalty=0.9 # a number between 0 and 1. The higher this value the model will make a bigger effort in talking about new topics.
    )


    text = response['choices'][0]['text']
    print("Prompt:", prompt)
    print("Response:", text)

    st.subheader("ProposalLetter Prompt")
    st.write(prompt)
    st.subheader("Auto-Generated Proposal Letter")
    st.write(text)
    st.download_button(label='Download Proposal Letter', file_name='proposal_letter.txt', data=text)

    # print("Other results:", response)

    with open('proposal_letters.txt', 'a') as f:
        f.write(text)