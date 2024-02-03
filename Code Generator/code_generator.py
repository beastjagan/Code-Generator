# import gradio as gr
# import google.generativeai as palm

# # Replace 'YOUR_API_KEY' with your actual API key
# palm.configure(api_key='AIzaSyBCJ0KPSLfwq9LCdg0R8aQrd_z07eqyGcE')

# # List available models
# models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
# model = models[0].name if models else None

# def generate_code(prompt):
#     if model:
#         completion = palm.generate_text(
#             model=model,
#             prompt=prompt,
#             temperature=0.8,
#             max_output_tokens=200,
#         )
#         response = completion.result
#         return response
#     else:
#         return "No suitable models found."

# # Define the Gradio UI
# iface = gr.Interface(
#     fn=generate_code,
#     inputs=gr.Textbox(label="Enter a prompt to generate code", lines=5),
#     outputs=gr.Textbox(label="Generated Code", lines=10),
#     title="Python Code Generator",
# )

# # Launch the Gradio app
# iface.launch(share=True)

# import gradio as gr
# import google.generativeai as palm

# # Replace 'YOUR_API_KEY' with your actual API key
# palm.configure(api_key='AIzaSyBCJ0KPSLfwq9LCdg0R8aQrd_z07eqyGcE')

# # List available models
# models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
# model = models[0].name if models else None

# def generate_code(prompt):
#     if model:
#         completion = palm.generate_text(
#             model=model,
#             prompt=prompt,
#             temperature=0.8,
#             max_output_tokens=200,
#         )
#         response = completion.result
#         return response
#     else:
#         return "No suitable models found."

# # Define the Gradio UI
# iface = gr.Interface(
#     fn=generate_code,
#     inputs=gr.Textbox(label="Enter a prompt to generate code", lines=5),
#     outputs=gr.Textbox(label="Generated Code", lines=20),  # Increased lines for better visibility
#     live=True,  # Enable live updates
#     title="Code Generator",
#     description="Generate code based on your prompt.",
# )

# # Launch the Gradio app
# iface.launch(share=True)

import streamlit as st
import google.generativeai as palm

# Replace 'YOUR_API_KEY' with your actual API key
palm.configure(api_key='AIzaSyBCJ0KPSLfwq9LCdg0R8aQrd_z07eqyGcE')


# List available models
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name if models else None

def generate_code(prompt):
    if model:
        completion = palm.generate_text(
            model=model,
            prompt=prompt,
            temperature=0.8,
            max_output_tokens=200,
        )
        response = completion.result
        return response
    else:
        return "No suitable models found."

# Streamlit app
st.title("Code Generator")

# Input prompt
prompt = st.text_area("Enter a prompt to generate code", height=100)

# Generate code button
if st.button("Generate Code"):
    # Generate code and display
    generated_code = generate_code(prompt)
    st.text_area("Generated Code", generated_code, height=400)

# Note: Streamlit automatically handles the web app rendering and updates.


