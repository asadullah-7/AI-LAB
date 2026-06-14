import streamlit as st
import requests

# 1. Page ki configuration aur Title
st.set_page_config(page_title="Realtime Currency Converter", page_icon="💱")
st.title("💱 Realtime Currency Converter")
st.write("Live exchange rates ke sath apni currency convert karein. \nMade by Asad Ullah")

# 2. Free API ka URL (Yeh bina kisi key ke base rates deta hai)
# Hum default base USD rakh rahe hain
API_URL = "https://open.er-api.com/v6/latest/USD"

# 3. API se realtime data fetch karna
@st.cache_data(ttl=3600) # Yeh data ko 1 ghante tak cache rakhega taake baar baar API load na ho
def fetch_currency_rates():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json().get("rates", {})
        else:
            st.error("API se data nahi mil saka. Dobara koshish karein.")
            return {}
    except Exception as e:
        st.error(f"Network error: {e}")
        return {}

rates = fetch_currency_rates()

if rates:
    # Saari available currencies ki list nikalna
    currencies = sorted(list(rates.keys()))

    # 4. User Input ke liye UI Components
    col1, col2, col3 = st.columns(3)

    with col1:
        amount = st.number_input("Amount", min_value=0.0, value=1.0, step=1.0)

    with col2:
        # Default USD select hoga
        from_currency = st.selectbox("From", currencies, index=currencies.index("USD"))

    with col3:
        # Default PKR select hoga (agar list mein hai, warna pehla)
        default_to_idx = currencies.index("PKR") if "PKR" in currencies else 0
        to_currency = st.selectbox("To", currencies, index=default_to_idx)

    # 5. Conversion Logic
    # Pehle input amount ko USD mein convert karte hain (kyunke hamara base USD hai)
    amount_in_usd = amount / rates[from_currency]
    # Phir USD se target currency mein convert karte hain
    converted_amount = amount_in_usd * rates[to_currency]

    # 6. Result Dikhana
    st.markdown("---")
    st.metric(
        label=f"Converted Amount ({to_currency})", 
        value=f"{converted_amount:,.2f} {to_currency}"
    )
    st.info(f"1 {from_currency} = {(rates[to_currency]/rates[from_currency]):.4f} {to_currency}")
else:
    st.warning("Rates Can't load, NO INTERNET!!!.")