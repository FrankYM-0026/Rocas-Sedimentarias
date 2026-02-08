import streamlit as st

st.title("Rocas Sedimentarias - Lista + Mini Quiz")

rocas = {
    "Detríticas": ["Conglomerado", "Brecha", "Arenisca", "Lutita", "Arcillita"],
    "Químicas": ["Caliza", "Dolomía", "Chert"],
    "Evaporitas": ["Yeso", "Halita"],
    "Orgánicas": ["Carbón"]
}

st.subheader("Lista de rocas")
for tipo, lista in rocas.items():
    st.write(f"**{tipo}**: " + ", ".join(lista))

st.subheader("Mini Quiz")

grano = st.selectbox("Tamaño de grano", ["grueso", "medio", "fino"])
clastos = st.radio("¿Ves fragmentos (clastos)?", ["si", "no"]) == "si"
organica = st.radio("¿Proviene de restos orgánicos?", ["si", "no"], index=1) == "si"
evaporita = st.radio("¿Se formó por evaporación?", ["si", "no"], index=1) == "si"

def clasificar(grano, clastos, organica, evaporita):
    if evaporita:
        return "Evaporita (Yeso / Halita)"
    if organica:
        return "Orgánica (Carbón)"
    if clastos:
        if grano == "grueso":
            return "Conglomerado o Brecha"
        if grano == "medio":
            return "Arenisca"
        if grano == "fino":
            return "Lutita o Arcillita"
    return "Química (Caliza / Dolomía)"

if st.button("Clasificar"):
    st.success("Resultado: " + clasificar(grano, clastos, organica, evaporita))

