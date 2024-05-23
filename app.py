import streamlit as st
import pandas as pd
import numpy as np

# Titel und Einführung
st.title("MDM SW13 schneli3: Datenanalyse mit Streamlit")
st.markdown("""
### Anforderungen an die App:
1. **Laden Sie innerhalb der App ein Beispiel-Datenset aus dem Netz**
2. **Stellen Sie die Daten aufbereitet dar (Tabelle oder Grafiken)**
3. **Die Anzeige soll durch Eingabefelder (z.B. Radio-Buttons oder Slider) steuerbar sein**
""")

# Abschnitt 1: Beispielhafte Datentabelle
st.header("Beispielhafte Datentabelle")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# Abschnitt 2: Zufällige Daten für ein Liniendiagramm
st.header("Zufällige Daten für ein Liniendiagramm")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

# Abschnitt 3: Formular zur Eingabe
st.header("Formular zur Eingabe")
with st.form("my_form2"):
    st.write("Bitte füllen Sie das Formular aus:")
    slider_val = st.slider("Form Slider")
    checkbox_val = st.checkbox("Form Checkbox")
    # Submit-Button für das Formular
    submitted2 = st.form_submit_button("Submit")
    if submitted2:
        st.write("Ergebnis des Formulars:")
        st.write("Slider:", slider_val, "Checkbox:", checkbox_val)

# Schaltfläche zum Wechseln der Nachricht
st.header("Interaktive Nachricht")
if st.button('Say Goodbye', key="button1"):
    st.write('Goodbye')
else:
    st.write('Hello')

# Abschnitt 4: Beispiel-Datenset aus dem Netz laden und anzeigen
st.header("Beispiel-Datenset aus dem Netz")
@st.cache_data
def load_data():
    url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
    return pd.read_csv(url)

data = load_data()

st.write("### Das Iris-Dataset")
st.write(data.head())

# Eingabefelder zur Steuerung der Anzeige
st.header("Steuerung der Datenanzeige")
option = st.selectbox(
    'Wählen Sie die anzuzeigende Spalte:',
    data.columns)

num_rows = st.slider('Wählen Sie die Anzahl der anzuzeigenden Zeilen:', 1, len(data), 5)

# Anzeige der gefilterten Daten
st.write(f"### Anzeigen der ersten {num_rows} Zeilen der Spalte '{option}':")
st.write(data[[option]].head(num_rows))

# Erstellung eines Diagramms basierend auf Benutzereingabe
if st.checkbox('Diagramm anzeigen'):
    st.write(f"### Diagramm der Spalte '{option}':")
    st.line_chart(data[[option]].head(num_rows))
