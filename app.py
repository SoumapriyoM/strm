import streamlit as st

def find_largest(a, b, c):
    return max(a, b, c)

def main():
    st.title("Largest Number Finder")
    
    st.write("Enter three numbers:")
    a = st.number_input("Number 1", value=0)
    b = st.number_input("Number 2", value=0)
    c = st.number_input("Number 3", value=0)
    
    if st.button("Find Largest"):
        largest = find_largest(a, b, c)
        st.success(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
