import reflex as rx
from .state import State

def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Calculadora de Nómina", size="8"),

            rx.text("Ingresa tu sueldo bruto mensual:"),
            rx.input(
                placeholder="RD$",
                type_="number",
                on_blur=State.set_sueldo_bruto
            ),

            rx.text("¿Cumple años laborales en la empresa este año?"),
            rx.radio(
                items=["Sí", "No"],
                on_change=State.set_aplica_bonificacion,
            ),

            rx.cond(
                State.aplica_bonificacion == "Sí",
                rx.vstack(
                    rx.text("¿Cuántos años tienes en la empresa?"),
                    rx.input(
                        placeholder="Años",
                        type_="number",
                        on_blur=State.set_anios_en_empresa
                    ),
                )
            ),

            # ✅ Botón corregido con navegación al resultado
            rx.button(
                "Calcular",
                on_click=[
                    State.calcular_nomina,
                    rx.redirect("/resultado")
                ]
            ),

            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )

def resultado() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Resultado de Nómina", size="8"),

            rx.text(f"Sueldo Bruto: RD$ {State.sueldo_bruto:,.2f}"),
            rx.text(f"¿Aplica Bonificación?: {State.aplica_bonificacion}"),

            rx.cond(
                State.aplica_bonificacion == "Sí",
                rx.text(f"Bonificación: RD$ {State.bonificacion:,.2f}")
            ),

            rx.text(f"AFP: RD$ {State.afp:,.2f}"),
            rx.text(f"SFS: RD$ {State.sfs:,.2f}"),
            rx.text(f"ISR: RD$ {State.ir:,.2f}"),
            rx.text(f"Excedente Gravado ISR: RD$ {State.excedente:,.2f}"),
            rx.text(f"Sueldo Neto: RD$ {State.total:,.2f}"),

            rx.link("← Volver al inicio", href="/"),
            spacing="5",
            justify="center",
            min_height="85vh",
        )
    )

app = rx.App()
app.add_page(index, route="/")
app.add_page(resultado, route="/resultado")
