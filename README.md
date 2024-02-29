# streamlit_cld_media_library

Import Cloudinary's [Media Library Widget](https://cloudinary.com/documentation/media_library_widget) as a component in Streamlit application.

## Installation instructions 

```sh
pip install cld_media_library
```

## Usage instructions

```python
import streamlit as st

from streamlit_cld_media_library import cld_media_library

value = streamlit_cld_media_library(cloud_name="<<your cloudinary account name>>", api_key="<<your api key>>")

st.write(value)
```

## Detailed Usage

Media Library Widget is a method to embed Cloudinary's Digital Asset Management (DAM) capability into your application. The widget has a bunch of [configuration parameters](https://cloudinary.com/documentation/media_library_widget#2_set_the_configuration_options). For simplicity, this python module exposes the following:

| Parameter      | Purpose                                                                                                                                                            | Default Value                                |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| cloud_name     | This is your Cloudinary account name. To retrieve it, you may have to login to the Cloudinary's console and get the details from \`Programmable Media\` dashboard. | demo                                         |
| api_key        | This is part of your access credentials to Cloudinary. You can get this information from the same place as \`cloud_name\`.                                         | 123456 - this is an invalid value by design. |
| remove_header  | When the widget loads, it has the Cloudinary logo on top. You can suppress this by setting a value to \`True\`                                                     | False (i.e. display the logo)                |
| max_files      | Users can choose one or more files. Set this parameter to control the number of files that a user can select.                                                      | 5                                            |
| button_caption | ML Widget is invoked on clicking a button. This option controls the name of this button.                                                                           | "Select Image or Video"                      |
| insert_caption | When a user selects an image/video on the ML widget, a call to action button is activated. This controls the name of this call-to-action button.                   | "Insert"                                     |

The repo is published on Pypi at: [https://pypi.org/project/cld-media-library/](https://pypi.org/project/cld-media-library/).