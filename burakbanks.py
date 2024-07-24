import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class BankMobileApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Bank Mobil Uygulaması")
        self.master.configure(bg='#cccccc')
        self.master.attributes('-fullscreen', False)

        self.title_label = tk.Label(self.master, text="Bankamatik Uygulaması", bg='#cccccc', font=('Arial', 30, 'bold'))
        self.title_label.pack(expand=True, fill='both', pady=10)

        self.menu_frame = tk.Frame(self.master, bg='#cccccc')
        self.menu_frame.pack(expand=True, fill='both')

        self.transfer_frame = tk.Frame(self.master, bg='#cccccc')
        self.eft_frame = tk.Frame(self.master, bg='#cccccc')
        self.havale_frame = tk.Frame(self.master, bg='#cccccc')
        self.multi_transfer_frame = tk.Frame(self.master, bg='#cccccc')
        self.group_transfer_frame = tk.Frame(self.master, bg='#cccccc')


        self.login_frame = tk.Frame(self.master, bg='#cccccc')

        self.id_label = tk.Label(self.login_frame, text="Kimlik Numarası:", bg='#cccccc', font=('Arial', 20 , 'bold'))
        self.id_label.pack(pady=(100, 10))
        self.id_entry = tk.Entry(self.login_frame, font=('Arial', 20))
        self.id_entry.pack(pady=10)
        self.pw_label = tk.Label(self.login_frame, text="Şifre:", bg='#cccccc', font=('Arial', 20 ,'bold'))
        self.pw_label.pack(pady=10)
        self.pw_entry = tk.Entry(self.login_frame, show='*', font=('Arial', 20))
        self.pw_entry.pack(pady=10)
        self.login_btn = tk.Button(self.login_frame, text="Giriş Yap", command=self.check_credentials,
                                   font=('Arial', 20, 'bold'))
        self.login_btn.pack(pady=10)

        self.back_button = tk.Button(self.master, text="Geri Dön", command=self.show_menu,
                                     font=('Arial', 20, 'bold'))


        self.close_button = tk.Button(self.master, text="Uygulamayı Kapat", command=self.master.quit,
                                      font=('Arial', 20, 'bold'))
        self.close_button.pack(side=tk.LEFT, anchor=tk.SW, padx=10, pady=10)

        self.fullscreen_button = tk.Button(self.master, text="Tam Ekran", command=self.enter_fullscreen,
                                           font=('Arial', 20, 'bold'))
        self.fullscreen_button.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10)

        self.exit_fullscreen_button = tk.Button(self.master, text="Tam Ekrandan Çık", command=self.exit_fullscreen,
                                                font=('Arial', 20, 'bold'))
        self.fullscreen_button.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10)


        self.login_frame.pack(expand=True, fill='both')

    def enter_fullscreen(self):
        self.master.attributes('-fullscreen', True)

    def exit_fullscreen(self):
        self.master.attributes('-fullscreen', False)

    def check_credentials(self):
        kimlik_no = self.id_entry.get()
        sifre = self.pw_entry.get()

        if not kimlik_no or not sifre:
            messagebox.showerror("Hata", "Kimlik numarası veya şifre boş bırakılamaz.")
        elif not kimlik_no.isdigit() or len(kimlik_no) != 11:
            messagebox.showerror("Hata", "Kimlik numarası 11 haneli bir rakam olmalıdır.")
        elif sifre == "1234":
            messagebox.showinfo("Başarılı", "Giriş başarılı.")
            self.login_frame.pack_forget()
            self.show_menu_buttons()
        else:
            messagebox.showerror("Hata", "Kimlik numarası veya şifre yanlış.")

    def open_transfer_page(self):
        self.menu_frame.pack_forget()
        self.title_label.pack_forget()
        self.close_button.pack_forget()
        self.fullscreen_button.pack_forget()
        self.exit_fullscreen_button.pack_forget()
        self.back_button.config(command=self.show_menu)  # Update the back button command
        self.back_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        self.transfer_frame.pack(expand=True, fill='both')

        buttons = [
            ("EFT", self.eft),
            ("Havale", self.havale),
            ("Çoklu Para Transferi", self.multi_transfer),
            ("Alıcı Grubuna Para Transferleri", self.group_transfer),
        ]

        for btn_text, command in buttons:
            btn = tk.Button(self.transfer_frame, text=btn_text, command=command, font=('Arial', 20, 'bold'))
            btn.pack(expand=True, fill='both', pady=10)

    def eft(self):
        self.transfer_frame.pack_forget()
        self.back_button.config(command=self.open_transfer_page)  # Update the back button command
        self.eft_frame.pack(expand=True, fill='both', padx=100, pady=50)

        iban_label = tk.Label(self.eft_frame, text="IBAN Numarası:", bg='#cccccc', font=('Arial', 20))
        iban_label.pack(pady=10)
        self.iban_entry = tk.Entry(self.eft_frame, font=('Arial', 20))
        self.iban_entry.pack(pady=10)

        name_label = tk.Label(self.eft_frame, text="Alıcı Adı Soyadı:", bg='#cccccc', font=('Arial', 20))
        name_label.pack(pady=10)
        self.name_entry = tk.Entry(self.eft_frame, font=('Arial', 20))
        self.name_entry.pack(pady=10)

        amount_label = tk.Label(self.eft_frame, text="Miktar:", bg='#cccccc', font=('Arial', 20))
        amount_label.pack(pady=10)
        self.amount_entry = tk.Entry(self.eft_frame, font=('Arial', 20))
        self.amount_entry.pack(pady=10)

        date_label = tk.Label(self.eft_frame, text="Tarih:", bg='#cccccc', font=('Arial', 20))
        date_label.pack(pady=10)
        self.date_entry = tk.Entry(self.eft_frame, font=('Arial', 20))
        self.date_entry.pack(pady=10)

        submit_button = tk.Button(self.eft_frame, text="Gönder", command=self.submit_eft, font=('Arial', 20, 'bold'))
        submit_button.pack(pady=10)

    def submit_eft(self):
        iban = self.iban_entry.get()
        name = self.name_entry.get()
        amount = self.amount_entry.get()
        date = self.date_entry.get()

        if not iban or not name or not amount or not date:
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurunuz.")
            return

        # Burada EFT işlemi gerçekleştirilebilir, örneğin verileri bir veritabanına kaydetme veya API ile gönderme gibi

        message = f"EFT işlemi başlatıldı:\nIBAN: {iban}\nAlıcı: {name}\nMiktar: {amount}\nTarih: {date}"
        messagebox.showinfo("EFT", message)
        self.eft_frame.pack_forget()
        self.show_menu()

    def havale(self):
        self.transfer_frame.pack_forget()
        self.back_button.config(command=self.open_transfer_page)  # Update the back button command
        self.havale_frame.pack(expand=True, fill='both', padx=100, pady=50)

        iban_label = tk.Label(self.havale_frame, text="Alıcı IBAN Numarası:", bg='#cccccc', font=('Arial', 20))
        iban_label.pack(pady=10)
        self.iban_entry_havale = tk.Entry(self.havale_frame, font=('Arial', 20))
        self.iban_entry_havale.pack(pady=10)

        name_label = tk.Label(self.havale_frame, text="Alıcı Adı Soyadı:", bg='#cccccc', font=('Arial', 20))
        name_label.pack(pady=10)
        self.name_entry_havale = tk.Entry(self.havale_frame, font=('Arial', 20))
        self.name_entry_havale.pack(pady=10)

        amount_label = tk.Label(self.havale_frame, text="Miktar:", bg='#cccccc', font=('Arial', 20))
        amount_label.pack(pady=10)
        self.amount_entry_havale = tk.Entry(self.havale_frame, font=('Arial', 20))
        self.amount_entry_havale.pack(pady=10)

        date_label = tk.Label(self.havale_frame, text="Tarih:", bg='#cccccc', font=('Arial', 20))
        date_label.pack(pady=10)
        self.date_entry_havale = tk.Entry(self.havale_frame, font=('Arial', 20))
        self.date_entry_havale.pack(pady=10)

        submit_button = tk.Button(self.havale_frame, text="Gönder", command=self.submit_havale, font=('Arial', 20, 'bold'))
        submit_button.pack(pady=10)

    def submit_havale(self):
        iban = self.iban_entry_havale.get()
        name = self.name_entry_havale.get()
        amount = self.amount_entry_havale.get()
        date = self.date_entry_havale.get()

        if not iban or not name or not amount or not date:
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurunuz.")
            return


        message = f"Havale işlemi başlatıldı:\nAlıcı IBAN: {iban}\nAlıcı: {name}\nMiktar: {amount}\nTarih: {date}"
        messagebox.showinfo("Havale", message)
        self.havale_frame.pack_forget()
        self.show_menu()

    def multi_transfer(self):
        self.transfer_frame.pack_forget()
        self.back_button.config(command=self.open_transfer_page)
        self.multi_transfer_frame.pack(expand=True, fill='both', padx=100, pady=50)

    def group_transfer(self):
        self.transfer_frame.pack_forget()
        self.back_button.config(command=self.open_transfer_page)  # Update the back button command
        self.group_transfer_frame.pack(expand=True, fill='both', padx=100, pady=50)


    def open_payment_page(self):
        pass

    def open_investment_page(self):
        pass

    def open_loan_page(self):
        pass

    def open_branches_page(self):
        pass

    def open_profile_page(self):
        pass

    def open_customer_service(self):
        pass

    def open_settings_page(self):
        pass

    def show_menu_buttons(self):
        self.menu_frame.pack(expand=True, fill='both')
        self.close_button.pack(side=tk.LEFT, padx=0, pady=10)
        self.fullscreen_button.pack(side=tk.RIGHT, padx=10, pady=10)
        self.exit_fullscreen_button.pack(side=tk.TOP, padx=10, pady=10)

        buttons = [
            ("Para Transferi", self.open_transfer_page),
            ("Fatura Ödeme", self.open_payment_page),
            ("Yatırımlar", self.open_investment_page),
            ("Kredi ve Kredi Kartı İşlemleri", self.open_loan_page),
            ("Şubelerimiz", self.open_branches_page),
            ("Profil", self.open_profile_page),
            ("Müşteri Hizmetleri", self.open_customer_service),
            ("Ayarlar ve Bildirimler", self.open_settings_page),
        ]

        for btn_text, command in buttons:
            btn = tk.Button(self.menu_frame, text=btn_text, command=command, font=('Arial', 20, 'bold'))
            btn.pack(expand=True, fill='both', pady=10)

    def show_menu(self):
        self.menu_frame.pack(expand=True, fill='both')
        if not self.login_frame.winfo_ismapped():
            self.title_label.pack(expand=True, fill='both', pady=20)
        self.close_button.pack(side=tk.LEFT, padx=0, pady=10)
        self.fullscreen_button.pack(side=tk.RIGHT, padx=10, pady=10)
        self.exit_fullscreen_button.pack(side=tk.TOP, padx=10, pady=10)
        self.back_button.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = BankMobileApp(root)
    root.mainloop()
