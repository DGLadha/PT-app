import streamlit as st, pandas as pd, numpy as np
import plotly.express as px
st.header('Atomic Radius Trend')


data = pd.read_excel(r"C:\Users\divya\Desktop\Streamlit_app\Element_properties_final_1.xlsx", sheet_name= 'Groupwise_elements', index_col=0)
data['atomic_number'] = pd.to_numeric(data['atomic_number'], errors='coerce')

#replacement_values = {'atomic_number': '56-70', 'atomic_number': '89-102'}
#data['atomic_number'] = data['atomic_number'].fillna(replacement_values['atomic_number'])

replacement_values = {'56-70': (56, 70), '89-102': (89, 102)}

# Replace NaN values in 'atomic_number' column with specified ranges
data['atomic_number'] = data['atomic_number'].fillna(data['atomic_number'].apply(lambda x: next((k for k, v in replacement_values.items() if v[0] <= x <= v[1]), x)))


data_sorted = data.sort_values(by='atomic_number')


selected_group = st.selectbox('Select Group Number', data['group_id'].unique())

# Filter DataFrame based on selected group_id
filtered_data = data[data['group_id'] == selected_group]

# Handle click event on the bar plot
selected_bar = st.selectbox('Select element for trend reasoning:', filtered_data['name'])

# Show text container with hover information
hover_data = st.empty()

st.markdown(
    """
    <style>
    div[data-baseweb="select"] > div:first-child {
        width: 200px !important; /* Adjust the width as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the analysis text for the selected bar
selected_analysis = filtered_data[filtered_data['name'] == selected_bar]['Analysis'].values
hover_data.markdown(
    f"### Trend Analysis:\n{selected_analysis[0] if len(selected_analysis) > 0 else 'N/A'}"
)

# Adjust the width of the text container
st.markdown(
    """
    <style>
    .reportview-container .main .block-container {
        max-width: 1000px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Bar plot based on the filtered data
fig = px.bar(filtered_data, x='name', y='Atomic Radius',
             title=f'Atomic Radius Trend for Group {selected_group}', 
             hover_data=['electronic_configuration', 'VanderWaal_Radius', 'Covalent_Radius', 'Metallic_Radius'])
fig.update_traces(textposition='outside')

# Display the bar plot
st.plotly_chart(fig)
