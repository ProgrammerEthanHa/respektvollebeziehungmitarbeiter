import streamlit as st
import pandas as pd
import altair as alt

st.header("Wie respektvolle Beziehungen mit der Führungskraft auf die Mitarbeiter auswirken")
st.subheader(" ")

source = pd.DataFrame({
        'Anteil(%)': [58, 63, 55],
        'Meinung': ['sich mehr auf ihre Arbeit konzentrieren', 'zufriedener', 'engagierter']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Meinung:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    /
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle:  Gitnux")