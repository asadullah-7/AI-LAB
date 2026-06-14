import streamlit as st
import requests
import base64
import json
import os


st.set_page_config(page_title="Free Word to PDF Converter Online.", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    .main-title { font-size: 40px; font-weight: bold; color: #FF4B4B; text-align: center; }
    .sub-title { font-size: 18px; text-align: center; color: #555555; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-title">⚡ DocuConvert Pro</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Convert Word to High-Quality PDF with Exact Formatting in Seconds!</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Drag or browse your .docx file here.", type=["docx"])

if uploaded_file is not None:
    st.info(f"📋 Selected File: {uploaded_file.name}")
    st.warning("⚡ Your file is Ready to Convert!")

    if st.button("Convert to PDF 🚀", use_container_width=True):
        with st.spinner("Processing on Cloud Server... Please wait... ☁️"):
            
            input_filename = uploaded_file.name
            output_filename = input_filename.replace(".docx", ".pdf")
            
           
            api_url = "https://v2.convertapi.com/convert/docx/to/pdf"
            
            # Secret Key 
            api_secret = "Secret Code" 
            
            params = { 'Secret': api_secret }
            files = { 'File': (input_filename, uploaded_file.getvalue(), 'application/vnd.openxmlformats-officedocument.wordprocessingml.document') }
            
            try:
                response = requests.post(api_url, params=params, files=files)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    base64_pdf_data = data['Files'][0]['FileData']
                    
                    pdf_bytes = base64.b64decode(base64_pdf_data)
                    
                    with open(output_filename, "wb") as f:
                        f.write(pdf_bytes)
                        
                    st.balloons() 
                    st.success("✨ Here we go.! Your Premium PDF is ready.")
                    
                    with open(output_filename, "rb") as pdf_file:
                        st.download_button(
                            label="📥 Download Your PDF File",
                            data=pdf_file,
                            file_name=output_filename,
                            mime="application/pdf",
                            use_container_width=True
                        )
                else:
                    st.error(f"❌ API Error (Code {response.status_code}): {response.text[:200]}")
                    
            except Exception as e:
                st.error(f"❌ System Error: {e}")
                
            finally:
                if os.path.exists(output_filename):
                    os.remove(output_filename)

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Services by Wings of Steel</p>", unsafe_allow_html=True)

adsterra_code = """
<script>
  atOptions = {
    'key' : '5a12c44d4bfbcf38fbc4fd32a966e8e6',
    'format' : 'iframe',
    'height' : 90,
    'width' : 728,
    'params' : {}
  };
</script>
<script src="https://www.highperformanceformat.com/5a12c44d4bfbcf38fbc4fd32a966e8e6/invoke.js"></script>
"""