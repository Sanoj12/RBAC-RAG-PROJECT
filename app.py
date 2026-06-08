import streamlit as st
import requests

# ---------------- CONFIG ----------------
API_URL = "http://localhost:8000"

st.set_page_config(page_title="RBAC RAG Chatbot", layout="wide")

# ---------------- SESSION ----------------
if "token" not in st.session_state:
    st.session_state.token = None



if "department" not in st.session_state:
    st.session_state.department = None


# ---------------- API FUNCTIONS ----------------
def login_user(email, password):

    response = requests.post(
        f"{API_URL}/auth/login",
        json={
            "email": email,
            "password": password
        }
    )

    if response.status_code == 200:
        return response.json()
    else:
        return {
            "error": response.text,
            "status": response.status_code
        }


def add_user(name, email, password, department):

    headers = {
        "Authorization": f"Bearer {st.session_state.token}"
    }

    response = requests.post(
        f"{API_URL}/admin/add-user",
        json={
            "name": name,
            "email": email,
            "password": password,
            
            "department": department
        },
        headers=headers
    )

    return response.json()


def ask_question(query):

    headers = {
        "Authorization": f"Bearer {st.session_state.token}"
    }

    response = requests.post(
        f"{API_URL}/rag/query",
        json={
            "query": query
        },
        headers=headers
    )

    return response.json()


# ---------------- Main----------------
st.title("RBAC RAG Chatbot")

if st.session_state.token is None:

    st.title("🔐 Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        result = login_user(email, password)

        if "token" in result:
            st.session_state.token = result["token"]
            st.session_state.department = result["department"]
            st.rerun()

        else:
            st.error("Invalid credentials")

else:

    if st.session_state.department == "admin":

        st.title("👨‍💼 Admin Dashboard")

        with st.form("add_user_form"):

            name = st.text_input("Name")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")

            department = st.selectbox(
                "Department",
                [
                    "hr team",
                    "engineering",
                    "finance",
                    "general",
                    "marketing"
                ]
            )

            submitted = st.form_submit_button("Add User")

        if submitted:

            result = add_user(
                name,
                email,
                password,
                department
            )

            if "error" in result:
                st.error(result["error"])
            else:
                st.success("User added successfully")
                st.write(result)

    else:

        st.title("🤖 RAG Chatbot")

        query = st.text_area("Ask Question")

        if st.button("Submit"):

            result = ask_question(query)
            st.write(result)