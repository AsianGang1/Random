from tkinter import *

selected = (None, None)


def transfer(bucket):
    global selected
    if selected != (None, None):
        if bucket == 0:
            second_selected = 0, bucket1
        elif bucket == 1:
            second_selected = 1, bucket2
        else:
            second_selected = 2, bucket3
        if bucket_fills[selected[0]] + bucket_fills[second_selected[0]] > bucket_limits[second_selected[0]]:
            prev_fill = bucket_fills[second_selected[0]]
            bucket_fills[second_selected[0]] = bucket_limits[second_selected[0]]
            bucket_fills[selected[0]] = bucket_fills[selected[0]] + prev_fill - bucket_limits[
                second_selected[0]]
        else:
            bucket_fills[second_selected[0]] += bucket_fills[selected[0]]
            bucket_fills[selected[0]] = 0
        selected[1].configure(bg=orig_color,
                              text=f"Bucket {selected[0] + 1}: {bucket_fills[selected[0]]}/{bucket_limits[selected[0]]} litres")
        second_selected[1].configure(
            text=f"Bucket {second_selected[0] + 1}: {bucket_fills[second_selected[0]]} /{bucket_limits[second_selected[0]]} litres")
        selected = (None, None)
    else:
        if bucket == 0:
            selected = 0, bucket1
        elif bucket == 1:
            selected = 1, bucket2
        else:
            selected = 2, bucket3
        selected[1].configure(bg="red")


root = Tk()
root.title("Buckets")
bucket_image = PhotoImage(file=r"bucket.png")
bucket_image = bucket_image.zoom(3)
bucket_fills = [0, 5, 6]
bucket_limits = [10, 5, 6]
bucket1 = Button(text=f"Bucket 1: {bucket_fills[0]}/{bucket_limits[0]} litres", padx=10, pady=10, image=bucket_image,
                 compound=TOP,
                 command=lambda: transfer(0))
bucket2 = Button(text=f"Bucket 2: {bucket_fills[1]}/{bucket_limits[1]} litres", padx=10, pady=10, image=bucket_image,
                 compound=TOP,
                 command=lambda: transfer(1))
bucket3 = Button(text=f"Bucket 3: {bucket_fills[2]}/{bucket_limits[2]} litres", padx=10, pady=10, image=bucket_image,
                 compound=TOP,
                 command=lambda: transfer(2))

orig_color = bucket1.cget("background")
bucket1.grid(row=0, column=0, padx=10, pady=10)
bucket2.grid(row=0, column=1, padx=10, pady=10)
bucket3.grid(row=0, column=2, padx=10, pady=10)
root.mainloop()
