import streamlit as st
import pandas as pd
# Set page configuration
st.set_page_config(
    page_title="Chemical Reaction Simulator",
    page_icon="🔬",
    layout="centered",
    initial_sidebar_state="collapsed"
)
# st.set_option('de.showTopBar', True)

# Custom CSS to style the page
st.markdown("""
    <style>
        .landing-title {
            font-size: 50px;
            color: #4A90E2;
            # text-align: center;
            font-weight: bold;
        }
        .landing-subtitle {
            font-size: 24px;
            color: #555;
            # text-align: center;
            margin-top: -10px;
        }
        
        .feature-section {
            margin-top: 10px;
        }
        .feature-section h3 {
            # text-align: center;
            color: #333;
        }
        .feature-section p {
            # text-align: center;   
            color: #777;
        }
        .footer {
            # text-align: center;
            margin-top: 50px;
            color: #aaa;
        }
        .footer a {
            color: #4A90E2;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='landing-title'>Welcome to the <span style='color: #f78393;'>ChemTech</span></h1>", unsafe_allow_html=True)
st.markdown("<p class='landing-subtitle' style='color: gray;'>Your Gateway to Advanced Chemical Learning and Simulation!</p>", unsafe_allow_html=True)

st.markdown("""
<div class='feature-section' style="margin-bottom: 50px;">
    <h2 style = "color: #4A90E2;">Why use our AI-powered tool..?</h2>
    <p style = "color: gray;">🔍 Explore over 100+ elements and their properties.</p>
    <p style = "color: gray;">📖 Easy understanding of Name Reactions and Benzene Reactions</p>
    <p style = "color: gray;">⚡ Perforom reactions with customized conditions and catalysts.</p>
    <p style = "color: gray;">🎨 Get detailed information on products, including structure and properties.</p>
    <p style = "color: gray;">📊 Visualize molecular weights and densities in a tabular format.</p>
    
</div>
""", unsafe_allow_html=True)


left2, right2 = st.columns(2)
    
with left2:
    if st.button("⌬ Benzene Reactions", type="secondary", use_container_width=True):
        st.switch_page("pages/1_Benzene Reactions.py")

with right2:    
    if st.button("👩‍🔬 Name Reactions", type="secondary", use_container_width=True):
        st.switch_page("pages/2_Name Reactions.py")


left1, right1 = st.columns(2)
with left1:
    # st.markdown ("Perform any reaction chemical reaction in seconds !")
    if st.button("⚗️ Basic Reactions", type="secondary", use_container_width=True):
        st.switch_page("pages/3_Basic Reactions.py")

with right1:
    if st.button("📊 Periodic Table", type="secondary", use_container_width=True):
        st.switch_page("pages/4_Periodic Table.py")
    
with st.sidebar:
    st.subheader("Made with ❤️ by ChemTech and Team", divider="red")
    st.image("asset/chem.gif", use_column_width=True,width=None)

@st.dialog("👥 Meet our team")
def show_team_members():
    st.subheader("Team ChemTech", divider="red")
    st.write("**Guided By:** Tushar P. Bagul")
    team_members = [
        {"Name of members": "Krupali J. Mali"},
        {"Name of members": "Ankita Kulkarni"},
        {"Name of members": "Rutuja Kokane"},
        {"Name of members": "Ankita K. Matere"},
        {"Name of members": "Vivek G. Chaudhari"}
    ]
    df = pd.DataFrame(team_members)
    st.dataframe(df, use_container_width=True, hide_index=True)
st.sidebar.button("👥 Meet our team", on_click=show_team_members, type="secondary", use_container_width=True)

st.markdown(
    """
    <footer style="text-align: center; margin-top: 20px;">
        <p style="font-size: 11px; margin-bottom: 5px; font-type: italic">✨ Powered by ChemTech - Where Chemistry Meets Innovation ✨</p>
    </footer>
    """,
    unsafe_allow_html=True
)
