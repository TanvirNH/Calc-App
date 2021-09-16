"""
-------------------------------------
File:    Calc_App_Code.py
Project: Calc_App
A calculator application which is able to solve basic arithmetic operations.
-------------------------------------
Version  2021-09-17
-------------------------------------
"""
import tkinter as gui
# Font colour specified below
C_1 = "#a8b3b8"
C_2 = "#9c9c9c"
C_3 = "#b3b1bf"
C_4 = "#c0c8d1"
C_5 = "#ea131b"
# Font names and size specified below
Font_1 = ("Open Sans", 50)
Font_2 = ("Open Sans", 20)
Font_3 = ("Open Sans", 35)
Font_4 = ("Open Sans", 30)


class Calc_App:
    def __init__(self):
        self.window = gui.Tk()
        self.window.title("Calc App")
        self.window.resizable(1, 1)
        self.window.geometry("400x700")
        self.Y = ""
        self.X = ""
        self.F = self.Make_F()
        self.total_label, self.label = self.Make_D_L()
        self.D = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.B_FM = self.Make_F_B()
        self.B_FM.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.B_FM.rowconfigure(x, weight=1)
            self.B_FM.columnconfigure(x, weight=1)
        self.male_var_buttons()
        self.make_D_B()
        self.make_S_Character_B()
        self.b_k()

    def b_k(self):
        self.window.bind("<Return>", lambda event: self.solve())
        for key in self.D:
            self.window.bind(str(key), lambda event,
                             digit=key: self.A_Operation(digit))

        for key in self.operations:
            self.window.bind(key, lambda event,
                             variable=key: self.app_var(variable))

    def make_S_Character_B(self):
        self.Make_c_b()
        self.make_eql_b()
        self.Make_sqr_B()
        self.Make_sqr_root_b()

    def Make_D_L(self):
        total_label = gui.Label(self.F, text=self.X, anchor=gui.E, bg=C_4,
                                fg=C_5, padx=24, font=Font_2)
        total_label.pack(expand=True, fill='both')

        label = gui.Label(self.F, text=self.Y, anchor=gui.E, bg=C_4,
                          fg=C_5, padx=24, font=Font_1)
        label.pack(expand=True, fill='both')

        return total_label, label

    def Make_F(self):
        frame = gui.Frame(self.window, height=221, bg=C_4)
        frame.pack(expand=True, fill="both")
        return frame

    def A_Operation(self, value):
        self.Y += str(value)
        self.L_Up()

    def make_D_B(self):
        for digit, g_val in self.D.items():
            button = gui.Button(self.B_FM, text=str(digit), bg=C_2, fg=C_5, font=Font_3,
                                borderwidth=0, command=lambda x=digit: self.A_Operation(x))
            button.grid(row=g_val[0],
                        column=g_val[1], sticky=gui.NSEW)

    def app_var(self, variable):
        self.Y += variable
        self.X += self.Y
        self.Y = ""
        self.L_T_Up()
        self.L_Up()

    def male_var_buttons(self):
        i = 0
        for variable, symbol in self.operations.items():
            button = gui.Button(self.B_FM, text=symbol, bg=C_1, fg=C_5, font=Font_4,
                                borderwidth=0, command=lambda x=variable: self.app_var(x))
            button.grid(row=i, column=4, sticky=gui.NSEW)
            i += 1

    def c(self):
        self.Y = ""
        self.X = ""
        self.L_Up()
        self.L_T_Up()

    def Make_c_b(self):
        button = gui.Button(self.B_FM, text="C", bg=C_1, fg=C_5, font=Font_4,
                            borderwidth=0, command=self.c)
        button.grid(row=0, column=1, sticky=gui.NSEW)

    def sqr(self):
        self.Y = str(eval(f"{self.Y}**2"))
        self.L_Up()

    def Make_sqr_B(self):
        button = gui.Button(self.B_FM, text="x\u00b2", bg=C_1, fg=C_5, font=Font_4,
                            borderwidth=0, command=self.sqr)
        button.grid(row=0, column=2, sticky=gui.NSEW)

    def sqr_root(self):
        self.Y = str(eval(f"{self.Y}**0.5"))
        self.L_Up()

    def Make_sqr_root_b(self):
        button = gui.Button(self.B_FM, text="\u221ax", bg=C_1, fg=C_5, font=Font_4,
                            borderwidth=0, command=self.sqr_root)
        button.grid(row=0, column=3, sticky=gui.NSEW)

    def solve(self):
        self.X += self.Y
        self.L_T_Up()
        try:
            self.Y = str(eval(self.X))

            self.X = ""
        except Exception as e:
            self.Y = "INVALID, Please enter again"
        finally:
            self.L_Up()

    def make_eql_b(self):
        button = gui.Button(self.B_FM, text="=", bg=C_3, fg=C_5, font=Font_4,
                            borderwidth=0, command=self.solve)
        button.grid(row=4, column=3, columnspan=2, sticky=gui.NSEW)

    def Make_F_B(self):
        frame = gui.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def L_T_Up(self):
        operation = self.X
        for variable, symbol in self.operations.items():
            operation = operation.replace(variable, f' {symbol} ')
        self.total_label.config(text=operation)

    def L_Up(self):
        self.label.config(text=self.Y[:11])

    def start(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calc_App()
    calc.start()
