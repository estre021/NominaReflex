import reflex as rx

class State(rx.State):
    sueldo_bruto: float = 0.0
    aplica_bonificacion: str = "No"
    anios_en_empresa: int = 0

    afp: float = 0.0
    sfs: float = 0.0
    ir: float = 0.0
    excedente: float = 0.0
    bonificacion: float = 0.0
    total: float = 0.0

    def set_sueldo_bruto(self, value: str):
        try:
            self.sueldo_bruto = float(value)
        except ValueError:
            self.sueldo_bruto = 0.0

    def set_aplica_bonificacion(self, value: str):
        self.aplica_bonificacion = value

    def set_anios_en_empresa(self, value: str):
        try:
            self.anios_en_empresa = int(value)
        except ValueError:
            self.anios_en_empresa = 0

    def calcular_nomina(self):
        self.afp = self.sueldo_bruto * 0.0287
        self.sfs = self.sueldo_bruto * 0.0304
        ingreso_mensual = self.sueldo_bruto
        ingreso_para_isr = ingreso_mensual - self.afp - self.sfs
        self.excedente = 0
        self.ir = 0

      
        if ingreso_para_isr <= 34685:
            self.ir = 0
            self.excedente = 0
        elif ingreso_para_isr <= 52027.41:
            self.excedente = ingreso_para_isr - 34685
            self.ir = self.excedente * 0.15
        elif ingreso_para_isr <= 72260.25:
            self.excedente = ingreso_para_isr - 52027.41
            self.ir = 2600.42 + self.excedente * 0.20
        else:
            self.excedente = ingreso_para_isr - 72260.25
            self.ir = 6647.91 + self.excedente * 0.25

     
        self.bonificacion = 0
        if self.aplica_bonificacion == "Sí":
            if self.anios_en_empresa >= 5:
                self.bonificacion = ingreso_mensual * 0.10
            elif self.anios_en_empresa >= 3:
                self.bonificacion = ingreso_mensual * 0.05
            else:
                self.bonificacion = ingreso_mensual * 0.02


        self.total = ingreso_mensual - self.afp - self.sfs - self.ir + self.bonificacion
