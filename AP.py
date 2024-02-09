
import streamlit as st
import pandas as pd
import plotly.express as px


def dashboard_one():
    st.title("Groupwise Analysis")
    data = pd.read_excel(r"C:\Users\divya\Desktop\Streamlit_app\Element_properties_final_1.xlsx", sheet_name= 'Groupwise_elements', index_col=0)
    data['atomic_number'] = pd.to_numeric(data['atomic_number'], errors='coerce')

#replacement_values = {'atomic_number': '56-70', 'atomic_number': '89-102'}
#data['atomic_number'] = data['atomic_number'].fillna(replacement_values['atomic_number'])

    replacement_values = {'56-70': (56, 70), '89-102': (89, 102)}

# Replace NaN values in 'atomic_number' column with specified ranges
    data['atomic_number'] = data['atomic_number'].fillna(data['atomic_number'].apply(lambda x: next((k for k, v in replacement_values.items() if v[0] <= x <= v[1]), x)))

#st.sidebar.slider('Group_num', 1, 18)
#selected_option = st.sidebar.selectbox("Group_num", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])

    data_sorted = data.sort_values(by='atomic_number')

    selected_group = st.selectbox('Select Group Number', data['group_id'].unique())

# Filter DataFrame based on selected group_id
    filtered_data = data[data['group_id'] == selected_group]

# Handle click event on the bar plot
    selected_bar = st.selectbox('Select element for trend reasoning:', filtered_data['name'])

# Show text container with hover information above the bar graph
    hover_data_above = st.empty()

# Show text container with hover information below the group ID dropdown
    hover_data_below = st.empty()

# Display the analysis text above the bar graph
    selected_analysis = filtered_data[filtered_data['name'] == selected_bar]['Analysis'].values
    hover_data_above.markdown(
    f"### Trend Analysis:\n{selected_analysis[0] if len(selected_analysis) > 0 else 'N/A'}")

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

# Display the group ID dropdown
    st.markdown(f"### Group Number: {selected_group}")

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

    color_map = dict(zip(data['name'], data['jmol_color']))

# Bar plot based on the filtered data
    fig = px.bar(
    filtered_data, x='name', y='Atomic Radius',
    title=f'Atomic Radius Trend for Group {selected_group}', 
    hover_data=['electronic_configuration', 'VanderWaal_Radius', 'Covalent_Radius', 'Metallic_Radius'],
    color='name',
    color_discrete_map=color_map
    )
    fig.update_traces(textposition='outside')



# Display the bar plot
    st.plotly_chart(fig, use_container_width=True)


def dashboard_two():
    st.title("Periodwise Analysis")
    data = pd.read_excel(r"C:\Users\divya\Desktop\Streamlit_app\Element_properties_final_1.xlsx", sheet_name= 'Periodwise_elements', index_col=0)
    data['atomic_number'] = pd.to_numeric(data['atomic_number'], errors='coerce')

#replacement_values = {'atomic_number': '56-70', 'atomic_number': '89-102'}
#data['atomic_number'] = data['atomic_number'].fillna(replacement_values['atomic_number'])

    replacement_values = {'21-30': (21, 30),'39-48': (39, 48), '57-71': (56, 70), '72-80': (72, 80), '89-102': (89, 102), '104-112': (104, 112)}

# Replace NaN values in 'atomic_number' column with specified ranges
    data['atomic_number'] = data['atomic_number'].fillna(data['atomic_number'].apply(lambda x: next((k for k, v in replacement_values.items() if v[0] <= x <= v[1]), x)))

#st.sidebar.slider('Group_num', 1, 18)
#selected_option = st.sidebar.selectbox("Group_num", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])

    data_sorted = data.sort_values(by='atomic_number')

    selected_group = st.selectbox('Select Period Number', data['period'].unique())

# Filter DataFrame based on selected group_id
    filtered_data = data[data['period'] == selected_group]

# Handle click event on the bar plot
    selected_bar = st.selectbox('Select element for trend reasoning:', filtered_data['name'])

# Show text container with hover information above the bar graph
    hover_data_above = st.empty()

# Show text container with hover information below the group ID dropdown
   # hover_data_below = st.empty()

# Display the analysis text above the bar graph
    selected_analysis = filtered_data[filtered_data['name'] == selected_bar]['Analysis'].values
    hover_data_above.markdown(
    f"### Trend Analysis:\n{selected_analysis[0] if len(selected_analysis) > 0 else 'N/A'}")

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

# Display the group ID dropdown
    st.markdown(f"### Period Number: {selected_group}")

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

    color_map = dict(zip(data['name'], data['jmol_color']))

# Bar plot based on the filtered data
    fig = px.bar(
    filtered_data, x='name', y='Atomic Radius',
    title=f'Atomic Radius Trend for Group {selected_group}', 
    hover_data=['electronic_configuration', 'VanderWaal_Radius', 'Covalent_Radius', 'Metallic_Radius'],
    color='name',
    color_discrete_map=color_map
    )
    fig.update_traces(textposition='outside')



# Display the bar plot
    st.plotly_chart(fig, use_container_width=True)



def dashboard_three():
    st.title("Transition Metals Analysis")
    # Add content for dashboard three

    data = pd.read_excel(r"C:\Users\divya\Desktop\Streamlit_app\Element_properties_final_1.xlsx", sheet_name= 'Transition_metals', index_col=0)
    data['atomic_number'] = pd.to_numeric(data['atomic_number'], errors='coerce')

#replacement_values = {'atomic_number': '56-70', 'atomic_number': '89-102'}
#data['atomic_number'] = data['atomic_number'].fillna(replacement_values['atomic_number'])

    #replacement_values = {'21-30': (21, 30),'39-48': (39, 48), '57-71': (56, 70), '72-80': (72, 80), '89-102': (89, 102), '104-112': (104, 112)}

# Replace NaN values in 'atomic_number' column with specified ranges
    #data['atomic_number'] = data['atomic_number'].fillna(data['atomic_number'].apply(lambda x: next((k for k, v in replacement_values.items() if v[0] <= x <= v[1]), x)))

#st.sidebar.slider('Group_num', 1, 18)
#selected_option = st.sidebar.selectbox("Group_num", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])

    data_sorted = data.sort_values(by='atomic_number')

    selected_group = st.selectbox('Select Series Number', data['series'].unique())

# Filter DataFrame based on selected group_id
    filtered_data = data[data['series'] == selected_group]

# Handle click event on the bar plot
    selected_bar = st.selectbox('Select element for trend reasoning:', filtered_data['name'])

# Show text container with hover information above the bar graph
    hover_data_above = st.empty()

# Show text container with hover information below the group ID dropdown
   # hover_data_below = st.empty()

# Display the analysis text above the bar graph
    selected_analysis = filtered_data[filtered_data['name'] == selected_bar]['Analysis'].values
    hover_data_above.markdown(
    f"### Trend Analysis:\n{selected_analysis[0] if len(selected_analysis) > 0 else 'N/A'}")

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

# Display the group ID dropdown
    st.markdown(f"### Series Number: {selected_group}")

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

    color_map = dict(zip(data['name'], data['jmol_color']))

# Bar plot based on the filtered data
    fig = px.bar(
    filtered_data, x='name', y='Atomic Radius',
    title=f'Atomic Radius Trend for Group {selected_group}', 
    hover_data=['electronic_configuration', 'VanderWaal_Radius', 'Covalent_Radius', 'Metallic_Radius'],
    color='name',
    color_discrete_map=color_map
    )
    fig.update_traces(textposition='outside')



# Display the bar plot
    st.plotly_chart(fig, use_container_width=True)

def dashboard_four():
    st.title("Lanthanides and Actinides Analysis")
    # Add content for dashboard three

    data = pd.read_excel(r"C:\Users\divya\Desktop\Streamlit_app\Element_properties_final_1.xlsx", sheet_name= 'f_block_elements', index_col=0)
    data['atomic_number'] = pd.to_numeric(data['atomic_number'], errors='coerce')

#replacement_values = {'atomic_number': '56-70', 'atomic_number': '89-102'}
#data['atomic_number'] = data['atomic_number'].fillna(replacement_values['atomic_number'])

    #replacement_values = {'21-30': (21, 30),'39-48': (39, 48), '57-71': (56, 70), '72-80': (72, 80), '89-102': (89, 102), '104-112': (104, 112)}

# Replace NaN values in 'atomic_number' column with specified ranges
    #data['atomic_number'] = data['atomic_number'].fillna(data['atomic_number'].apply(lambda x: next((k for k, v in replacement_values.items() if v[0] <= x <= v[1]), x)))

#st.sidebar.slider('Group_num', 1, 18)
#selected_option = st.sidebar.selectbox("Group_num", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])

    data_sorted = data.sort_values(by='atomic_number')

    selected_group = st.selectbox('Select Lanthanide or Actinide', data['Lanthanide and Actinide'].unique())

# Filter DataFrame based on selected group_id
    filtered_data = data[data['Lanthanide and Actinide'] == selected_group]

# Handle click event on the bar plot
    selected_bar = st.selectbox('Select element for trend reasoning:', filtered_data['name'])

# Show text container with hover information above the bar graph
    hover_data_above = st.empty()

# Show text container with hover information below the group ID dropdown
   # hover_data_below = st.empty()

# Display the analysis text above the bar graph
    selected_analysis = filtered_data[filtered_data['name'] == selected_bar]['Analysis'].values
    hover_data_above.markdown(
    f"### Trend Analysis:\n{selected_analysis[0] if len(selected_analysis) > 0 else 'N/A'}")

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

# Display the group ID dropdown
    st.markdown(f"### Lanthanide or Actinide: {selected_group}")

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

    color_map = dict(zip(data['name'], data['jmol_color']))

# Bar plot based on the filtered data
    fig = px.bar(
    filtered_data, x='name', y='Atomic Radius',
    title=f'Atomic Radius Trend for Group {selected_group}', 
    hover_data=['electronic_configuration', 'VanderWaal_Radius', 'Covalent_Radius', 'Metallic_Radius'],
    color='name',
    color_discrete_map=color_map
    )
    fig.update_traces(textposition='outside')



# Display the bar plot
    st.plotly_chart(fig, use_container_width=True)


# Create sidebar navigation to switch between dashboards
page = st.sidebar.selectbox("Select a dashboard", ["Groupwise Analysis", "Periodwise Analysis", "Transition Metals Analysis", "Lanthanides and Actinides Analysis"])

# Display selected dashboard based on user choice
if page == "Groupwise Analysis":
    dashboard_one()
elif page == "Periodwise Analysis":
    dashboard_two()
elif page == "Transition Metals Analysis":
    dashboard_three()
elif page == "Lanthanides and Actinides Analysis":
    dashboard_four()
