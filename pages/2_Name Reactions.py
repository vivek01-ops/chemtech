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

@st.cache_data
# def load_compounds():
#     try:
#         return pd.read_csv('compounds.csv')
#     except FileNotFoundError:
#         st.error("The 'compounds.csv' file is missing.")
#         return pd.DataFrame()

# compounds_df = load_compounds()

# Utility function to convert HTML-like text to LaTeX
def convert_to_latex_format(text):
    return re.sub(r'<sub>(\d+)</sub>', r'_\1', text)

# Display the main page
st.title("Name Reactions Simulator")
st.subheader("Quick Revision of Name and Benzene Reactions", divider="red")

# Display the Name Reactions DataFrame
df_name_reactions = pd.DataFrame(name_reactions)
with st.expander("Show Name Reactions"):
    st.dataframe(df_name_reactions, use_container_width=True, hide_index=True)

# Input section for performing name reactions
st.subheader("Perform Name Reactions", divider="red")

reaction_name = st.selectbox(
    'Select a Reaction',
    df_name_reactions['Reaction Name'].tolist(),
    placeholder="Select at least one reaction",
    help="Choose the Name Reaction you want to perform."
)

compounds = st.text_input(
    'Enter Reactants (separated by commas)',
    placeholder="e.g., H2O, NaCl",
    help="Type the name or formula of reactants."
)

substrate = st.text_input(
    'Enter Substrates (separated by commas)',
    placeholder="e.g., ethanol, benzene",
    help="Type the name or formula of substrates."
)

catalyst = st.text_input(
    'Enter Catalysts (separated by commas)',
    placeholder="e.g., H2SO4, AlCl3",
    help="Type the name or formula of catalysts."
)

temperature = st.number_input('Temperature (K)', min_value=0, max_value=1000, value=300, step=1)

# Perform the reaction
if st.button('Perform Reaction'):
    if compounds:
        # Display input parameters
        st.write(f"**Reaction Selected:** {reaction_name}")
        st.header("Reaction Result", divider="red")

        with st.status('Performing the reaction...', expanded=True):
            st.toast('⏳ The reaction is being performed. This may take more than 40 seconds. Please wait...!')
            time.sleep(.5)
            try:
                # Generate the prompt for Google GenAI API
                model = genai.GenerativeModel("gemini-1.5-pro-002")
                prompt = (
                    f"Perform a reaction using the reactants {compounds}, catalysts {catalyst}, "
                    f"and substrates {substrate}. Show the product. Display the chemical formulas of "
                    f"reactants, catalysts, substrates, and products. Provide detailed information "
                    f"on the {reaction_name} reaction, including: 1. Definition, 2. Conditions (temperature, catalyst, etc.), "
                    f"3. Mechanism, and 4. General structure of the product in ASCII format. "
                    f"Describe the product with its chemical names and formulas."
                )

                # Call the API and fetch the response
                response = model.generate_content(prompt)
                result = response.text
                result = convert_to_latex_format(result)

                # Display the result
                st.write(result)
                st.success("Done", **{"icon": "✔"})
            except Exception as e:
                st.error(f"There was an error with the API request: {e}")

        st.warning("**Note:** The result is generated by AI and may require validation.")
    else:
        st.error("Please provide input for reactants, substrates, and catalysts.")

st.sidebar.subheader("About Name Reaction Simulator: ", divider="orange")
st.sidebar.info("📌 The Name Reactions and Benzene Reactions Simulator is an advanced AI-powered tool designed to help chemistry students to explore, learn and simulate chemical reactions. The app focuses on well-known Name Reactions and Benzene Reactions, offering detailed information about the mechanisms, conditions, and products of these reactions. Additionally, users can simulate reactions by selecting specific reactants and substrates, with detailed results generated using Generative AI.",)


