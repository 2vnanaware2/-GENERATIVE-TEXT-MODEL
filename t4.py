#step 1
from transformers import pipeline, set_seed
import ipywidgets as widgets
from IPython.display import display

# Set random seed for consistent output
set_seed(42)

# Load the pre-trained GPT-2 model
text_generator = pipeline("text-generation", model="gpt2")


#step 2
# Input prompt text box
prompt_input = widgets.Text(
    value='The future of artificial intelligence',
    placeholder='Type a topic or prompt here...',
    description='Prompt:',
    disabled=False,
    layout=widgets.Layout(width='80%')
)

# Generate button and output area
generate_button = widgets.Button(description="Generate Text")
output_area = widgets.Output()


#step3
# Text generation function
def generate_text(prompt):
    result = text_generator(prompt, max_length=150, num_return_sequences=1)
    return result[0]['generated_text']



#step 4
# Button click event
def on_generate_clicked(b):
    with output_area:
        output_area.clear_output()
        generated = generate_text(prompt_input.value)
        print("📝 Generated Paragraph:\n")
        print(generated)

generate_button.on_click(on_generate_clicked)

#step 5
# Display the input, button, and output
display(prompt_input, generate_button, output_area)



