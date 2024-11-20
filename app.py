import streamlit as st


st.text('ciao')

def somma(l1:float,l2:float):
    a =l1+l2
    return a

def main():
    st.text('Ciao questo front-end funziona')
    num1 = st.slider('Quanto è frocio bolletta da 1 a 100', 0, 100, 25)
    num2 = st.slider('Quanto è frocio ricca da 1 a 100', 0, 100, 30)
    r = somma(num1,num2)

    st.write('livello di omossesualità', r)

if __name__ == '__main__':
    main()
