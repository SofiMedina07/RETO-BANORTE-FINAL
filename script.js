document.addEventListener("DOMContentLoaded", function () {
    // Obtén todas las respuestas seleccionadas por el usuario
    const respuestas = document.querySelectorAll("input[type=radio]:checked");

    // Suma los valores de las respuestas seleccionadas para calcular los puntos acumulados
    let puntos = 0;
    respuestas.forEach(function (respuesta) {
        puntos += parseFloat(respuesta.value);
    });

    // Muestra los resultados en la página
    const resultadosDiv = document.getElementById("resultados");
    resultadosDiv.innerHTML = `<p>Puntos acumulados: ${puntos}</p>`;
});