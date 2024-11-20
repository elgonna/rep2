import streamlit as st


st.text('ciao')

def somma(l1:float,l2:float):
    a =l1+l2
    return a

def main():
    st.text('Ciao questo front-end funziona')
    num1 = st.slider('1', 0, 100, 25)
    num2 = st.slider('1', 0, 100, 30)
    r = somma(num1,num2)

    st.write('2', r)

if __name__ == '__main__':
    main()
