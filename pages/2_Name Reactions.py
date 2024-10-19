from cgitb import text
import streamlit as st
import os
import time
import google.generativeai as genai
import pandas as pd
import re

# Set up API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyAdS57TfssxTs_Z0_YTXB3kikFv7KqWtA0"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

st.set_page_config(page_title="Name Reactions", page_icon="🧪", layout="wide", initial_sidebar_state="auto")


# Data for Name Reactions
name_reactions = {
    "Sr.No": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    ],
    "Reaction Name": [
        "Pinnacle-Pinacalon rearrangement",
        "Hafman's reaction",
        "Baeyer-Villiger oxidation",
        "Benzilic acid rearrangement",
        "Beckmann's rearrangement",
        "Claisen-Schmidt condensation",
        "Schmidt rearrangement",
        "Clemmensen reduction",
        "Wolff rearrangement",
        "Oppenauer oxidation",
        "Dakin reaction",
        "Birch reduction"
    ],
    "Description": [
        "Rearrangement of pinacol to pinacolone through acid catalysis.",
        "Elimination of an alcohol from a β-hydroxy ketone to form an α,β-unsaturated carbonyl compound.",
        "Oxidation of ketones to esters using peracids (e.g., peracetic acid).",
        "Rearrangement of benzil to benzilic acid via nucleophilic attack on the carbonyl.",
        "Rearrangement of oximes to amides in the presence of acid.",
        "Condensation of two esters or an ester and a carbonyl compound in the presence of a base.",
        "Rearrangement of primary amides to amines and carboxylic acids upon treatment with nitrous acid.",
        "Reduction of ketones or aldehydes to alkanes using zinc amalgam and hydrochloric acid.",
        "Rearrangement of α-ketoacids to form isocyanides upon treatment with a base.",
        "Oxidation of alcohols to ketones using aluminum alkoxides as catalysts.",
        "Reaction of aromatic aldehydes with hydrogen peroxide to form phenols.",
        "Reduction of aromatic compounds to cyclohexadienes using sodium in liquid ammonia."
    ],
    "Molecular Formula": [
        "C6H12O2 (Pinacol); C6H10O (Pinacolone)",
        "C6H10O (β-hydroxy ketone); C6H10O (α,β-unsaturated carbonyl)",
        "C4H8O2 (Acetic acid); C5H10O2 (Ethyl acetate)",
        "C14H12O3 (Benzilic acid)",
        "C5H9NO (Oxime); C5H11NO (Amide)",
        "C9H10O2 (Alkylated product)",
        "C4H9NO (Amide); C5H11NO2 (Amines and acids)",
        "C6H12O (Ketone); C6H14 (Alkane)",
        "C3H4O2 (α-keto acid); C3H5NO (Isocyanide)",
        "C6H14O (Alcohol); C6H12O (Ketone)",
        "C6H6O (Phenol)",
        "C6H6 (Benzene); C6H10 (Cyclohexadiene)"
    ]
}

def convert_to_latex_format(text):
    return re.sub(r'<sub>(\d+)</sub>', r'_\1', text)

# Function to load elements from CSV
def load_compounds():
    return pd.read_csv('compounds .csv')

compounds_df = load_compounds()


# Create DataFrames

st.title("Name Reactions")

st.subheader("Have a quick revision on Name and Benzene Reactions", divider="red")
df1 = pd.DataFrame(name_reactions)
# df2 = pd.DataFrame(benzene_reactions)
with st.expander("Show Name Reactions"):
        st.dataframe(df1, use_container_width=True, hide_index=True)

# User input for reaction details
st.subheader("Perform Name Reactions", divider="red")
    
    # Input fields for user to enter new reaction details
reaction_name = st.selectbox(
        'Select Reactants',
        df1['Reaction Name'].tolist(),
        placeholder="Select at least one reaction",
        help="Choose the Name Reaction you want to perform.",
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
            # Display input parameters
            st.write(f"**You Selected:** {reaction_name}")
            # st.write(f"**You Selected:** {benzene}")
            st.header("Result", divider="red")   
        
            with st.status('Performing the reaction...', expanded=True):
                try:
                    # Send prompt to Google genai API
                    model = genai.GenerativeModel("gemini-1.5-pro-002")
                    # Combine the prompt into one string
                    prompt = (
                        f"perform a reaction using the reactants {', '.join(compounds)} , {', '.join(catalyst)}and the substrates {', '.join(substrate)}. show the product."
                        f"Display the reaction"
                        f"display the chemical formulas of reactants {', '.join(compounds)} , {', '.join(catalyst)}and the substrates {', '.join(substrate)} and products."
                        f"Provide detailed information on the {reaction_name} reaction, including: "
                        f"1. Definition, "
                        f"2. Conditions (temperature, catalyst, etc.), "
                        f"3. Mechanism "
                        f"4. General structure of the product in ASCII format.\n"   
                        f"under the typical conditions of {reaction_name}, and describe product with its chemical names and chemical formulas"
                    )

                    response = model.generate_content(prompt)
                    result = response.text
                    result = convert_to_latex_format(result)
                    sections = result.split("\n\n")   # Assuming the response is divided by two newlines between sections
                    st.write(sections)
                    st.success("Done", **{"icon": "✔"})
                except Exception as e:
                    st.error(f"**Error:** There was an issue with the API request: {e}")
                    
            st.warning("Result is generated by Generative AI, it can make mistakes in some cases, please cross check the result from your side")
        else:
            st.error("Please ensure that you have provided inputs of both **reactants** and **substrate**.")

st.sidebar.subheader("About Name Reaction Simulator: ", divider="orange")
st.sidebar.info("📌 The Name Reactions and Benzene Reactions Simulator is an advanced AI-powered tool designed to help chemistry students to explore, learn and simulate chemical reactions. The app focuses on well-known Name Reactions and Benzene Reactions, offering detailed information about the mechanisms, conditions, and products of these reactions. Additionally, users can simulate reactions by selecting specific reactants and substrates, with detailed results generated using Generative AI.",)


