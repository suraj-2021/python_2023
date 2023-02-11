# Import the library 'pywhatkit' as 'pw'

import pywhatkit as pw

# Define the text that we want to convert to handwriting

txt = "Python is one of the most popular programming language in the world and is widely used in different areas like machine learning, data science, and software development"

# Use the text_to_handwriting function from pywhatkit library
# First parameter: the text that we want to convert
# Second parameter: the name of the file that we want to save the handwriting image
# Third parameter: the color code for the handwriting (in this case, [0, 0, 138] which is blue)

pw.text_to_handwriting(txt,"test_text.png",[0,0,138])

# Let's let the user know that the process has ended
print("END")

# Note: If you don't pass the second and third parameters, the default file name will be 'pywhatkit.png' and the default color code will be blue.
