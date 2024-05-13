import matplotlib.pyplot as plt

def generate_bar_chart(labels, values, title, filename, fig_width=15, fig_height=10, font_size=12):
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    ax.bar(labels, values)
    ax.set_ylim(bottom=0)
    ax.set_title(title)
    ax.bar(labels, values, color=['#c0d88c', '#f7a472', '#f07877', '#fa2a3a', '#0a5c5a', '#680e34', '#fe4b74']) 
    #plt.show()

    ax.tick_params(axis='x', labelsize = font_size)  
    ax.tick_params(axis='y', labelsize = font_size)

    plt.savefig(f'./imgs/{filename}.png')
    plt.close()

if __name__ == '__main__':
    generate_bar_chart()
     