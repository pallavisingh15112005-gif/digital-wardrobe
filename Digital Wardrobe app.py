import streamlit as st
import pandas as pd
import os

st.title("👗 My Digital Wardrobe with Outfit Uploads")

# Ensure image folder exists
if not os.path.exists("wardrobe_images"):
    os.makedirs("wardrobe_images")

# Initialize wardrobe
if "wardrobe" not in st.session_state:
    st.session_state.wardrobe = pd.DataFrame(columns=["Outfit Name", "Occasion", "Notes", "Image Path"])

# Upload outfit picture
uploaded_file = st.file_uploader("Upload an outfit picture", type=["jpg", "jpeg", "png"])

outfit_name = st.text_input("Outfit Name")
occasion = st.selectbox("Occasion", ["Casual", "Formal", "Party", "Work"])
notes = st.text_area("Notes about this outfit")

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Outfit", use_column_width=True)

    if st.button("Save Outfit"):
        # Save image to folder
        image_path = os.path.join("wardrobe_images", uploaded_file.name)
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Add to wardrobe DataFrame
        st.session_state.wardrobe.loc[len(st.session_state.wardrobe)] = [outfit_name, occasion, notes, image_path]
        st.success(f"Outfit '{outfit_name}' saved!")

# Show wardrobe table
st.write("### Wardrobe Items")
st.dataframe(st.session_state.wardrobe)

# Display saved outfits with images
st.write("### Outfit Gallery")
for _, row in st.session_state.wardrobe.iterrows():
    st.write(f"**{row['Outfit Name']}** ({row['Occasion']})")
    st.write(row['Notes'])
    if os.path.exists(row['Image Path']):
        st.image(row['Image Path'], width=200)