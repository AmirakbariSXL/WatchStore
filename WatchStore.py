import tkinter as tk
from tkinter import messagebox, simpledialog

class WatchStoreApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AMIR's Watch Store")
        self.root.geometry("400x400")  # Set the window size

        # Create labels and buttons
        self.label = tk.Label(self.root, text="Welcome to the AMIR's Watch Store!", font=("serif", 15))
        self.label.pack(pady=10)

        self.add_watch_button = tk.Button(self.root, text="Add Watch", command=self.add_watch)
        self.add_watch_button.pack()

        self.show_list_button = tk.Button(self.root, text="Show List", command=self.show_watch_list)
        self.show_list_button.pack()

        self.remove_watch_button = tk.Button(self.root, text="Remove Watch", command=self.remove_watch)
        self.remove_watch_button.pack()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.exit_button.pack()

        # Set background colors
        self.root.configure(bg="red")
        self.label.configure(bg="red", fg="blue")

        # Initialize watch list (you can replace this with a database or other data structure)
        self.watch_list = []

    def add_watch(self):
        # Prompt user for watch details
        brand_name = simpledialog.askstring("Add Watch", "Enter Brand Name:")
        model_number = simpledialog.askstring("Add Watch", "Enter Model Number:")
        price = simpledialog.askfloat("Add Watch", "Enter Watch Price (e.g., 100.):")

        # Add watch to the list
        if brand_name and model_number and price:
            self.watch_list.append({"brand": brand_name, "model": model_number, "price": price})
            messagebox.showinfo("Watch Details", f"Watch added successfully!\nBrand: {brand_name}\nModel: {model_number}\nPrice: ${price:.2f}")
        else:
            messagebox.showwarning("Error", "Please enter valid watch details.")

    def show_watch_list(self):
        # Display the watch list
        print("Watch List:")
        for watch in self.watch_list:
            print(f"Brand: {watch['brand']}, Model: {watch['model']}, Price: ${watch['price']:.2f}")

    def add_price(self):
        # Implement adding watch price (you can customize this part)
        pass

    def remove_watch(self):
        # Prompt user for watch details to remove
        brand_name = simpledialog.askstring("Remove Watch", "Enter Brand Name to remove:")###
        
        model_number = simpledialog.askstring("Remove Watch", "Enter Model Number to remove:")

        # Remove watch from the list
        for watch in self.watch_list:
            if watch["brand"] == brand_name and watch["model"] == model_number:
                self.watch_list.remove(watch)
                messagebox.showinfo("Watch Removed", f"Watch removed successfully!\nBrand: {brand_name}\nModel: {model_number}")
                break
        else:
            messagebox.showwarning("Error", "Watch not found in the list.")

if __name__ == "__main__":
    app = WatchStoreApp()
    app.root.mainloop()
