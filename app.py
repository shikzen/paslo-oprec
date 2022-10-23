# Library import
import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

# Page setup
st.set_page_config(
    page_title="PASL Oprec",
    page_icon="favicon.png",
    layout="wide"
)

#Importing the data
dfQuan = pd.read_excel(
    io='dataform.xlsx',
    engine='openpyxl',
    sheet_name='Quan_TAspect'
)

dfFund = pd.read_excel(
    io='dataform.xlsx',
    engine='openpyxl',
    sheet_name='Motlet-Fund'
)

dfQual = pd.read_excel(
    io='dataform.xlsx',
    engine='openpyxl',
    sheet_name='Cleaned-Qual'
)

dfQuanfull = pd.read_excel(
    io='dataform.xlsx',
    engine='openpyxl',
    sheet_name='Quan-Aspect'
)

# Filter sidebar
st.sidebar.header("Filter Feature")
eligibility = st.sidebar.multiselect(
    "Filter Eligibility from Qualitative Data:",
    options=dfQual["Eligibility"].unique(),
    default=dfQual["Eligibility"].unique(),
)

df_selQual = dfQual.query(
    "Eligibility == @eligibility"
)

caaslab = st.sidebar.multiselect(
    "Filter Interviewee Motivation from Fundamental Data:",
    options=dfFund["CAASLAB"].unique(),
    default=dfFund["CAASLAB"].unique(),
)

df_selFund = dfFund.query(
    "CAASLAB == @caaslab"
)

#Mainpage
row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
with row0_1:
    st.title(":office: Public Administration Science Laboratory - Open Recruitment")
with row0_2:
    st.text("")
    st.subheader("Interactive Dashboard by [Virgilnr](https://twitter.com/virgilnrf)")
st.markdown("##")
with row0_1:
    st.markdown("Welcome to the Interactive Dashboard of PASL Oprec. This dashboard was made to make ease of the proccess of analysis from three perspective: Quantitaively, Qualitatively, and Fundamentally. I hope the data will be clear as sunshine :sun_with_face:")
with row0_2:
    st.markdown("There are some term about that really helpful to understand, click below")
    see_term = st.expander("Important Term ⚡")
    st.markdown("You could dowload the full dataset on [this link](https://docs.google.com/spreadsheets/d/1EUaZ5-1Qi2cyKqmEDd6UwZEJ68Xp75U0/edit?usp=sharing&ouid=112546519604793725864&rtpof=true&sd=true)")
    with see_term:
        st.markdown("* **UN**: Understanding (Interviewee understanding about onself and lab)")
        st.markdown("* **WI**: Will (Interviewee will and commitment to contribute to lab)")
        st.markdown("* **WE**: Work Ethics (Interviewee perspectuve on work ethcis in organization)")
        st.markdown("* **PS**: Problem Solving (Interviewee perspective on problem solving)")
        st.markdown("* **VAL**: Value (What Interviewee value the most)")
        st.markdown("* **AT_UN**: Accumulation of Understanding Variable")
        st.markdown("* **AT_WI**: Accumulation of Will Variable")
        st.markdown("* **AT_WE**: Accumulation of Work Ethics Variable")
        st.markdown("* **AT_PS**: Accumulation of Problem Solving Variable")
        st.markdown("* **AT_VAL**: Accumulation of Value Variable")
        st.markdown("* **AT_OVL**: Accumulation of All Variable - Overall")
row3_spacer1, row3_1, row3_spacer2 = st.columns((.2, 7.1, .2))
with row3_1:
    st.markdown("")
    see_data_quan = st.expander("You can click here to see the summary of Quantitative data Used 🧮")
    with see_data_quan:
        st.dataframe(data=dfQuan.reset_index(drop=True))
        st.markdown("> Quantitative data is the data collected and proccessed by counting the average of every variable accumulated such as *Understanding (AT_UN)*, *Will (AT_WI)*, *Work Ethics (AT_WE)*, *Problem Solving (AT_PS)*, and *Value (AT_VAL)*. The resulted average then make up a total average know as *AT_OVL* or *Accumulated Overall*")
    st.markdown("")
    see_data_fund = st.expander("You can click here to see the summary of Qualitative data Used 🦸")
    with see_data_fund:
        st.dataframe(data=df_selQual.reset_index(drop=True))
        st.markdown("> Qualitative data is the data collected based on interview session. In this data, subjectivity of the interviewer matters.")
    st.markdown("")
    see_data_fund = st.expander("You can click here to see the summary of Fundamental data Used 🧱")
    with see_data_fund:
        st.dataframe(data=df_selFund.reset_index(drop=True))
        st.markdown("> Fundamental data is the data collected based on interpreting interviewee Motivation Letter")

# Quantitative Analysis
st.subheader('Quantitative Analysis :bar_chart:')
st.markdown("Quantitative analysis show stats for every interviewee. Every aspect analyzed from the interview session are shown here. You could use what aspect you want to analyze.")

#bar chart
col1, col2 = st.columns(2)
with col1:
    see_inv_ovl = st.expander("You can click here to see Quantitative Analysis based on Overall Score 💡")
    with see_inv_ovl:
        # Overall bar
        inv_ovl = (
            dfQuan[["CAASLAB", "AT_OVL"]].sort_values(by="AT_OVL")
        )
        fig_inv_ovl = px.bar(
            inv_ovl,
            x="AT_OVL",
            y="CAASLAB",
            orientation="h",
            title="<b> Overall Score Bar Chart </b>",
            template="plotly_dark",
            labels={
                "CAASLAB":"Calon Asisten Laboratorium",
                "AT_OVL":"Overall Aspect"
            }
        )
        fig_inv_ovl.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False))
        )
        st.plotly_chart(fig_inv_ovl, use_container_width=True)

with col2:
    see_per_asp = st.expander("You can click here to see every analyzed aspect in Quantitative analysis 🔖")
    with see_per_asp:
        # Understanding bar
        inv_un = (
            dfQuan[["CAASLAB", "AT_UN"]].sort_values(by="AT_UN")
        )
        fig_inv_un = px.bar(
            inv_un,
            x="AT_UN",
            y="CAASLAB",
            orientation="h",
            title="<b> Understanding Score Bar Chart </b>",
            template="plotly_dark",
            labels={
                "CAASLAB":"Calon Asisten Laboratorium",
                "AT_UN":"Understanding Aspect"
            }
        )
        fig_inv_un.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False))
        )
        st.plotly_chart(fig_inv_un, use_container_width=True)

        # Will bar
        inv_wi = (
            dfQuan[["CAASLAB", "AT_WI"]].sort_values(by="AT_WI")
        )
        fig_inv_wi = px.bar(
            inv_wi,
            x="AT_WI",
            y="CAASLAB",
            orientation="h",
            title="<b> Will Score Bar Chart </b>",
            template="plotly_dark",
            labels={
                "CAASLAB":"Calon Asisten Laboratorium",
                "AT_WI":"Will Aspect"
            }
        )
        fig_inv_wi.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False))
        )
        st.plotly_chart(fig_inv_wi, use_container_width=True)

        # Work Ethics bar
        inv_we = (
            dfQuan[["CAASLAB", "AT_WE"]].sort_values(by="AT_WE")
        )
        fig_inv_we = px.bar(
            inv_we,
            x="AT_WE",
            y="CAASLAB",
            orientation="h",
            title="<b> Work Ethics Score Bar Chart </b>",
            template="plotly_dark",
            labels={
                "CAASLAB":"Calon Asisten Laboratorium",
                "AT_WE":"Work Ethics"
            }
        )
        fig_inv_we.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False))
        )
        st.plotly_chart(fig_inv_we, use_container_width=True)

        # Problem Solving Bar
        inv_ps = (
            dfQuan[["CAASLAB", "AT_PS"]].sort_values(by="AT_PS")
        )
        fig_inv_ps = px.bar(
            inv_ps,
            x="AT_PS",
            y="CAASLAB",
            orientation="h",
            title="<b> Problem Solving Bar Chart </b>",
            template="plotly_dark",
            labels={
                "CAASLAB":"Calon Asisten Laboratorium",
                "AT_PS":"Problem Solving Aspect"
            }
        )
        fig_inv_ps.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False))
        )
        st.plotly_chart(fig_inv_ps, use_container_width=True)

        # Value bar
        inv_val = (
            dfQuan[["CAASLAB", "AT_VAL"]].sort_values(by="AT_VAL")
        )
        fig_inv_val = px.bar(
            inv_val,
            x="AT_VAL",
            y="CAASLAB",
            orientation="h",
            title="<b> Value Score Bar Chart </b>",
            template="plotly_dark",
            labels={
                "CAASLAB":"Calon Asisten Laboratorium",
                "AT_VAL":"Value Aspect"
            }
        )
        fig_inv_val.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False))
        )
        st.plotly_chart(fig_inv_val, use_container_width=True)

# Qualitative and Fundamental Analysis
st.subheader('Fundamental and Qualitative Analysis :cloud:')
st.markdown("Fundamental dan qualitative analysis show interviewee's reasoning and personal understanding about PASLab. This analysis is based on Motivation Letter and Reasoning. With this, we will have a deeper understanding about interviewee psychological side such as motivation.")
row3_spacer1, row3_1, row3_spacer2 = st.columns((.2, 7.1, .2))
with row3_1:
    st.markdown("")
    see_data_qf = st.expander("You can click here to see the Fundamental and Qualitative Analysis")
    with see_data_qf:
        slctbx = st.selectbox(
            "Interviewee Name",
            (dfFund["CAASLAB"]),
            )
        dfSlbx = dfFund.query(
            "CAASLAB==@slctbx"
        )
        st.dataframe(data=dfSlbx.reset_index(drop=True))
        st.markdown("> Understanding the reasoning and motivation of the interviewee")