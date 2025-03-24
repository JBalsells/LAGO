import gradio as gr

def apply_voltage(value):
    return f"High Voltage Selected: {value:.2f}"

with gr.Blocks() as demo:
    gr.Markdown("##High Voltage Adjust")
    slider = gr.Slider(0, 2400, step=50, label="High Voltage")
    output = gr.Textbox(label="Result")
    slider.change(apply_voltage, slider, output)

demo.launch()