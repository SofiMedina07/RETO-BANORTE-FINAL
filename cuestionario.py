import streamlit as st
import openai
from PIL import Image

# Configuración de OpenAI (asegúrate de tener tu propia clave API)
openai.api_key = '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'

image = Image.open("Header.jpg")
image2 = Image.open("coach.jpg")
# Mostrar la imagen
st.image(image,caption=None, width=340)
st.header(':red[FINTECH BANORTE]', divider='red')
st.subheader('***Primero vamos a conocer tu perfil***', divider='red')

tipo_inversor1 = st.radio(
    "¿Qué harías si tus inversiones perdieran un 20% de su valor en un mes?",
     ["***Vendería todas mis inversiones***", "***Vendería una parte de mis inversiones***", "***Mantendría mis inversiones y esperaría a que se recuperen***", "***Compraría más inversiones aprovechando la caída de precios***", "***No me preocuparía y seguiría como siempre***"])

if tipo_inversor1 == '***Vendería todas mis inversiones***':
    contador=0
elif tipo_inversor1 == '***Vendería una parte de mis inversiones***':
    contador=2.5
elif tipo_inversor1 == '***Mantendría mis inversiones y esperaría a que se recuperen***':
    contador=5
elif tipo_inversor1 == '***Compraría más inversiones aprovechando la caída de precios***':
    contador=7.5
elif tipo_inversor1 == '***No me preocuparía y seguiría como siempre***':
    contador=10
else:
    st.write("Por favor, selecciona una respuesta.")

tipo_inversor2 = st.radio(
    "Si tu inversión más grande perdiera un 30% de su valor en un año, ¿cómo te sentirías?",
     ["***Muy preocupado y estresado***", "***Preocupado, pero mantendría la calma***", "***Aceptablemente preocupado***", "***Preocupado, pero tomaría medidas para mitigar las pérdidas***", "***No me preocuparía demasiado***"])

if tipo_inversor2 == '***Muy preocupado y estresado***':
    contador=contador+0
elif tipo_inversor2 == '***Preocupado, pero mantendría la calma***':
    contador=2.5
elif tipo_inversor2 == '***Aceptablemente preocupado***':
    contador=contador+5
elif tipo_inversor2 == '***Preocupado, pero tomaría medidas para mitigar las pérdidas***':
    contador=contador+7.5
elif tipo_inversor2 == '***No me preocuparía demasiado***':
    contador=contador+10
else:
    st.write("Por favor, selecciona una respuesta.")

tipo_inversor3 = st.radio(
    "¿Qué porcentaje de tu patrimonio total estás dispuesto a invertir en activos de alto riesgo?",
     ["***Menos del 10%***", "***Entre el 10% y el 20%***", "***Entre el 21% y el 40%***", "***Entre el 41% y el 60%***", "***Más del 60%***"])

if tipo_inversor3 == '***Menos del 10%***':
    contador=contador+0
elif tipo_inversor3 == '***Entre el 10% y el 20%***':
    contador=contador+2.5
elif tipo_inversor3 == '***Entre el 21% y el 40%***':
    contador=contador+5
elif tipo_inversor3 == '***Entre el 41% y el 60%***':
    contador=contador+7.5
elif tipo_inversor3 == '***Más del 60%***':
    contador=contador+10
else:
    st.write("Por favor, selecciona una respuesta.")

tipo_inversor4 = st.radio(
    "Ante una inversión que promete rendimientos muy altos pero con riesgos considerables, ¿cómo reaccionarías?",
     ["***Evitaría la inversión por completo***", "***Estaría indeciso y analizaría cuidadosamente los riesgos***", "***Invertiría una pequeña cantidad para probar***", "***Invertiría una cantidad significativa***", "***Invertiría la mayoría de mi capital sin dudarlo***"])

if tipo_inversor4 == '***Evitaría la inversión por completo***':
    contador=contador+0
elif tipo_inversor4 == '***Estaría indeciso y analizaría cuidadosamente los riesgos***':
    contador=contador+2.5
elif tipo_inversor4 == '***Invertiría una pequeña cantidad para probar***':
    contador=contador+5
elif tipo_inversor4 == '***Invertiría una cantidad significativa***':
    contador=contador+7.5
elif tipo_inversor4 == '***Invertiría la mayoría de mi capital sin dudarlo***':
    contador=contador+10
else:
    st.write("Por favor, selecciona una respuesta.")

tipo_inversor5 = st.radio(
    "¿Qué plazo de inversión te resulta más atractivo?",
     ["***Corto plazo (menos de 1 año)***", "***Mediano plazo (1-5 años)***", "***Largo plazo (más de 5 años)***", "***Depende de las circunstancias***", "***No lo tengo claro***"])

if tipo_inversor5 == '***Corto plazo (menos de 1 año)***':
    contador=contador+0
elif tipo_inversor5 == '***Mediano plazo (1-5 años)***':
    contador=contador+5
elif tipo_inversor5 == '***Largo plazo (más de 5 años)***':
    contador=contador+10
elif tipo_inversor5 == '***Depende de las circunstancias***':
    contador=contador+7.5
elif tipo_inversor5 == '***No lo tengo claro***':
    contador=contador+2.5
else:
    st.write("Por favor, selecciona una respuesta.")

tipo_inversor1_1 = st.radio(
    "¿Con qué frecuencia revisas y ajustas tu cartera de inversiones?",
     ["***Mensualmente o más frecuentemente***", "***Cada trimestre***", "***Anualmente***", "***Raramente, solo cuando lo recuerdo***", "***Nunca lo hago***"])
contador1=0
if tipo_inversor1 == '***Mensualmente o más frecuentemente***':
    contador1=10
elif tipo_inversor1 == '***Cada trimestre***':
    contador1=7.5
elif tipo_inversor1 == '***Anualmente***':
    contador1=5
elif tipo_inversor1 == '***Raramente, solo cuando lo recuerdo***':
    contador1=2.5
elif tipo_inversor1 == '***Nunca lo hago***':
    contador1=0
else:
    st.write("Por favor, selecciona una respuesta.")

tipo_inversor1_2 = st.radio(
    "¿Cuánto tiempo estás dispuesto a dedicar al estudio y seguimiento de tus inversiones?",
     ["***Varias horas a la semana***", "***Alrededor de una hora a la semana***", "***Algunas horas al mes***", "***Muy poco tiempo, solo cuando es necesario***", "***No estoy dispuesto a dedicar tiempo a esto***"])

if tipo_inversor1_2 == '***Varias horas a la semana***':
    contador1=contador1+10
elif tipo_inversor1_2 == '***Alrededor de una hora a la semana***':
    contador1=7.5
elif tipo_inversor1_2== '***Algunas horas al mes***':
    contador1=contador1+5
elif tipo_inversor1_2 == '***Muy poco tiempo, solo cuando es necesario***':
    contador1=contador1+2.5
elif tipo_inversor1_2 == '***No estoy dispuesto a dedicar tiempo a esto***':
    contador1=contador1+0
else:
    st.write("Por favor, selecciona una respuesta.")

tipo_inversor1_3 = st.radio(
    "¿Prefieres delegar la gestión de tus inversiones a un asesor financiero o roboadvisor?",
     ["***Sí, prefiero que alguien más lo haga por mí***", "***Estoy abierto a la idea, pero tomo algunas decisiones por mi cuenta***", "***No tengo preferencia, depende de la situación***", "***Prefiero tomar la mayoría de las decisiones por mí mismo***", "***No confío en los asesores financieros o roboadvisors***"])

if tipo_inversor1_3 == '***Sí, prefiero que alguien más lo haga por mí***':
    contador1=contador1+0
elif tipo_inversor1_3 == '***Estoy abierto a la idea, pero tomo algunas decisiones por mi cuenta***':
    contador1=2.5
elif tipo_inversor1_3== '***No tengo preferencia, depende de la situación***':
    contador1=contador1+5
elif tipo_inversor1_3 == '***Prefiero tomar la mayoría de las decisiones por mí mismo***':
    contador1=contador1+7.5
elif tipo_inversor1_3 == '***No confío en los asesores financieros o roboadvisors***':
    contador1=contador1+10
else:
    st.write("Por favor, selecciona una respuesta.")

tipo_inversor1_4 = st.radio(
    "¿Tienes una estrategia de inversión claramente definida y la sigues de manera consistente?",
     ["***Sí, tengo una estrategia y la sigo rigurosamente***", "***Tengo una estrategia, pero a veces hago excepciones***", "***No tengo una estrategia clara***", "***Cambio mi estrategia con frecuencia***", "***Me da igual tener una estrategia***"])

if tipo_inversor1_4 == '***Sí, tengo una estrategia y la sigo rigurosamente***':
    contador1=contador1+10
elif tipo_inversor1_4 == '***Tengo una estrategia, pero a veces hago excepciones***':
    contador1=7.5
elif tipo_inversor1_4== '***No tengo una estrategia clara***':
    contador1=contador1+5
elif tipo_inversor1_4 == '***Cambio mi estrategia con frecuencia***':
    contador1=contador1+2.5
elif tipo_inversor1_4 == '***Me da igual tener una estrategia***':
    contador1=contador1+0
else:
    st.write("Por favor, selecciona una respuesta.")

tipo_inversor1_5 = st.radio(
    "¿Qué tipo de inversiones prefieres tener en tu cartera?",
     ["***Principalmente acciones individuales y activos de alto riesgo***", "***Principalmente fondos indexados y ETFs***", "***Una mezcla equilibrada de diferentes activos***", "***Principalmente bonos y activos de bajo riesgo***", "***No tengo preferencia, depende de la situación***"])

if tipo_inversor1_5 == '***Principalmente acciones individuales y activos de alto riesgo***':
    contador1=contador1+10
elif tipo_inversor1_5 == '***Principalmente fondos indexados y ETFs***':
    contador1=7.5
elif tipo_inversor1_5== '***Una mezcla equilibrada de diferentes activos***':
    contador1=contador1+5
elif tipo_inversor1_5 == '***Principalmente bonos y activos de bajo riesgo***':
    contador1=contador1+2.5
elif tipo_inversor1_5 == '***No tengo preferencia, depende de la situacióno***':
    contador1=contador1+0
else:
    st.write("Por favor, selecciona una respuesta.")


total1=contador*2
total2=contador1*2
if st.button("Enviar"):
    st.write("***Su perfil es:***")
    if total1<=33:
        if total2<=33:
            st.write("***:red[ Conservador previsor (Hormiga)]***")
            col1, col2, col3 = st.columns([1,6,1])
            with col1:
                st.write("")

            with col2:
                st.image(Image.open("3.png"),caption=None, width=200)

            with col3:
                st.write("")
            st.write(":gray[Eres un inversor que sigue una estrategia de inversión previsora y constante, similar a las hormigas que almacenan comida para el invierno. Estás enfocado en acumular de manera constante a lo largo del tiempo. Diversificas tus inversiones de manera prudente y te esfuerzas por mantener un enfoque a largo plazo. La constancia es tu virtud.]")
            
        elif 33<total2<=66:
            st.write("***:red[Conservador cauteloso (Tortuga)]***")
            col1, col2, col3 = st.columns([1,6,1])
            with col1:
                st.write("")

            with col2:
                st.image(Image.open("2.png"),caption=None, width=200)

            with col3:
                st.write("")
            st.write(":gray[Eres  un inversor meticuloso y te mueves con precaución en el mundo de las inversiones, al igual que una tortuga. Tu principal objetivo es la preservación del capital, y estás dispuesto a aceptar rendimientos más bajos a cambio de la seguridad que proporcionan inversiones de bajo riesgo. Evitas la volatilidad y te concentras en mantener un rumbo constante.]")
        else:
            st.write("***:red[ Conservador elegante (Buho)]***")
            col1, col2, col3 = st.columns([1,6,1])
            with col1:
                st.write("")

            with col2:
                st.image(Image.open("1.png"),caption=None, width=200)

            with col3:
                st.write("")
            st.write(":gray[Eres un inversor que valora la seguridad por encima de todo. Tu enfoque es lento y constante, similar al vuelo silencioso de un búho en la noche. Buscas inversiones que minimicen los riesgos y estás dispuesto a ser paciente para lograrlo. Aprovechas tu sabiduría y observación para tomar decisiones financieras cuidadosas.]")

    elif 33<total1<=66:
        if total2<=33:
            st.write("***:red[ Moderado equilibrado (León)]***")
            col1, col2, col3 = st.columns([1,6,1])
            with col1:
                st.write("")

            with col2:
                st.image(Image.open("6.png"),caption=None, width=200)

            with col3:
                st.write("")
            st.write(":gray[Al igual que el león, eres el rey de la selva financiera, buscando un equilibrio entre la seguridad y el crecimiento. Diversificas tus inversiones de manera estratégica y sigues una estrategia equilibrada. Eres fuerte y capaz de tomar decisiones cuando sea necesario, pero también mantienes un enfoque a largo plazo.]")

        elif 33<total2<=66:
            st.write("***:red[ Moderado pasivo (Koala)]***")
            col1, col2, col3 = st.columns([1,6,1])
            with col1:
                st.write("")

            with col2:
                st.image(Image.open("5.png"),caption=None, width=200)

            with col3:
                st.write("")
            st.write(":gray[Eres un inversor que adopta una estrategia de inversión tranquila y relajada, similar al comportamiento de un koala en su eucalipto. A través de inversiones pasivas como fondos indexados, buscas replicar el rendimiento del mercado sin un enfoque constante en la toma de decisiones activas. Disfrutas de un enfoque más relajado hacia las finanzas.]")
        else:
            st.write("***:red[ Moderado perspicaz (Zorro)]***")
            col1, col2, col3 = st.columns([1,6,1])
            with col1:
                st.write("")

            with col2:
                st.image(Image.open("4.png"),caption=None, width=200)

            with col3:
                st.write("")
            st.write(":gray[Eres un inversor astuto y adaptable, al igual que un zorro. Buscas un equilibrio entre riesgo y crecimiento, y estás dispuesto a tomar decisiones informadas en función de las condiciones cambiantes del mercado. Tu agudeza te permite identificar oportunidades y gestionar tus inversiones de manera activa.]")
    else:
        if total2<=33:
            st.write("***:red[ Agresivo audaz (Tiburón)]***")
            col1, col2, col3 = st.columns([1,6,1])
            with col1:
                st.write("")

            with col2:
                st.image(Image.open("9.png"),caption=None, width=200)

            with col3:
                st.write("")
            st.write(":gray[Eres un inversor intrépido y rápido, similar a un guepardo en la sabana. Buscas rendimientos significativamente superiores al promedio del mercado y no temes asumir riesgos considerables. Tu velocidad y agilidad te permiten adaptarte rápidamente a las oportunidades del mercado.]")

        elif 33<total2<=66:
            st.write("***:red[ Agresivo valiente (Águila)]***")
            col1, col2, col3 = st.columns([1,6,1])
            with col1:
                st.write("")

            with col2:
                st.image(Image.open("8.png"),caption=None, width=200)

            with col3:
                st.write("")
            st.write(":gray[Eres un inversor valiente y audaz, como un águila que se lanza en picado para capturar su presa. Aunque buscas rendimientos elevados, lo haces a través de inversiones más convencionales. Sigues una estrategia de inversión que te permite estar atento a las oportunidades, pero también te proporciona cierta seguridad.]")

        else:
            st.write("***:red[ Agresivo dinámico (Guepardo)]***")
            col1, col2, col3 = st.columns([1,6,1])
            with col1:
                st.write("")

            with col2:
                st.image(Image.open("7.png"),caption=None, width=200)

            with col3:
                st.write("")
            st.write(":gray[Eres un inversor intrépido y rápido, similar a un guepardo en la sabana. Buscas rendimientos significativamente superiores al promedio del mercado y no temes asumir riesgos considerables. Tu velocidad y agilidad te permiten adaptarte rápidamente a las oportunidades del mercado.]")

    st.link_button("***:red[Conocer más: ]***", "http://10.22.135.95:8505")
