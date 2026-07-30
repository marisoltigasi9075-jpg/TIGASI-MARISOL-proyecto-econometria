import "./App.css";

function App() {
  return (
    <div className="container">

      <h1>Proyecto de Econometría</h1>

      <h2>
        Relación entre el crecimiento del PIB, la inflación y el desempleo en Ecuador mediante un modelo VAR
      </h2>

      <hr />

      <section>
        <h3>Autor</h3>
        <p>Marisol Veronica Tigasi Ugsha</p>

        <h3>Universidad</h3>
        <p>Universidad Técnica de Cotopaxi</p>
      </section>

      <section>
        <h3>Pregunta de investigación</h3>

        <p>
        ¿Cómo interactúan dinámicamente el crecimiento del PIB,
        la inflación y el desempleo en Ecuador durante el período
        2007–2024?
        </p>
      </section>

      <section>
        <h3>Objetivo</h3>

        <p>
        Analizar la relación dinámica entre el crecimiento del PIB,
        la inflación y el desempleo mediante un modelo VAR.
        </p>
      </section>

      <section>
        <h3>Fuente de datos</h3>

        <p>
        Banco Mundial (World Development Indicators).
        Datos anuales de Ecuador correspondientes al período
        2007–2024.
        </p>
      </section>

      <section>
        <h3>Variables utilizadas</h3>

        <ul>
          <li>Crecimiento del PIB (%)</li>
          <li>Inflación (%)</li>
          <li>Desempleo (%)</li>
        </ul>
      </section>

      <section>
        <h3>Modelo Econométrico</h3>

        <p>
        Se estimó un modelo VAR(1), luego de aplicar pruebas
        de estacionariedad (ADF) y seleccionar el número óptimo
        de rezagos mediante AIC y BIC.
        </p>
      </section>
<h2>Modelo econométrico</h2>

<p>
Se estimó un modelo VAR (Vectores Autorregresivos), el cual permite analizar
la relación dinámica entre el crecimiento del PIB, la inflación y el desempleo.
Antes de la estimación se verificó la estacionariedad de las series mediante la
prueba Dickey-Fuller Aumentada (ADF), seleccionándose finalmente un modelo VAR(1).
</p>

<h2>Principales resultados</h2>

<ul>
  <li>El desempleo ayuda a predecir el crecimiento del PIB.</li>
  <li>El crecimiento del PIB ayuda a explicar la inflación.</li>
  <li>El modelo VAR(1) fue el que presentó el mejor ajuste.</li>
  <li>No se encontraron problemas importantes en los diagnósticos del modelo.</li>
</ul>

<h2>Conclusiones</h2>

<p>
Los resultados muestran que el crecimiento del PIB, la inflación y el desempleo
mantienen una relación dinámica durante el período analizado. Aunque cada
variable explica principalmente su propio comportamiento, también existen
interacciones que permiten comprender mejor la evolución de la economía
ecuatoriana.
</p>
    </div>
    
  );
  
}
export default App;

