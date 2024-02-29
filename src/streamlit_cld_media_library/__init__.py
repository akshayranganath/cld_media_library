from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called cld_media_library,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
	"cld_media_library", path=str(frontend_dir)
)

# Create the python function that will be called
def cld_media_library(
    key: Optional[str] = None,
    cloud_name: Optional[str] = 'demo',
    api_key: Optional[str] = '123456',
    remove_header: Optional[bool] = False,
    max_files: Optional[int] = 5,
    insert_caption: Optional[str] = 'Insert',
    button_caption: Optional[str] = 'Select Image or Video'    
) -> dict:
    """Loads Cloudinary's Media Library Widget, lets the user select one of more resources and returns the details of selected objects as a dictionary.

    Args:
        key (Optional[str], optional): Streamlit default de-duplication parameter. Defaults to None.
        cloud_name (Optional[str], optional): Specify you Cloudinary sub-account name. Defaults to 'demo'.
        api_key (Optional[str], optional): Specify the API Key for your Cloudinary sub-account. Defaults to '373364719177799'.
        remove_header (Optional[bool], optional): Do you want the Cloudinary banner on top to be removed?  Defaults to False.
        max_files (Optional[int], optional): Spcify the number of files your user can choose in the Media Library, Defaults to 5.
        insert_caption (Optional[str], optional): When a user slects an image in the widget, what should the Call to Action button say? Defaults to 'Insert'.
        button_caption (Optional[str], optional): Name of the button that launches the media library widget. Defaults to 'Select Image or Video'.

        For detailed description of each variable, please refer to Media Library Widget documentation at https://cloudinary.com/documentation/media_library_widget

    Returns:
        dict: Returns a dictionary of selected objects. The primary key is 'assets' which has a list of selected resources on Cloudinary. Each selected object has multiple attributes include public_id, secure_url, tags and so on.
    """
    component_value = _component_func(
        key=key,
        cloudName=cloud_name,
        apiKey = api_key,
        removeHeader = remove_header,
        maxFiles = max_files,
        insertCaption = insert_caption,
        buttonCaption = button_caption        
    )

    return component_value

## Built in https://blog.streamlit.io/how-to-build-your-own-streamlit-component/

def main():
    st.write("## Example")
    value = cld_media_library(remove_header=True, max_files=2)

    st.write(value)


if __name__ == "__main__":
    main()
