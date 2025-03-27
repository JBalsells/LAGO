import gradio as gr
from ssh_connector import ssh_connect
import matplotlib.pyplot as plt
import numpy as np

def apply_voltage(value):
    command = f"./lago -s hv1 {value}"
    return ssh_connect(command)

def apply_threshold(value):
    command = f"./lago -s t1 {value}"
    return ssh_connect(command)

def textbox(name, intensity):
    return ssh_connect(command)

def show_data():
    command = f"./lago -a"
    return ssh_connect(command)

def plot_function(frequency):
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(frequency * x)

    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"sin({frequency}x)")
    ax.legend()
    ax.set_title("Sine Wave")
    
    return fig  # Gradio acepta la figura de matplotlib directamente


with gr.Blocks() as demo:

    with gr.Row():
        with gr.Column():
            gr.Markdown("Threshold Adjust")
            slider1 = gr.Slider(0, 100, step=0.1, label="Threshold")
            output1 = gr.Textbox(label="Result")
            slider1.change(apply_threshold, slider1, output1)

        with gr.Column():
            gr.Markdown("High Voltage Adjust")
            slider2 = gr.Slider(0, 2400, step=50, label="High Voltage")
            output2 = gr.Textbox(label="Result")
            slider2.change(apply_voltage, slider2, output2)

    with gr.Row():
        with gr.Column():
            gr.Markdown("### Espacio para mostrar datos textuales")
            salida = gr.Textbox(label="Datos", interactive=False)

            boton = gr.Button("Mostrar Datos")
            boton.click(fn=show_data, outputs=salida)

        with gr.Column():
            plot_output = gr.Plot()
            
            slider = gr.Slider(0.1, 10, step=0.1, label="Frequency")
            slider.change(plot_function, slider, plot_output)
        
    with gr.Row():
        pass

demo.launch()