from cgitb import text
import streamlit as st
import os
import time
import google.generativeai as genai
import pandas as pd

# Set up API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyAdS57TfssxTs_Z0_YTXB3kikFv7KqWtA0"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

st.set_page_config(page_title="Benzene Reactions", page_icon="⚛️", layout="wide", initial_sidebar_state="auto")



# Data for Benzene Reactions
benzene_reactions = {
    "Sr.No": [
        1, 2, 3, 4, 5
    ],
    "Reaction Name": [
        "Halogenation",
        "Nitration",
        "Sulfonation",
        "Friedel-Crafts Alkylation",
        "Friedel-Crafts Acylation"
    ],
    "Reaction Overview": [
        "Electrophilic aromatic substitution of benzene with halogens (Cl₂, Br₂).",
        "Electrophilic aromatic substitution of benzene with nitric acid to form nitrobenzene.",
        "Electrophilic aromatic substitution of benzene with sulfur trioxide (SO₃) to form benzene sulfonic acid.",
        "Electrophilic aromatic substitution where an alkyl group is introduced into benzene.",
        "Electrophilic aromatic substitution where an acyl group is introduced into benzene."
    ],
    "Catalyst": [
        "FeCl₃ (Ferric chloride) or AlCl₃ (Aluminum chloride)",
        "H₂SO₄ (Sulfuric acid)",
        "H₂SO₄ (Sulfuric acid)",
        "AlCl₃ (Aluminum chloride)",
        "AlCl₃ (Aluminum chloride)"
    ]
}


# Function to load elements from CSV
def load_elements():
    return pd.read_csv('elements.csv')

elements_df = load_elements()


# Create DataFrames
st.title("Benzene Reactions")

st.subheader("Have a quick revision on Name and Benzene Reactions", divider="red")

df2 = pd.DataFrame(benzene_reactions)

with st.expander("Show Benzene Reactions"):
        st.dataframe(df2, use_container_width=True, hide_index=True)

st.subheader("Perform Benzene Reactions", divider="red")
    

benzene = st.selectbox(
        'Select Benzene Reaction',
        df2['Reaction Name'].tolist(),
        placeholder="Select at least one reaction",
        help="Choose the Benzene Reaction you want to perform.",
)   
compounds = st.text_input(
        'Enter Reactants (**seperated by commas**)',
        # compounds_df['Compounds'].tolist(),

        placeholder="Select at least one reaction",
        help="Type the name or formula of reactant",
)

substrate = st.text_input(
        'Enter Substrate (**seperated by commas**)',
        # compounds_df['Compounds'].tolist(),

        placeholder="Select at least one reaction",
        help="Type the name or formula of substrate",
    )

catalyst = st.text_input(
        'Enter Catalyst (**seperated by commas**)',
        # compounds_df['Compounds'].tolist(),

        placeholder="Select at least one reaction",
        help="Type the name or formula of catalyst",
    )
temperature = st.number_input('Temperature (K)', min_value=0, max_value=1000, value=300, step=1)    

    # Trigger the Reaction Simulation
if st.button('Perform Reaction'):
        if compounds:
            st.write(f"**You Selected:** {benzene}")
            st.subheader("Result", divider="red")   
        
            with st.status('Performing the reaction...', expanded=True):
                try:
                    # Send prompt to Google genai API
                    model = genai.GenerativeModel("gemini-1.5-pro-002")
                    # Combine the prompt into one string
                    prompt = (
                        f"Provide detailed information on the {benzene} reaction, including: "
                        f"1. Definition, "
                        f"2. Conditions (temperature, catalyst, etc.), "
                        f"3. Mechanism, and "
                        f"4. General structure of the product in ASCII format.\n"   
                        f"Also, perform a reaction using the reactants {', '.join(compounds)} , {', '.join(catalyst)}and the substrates {', '.join(substrate)}. And show the reaction also"
                        f"under the typical conditions of {benzene} reaction, and describe the  expected product with its chemical names."
                        f"Show headings in bold and slightly bigger font size "
                    )

                    response = model.generate_content(prompt)
                    
                    # Display the result of the reaction
                    result = response.text
                    sections = result.split("\n\n")   # Assuming the response is divided by two newlines between sections
                    st.write(result)
                    st.success("Done", **{"icon": "✔"})
                except Exception as e:
                    st.error(f"**Error:** There was an issue with the API request: {e}")
        else:
            st.error("Please select at least one reactant.")

st.sidebar.subheader("About Name Reaction Simulator: ", divider="orange")
st.sidebar.info("📌 The Name Reactions and Benzene Reactions Simulator is an advanced AI-powered tool designed to help chemistry students to explore, learn and simulate chemical reactions. The app focuses on well-known Name Reactions and Benzene Reactions, offering detailed information about the mechanisms, conditions, and products of these reactions. Additionally, users can simulate reactions by selecting specific reactants and substrates, with detailed results generated using Generative AI.",)


