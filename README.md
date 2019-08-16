
<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml" lang="es">
  <head>
    <meta charset="utf-8" />
    <title>Welcome to PyDBOD’s documentation! &#8212; documentación de PyDBOD - 1.0</title>
    <link rel="stylesheet" href="_static/alabaster.css" type="text/css" />
    <link rel="stylesheet" href="_static/pygments.css" type="text/css" />
    <script type="text/javascript" id="documentation_options" data-url_root="./" src="_static/documentation_options.js"></script>
    <script type="text/javascript" src="_static/jquery.js"></script>
    <script type="text/javascript" src="_static/underscore.js"></script>
    <script type="text/javascript" src="_static/doctools.js"></script>
    <script type="text/javascript" src="_static/language_data.js"></script>
    <script type="text/javascript" src="_static/translations.js"></script>
    <link rel="index" title="Índice" href="genindex.html" />
    <link rel="search" title="Búsqueda" href="search.html" />
   
  <link rel="stylesheet" href="_static/custom.css" type="text/css" />
  
  
  <meta name="viewport" content="width=device-width, initial-scale=0.9, maximum-scale=0.9" />

  </head><body>
  

    <div class="document">
      <div class="documentwrapper">
        <div class="bodywrapper">
          

          <div class="body" role="main">
            
  <div class="section" id="welcome-to-pydbod-s-documentation">
<h1>Welcome to PyDBOD’s documentation!<a class="headerlink" href="#welcome-to-pydbod-s-documentation" title="Enlazar permanentemente con este título">¶</a></h1>
<div class="toctree-wrapper compound">
</div>
</div>
<div class="section" id="introduccion">
<h1>Introduccion<a class="headerlink" href="#introduccion" title="Enlazar permanentemente con este título">¶</a></h1>
<p>Bienvenido a PyDBOD, la biblioteca de Python para la detección de anomalías usando
algoritmos basados en distancias. En esta bibliotica tienes una amplia selección de
algoritmos los cuales vamos a documentar a continuación. El uso de todos se reduce a
la creación de un objeto de la clase respectiva y el uso del método <strong>fit_predict</strong>.</p>
</div>
<div class="section" id="lof">
<h1>LOF<a class="headerlink" href="#lof" title="Enlazar permanentemente con este título">¶</a></h1>
<p>Local Outlier Factor (LOF), o en español factor de valor atı́pico local, es
una cuantificación del valor atı́pico de un punto perteneciente al conjunto de
datos. Esta cuantificación es capaz de ajustar las variaciones en las densidades
locales.</p>
<dl class="function">
<dt id="LOF">
<code class="descname">LOF</code><span class="sig-paren">(</span><em>k = 20</em><span class="sig-paren">)</span><a class="headerlink" href="#LOF" title="Enlazar permanentemente con esta definición">¶</a></dt>
<dd><p>Constructor para la creación del objeto de la clase LOF.</p>
<dl class="field-list simple">
<dt class="field-odd">Parámetros</dt>
<dd class="field-odd"><p><strong>int</strong> – k, número de k vecinos a calcular</p>
</dd>
<dt class="field-even">Tipo del valor devuelto</dt>
<dd class="field-even"><p>objeto de la clase LOF</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="fit_predict">
<code class="descname">fit_predict</code><span class="sig-paren">(</span><em>data</em><span class="sig-paren">)</span><a class="headerlink" href="#fit_predict" title="Enlazar permanentemente con esta definición">¶</a></dt>
<dd><p>Método para aplicar el algoritmo LOF a una matriz de datos.</p>
<dl class="field-list simple">
<dt class="field-odd">Parámetros</dt>
<dd class="field-odd"><p><strong>numpy.array</strong> – data, matriz de datos</p>
</dd>
<dt class="field-even">Tipo del valor devuelto</dt>
<dd class="field-even"><p>numpy.array de puntuaciones de anomalía</p>
</dd>
</dl>
</dd></dl>

</div>
<div class="section" id="loop">
<h1>LOOP<a class="headerlink" href="#loop" title="Enlazar permanentemente con este título">¶</a></h1>
<p>Local Outlier Probability (LoOP), esta técnica combina varios conceptos.
En primer lugar, la idea de localidad, los algoritmos basados en densidad
como LOF. Por otro lado, LOCI
con conceptos probabilı́sticos.</p>
<dl class="function">
<dt id="LOOP">
<code class="descname">LOOP</code><span class="sig-paren">(</span><em>k = 20</em>, <em>lamda=3</em><span class="sig-paren">)</span><a class="headerlink" href="#LOOP" title="Enlazar permanentemente con esta definición">¶</a></dt>
<dd><p>Constructor para la creación del objeto de la clase LOOP.</p>
<dl class="field-list simple">
<dt class="field-odd">Parámetros</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>int</strong> – k, número de k vecinos a calcular</p></li>
<li><p><strong>int</strong> – lamda, párametro para regular la normalización</p></li>
</ul>
</dd>
<dt class="field-even">Tipo del valor devuelto</dt>
<dd class="field-even"><p>objeto de la clase LOOP</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt>
<code class="descname">fit_predict</code><span class="sig-paren">(</span><em>data</em><span class="sig-paren">)</span></dt>
<dd><p>Método para aplicar el algoritmo LOOP a una matriz de datos.</p>
<dl class="field-list simple">
<dt class="field-odd">Parámetros</dt>
<dd class="field-odd"><p><strong>numpy.array</strong> – data, matriz de datos</p>
</dd>
<dt class="field-even">Tipo del valor devuelto</dt>
<dd class="field-even"><p>numpy.array de probabilidad anomalia [0-1]</p>
</dd>
</dl>
</dd></dl>

</div>
<div class="section" id="ldof">
<h1>LDOF<a class="headerlink" href="#ldof" title="Enlazar permanentemente con este título">¶</a></h1>
<p>Local Outlier Probability (LoOP), utiliza la distancia relativa
de un objeto a sus vecinos para medir la cantidad de objetos que se desvıían
de su vecindario disperso.</p>
<dl class="function">
<dt id="LDOF">
<code class="descname">LDOF</code><span class="sig-paren">(</span><em>k = 20</em><span class="sig-paren">)</span><a class="headerlink" href="#LDOF" title="Enlazar permanentemente con esta definición">¶</a></dt>
<dd><p>Constructor para la creación del objeto de la clase LDOF.</p>
<dl class="field-list simple">
<dt class="field-odd">Parámetros</dt>
<dd class="field-odd"><p><strong>int</strong> – k, número de k vecinos a calcular</p>
</dd>
<dt class="field-even">Tipo del valor devuelto</dt>
<dd class="field-even"><p>objeto de la clase LOOP</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt>
<code class="descname">fit_predict</code><span class="sig-paren">(</span><em>data</em><span class="sig-paren">)</span></dt>
<dd><p>Método para aplicar el algoritmo LDOF a una matriz de datos.</p>
<dl class="field-list simple">
<dt class="field-odd">Parámetros</dt>
<dd class="field-odd"><p><strong>numpy.array</strong> – data, matriz de datos</p>
</dd>
<dt class="field-even">Tipo del valor devuelto</dt>
<dd class="field-even"><p>numpy.array de puntuaciones de anomalía</p>
</dd>
</dl>
</dd></dl>

</div>
<div class="section" id="pinn-lof">
<h1>PINN-LOF<a class="headerlink" href="#pinn-lof" title="Enlazar permanentemente con este título">¶</a></h1>
<p>Projection-Indexed Nearest-Neighbour (PINN), en este algoritmo se
propone un método de detección de valores atı́picos
locales proyectivo basado en LOF.</p>
<dl class="function">
<dt>
<code class="descname">PINN-LOF(k = 20, t=2, s=1, h=20)</code></dt>
<dd><p>Constructor para la creación del objeto de la clase PINN-LOF.</p>
<dl class="field-list simple">
<dt class="field-odd">Parámetros</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>int</strong> – k, número de k vecinos a calcular</p></li>
<li><p><strong>int</strong> – t, probabilidad de seleccion de caracteristicas para la proyección</p></li>
<li><p><strong>int</strong> – s, probabilidad de selección para la proyección</p></li>
<li><p><strong>int</strong> – h, número de k vecinos a calcular en la proyección</p></li>
</ul>
</dd>
<dt class="field-even">Tipo del valor devuelto</dt>
<dd class="field-even"><p>objeto de la clase PINN-LOF</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt>
<code class="descname">fit_predict</code><span class="sig-paren">(</span><em>data</em><span class="sig-paren">)</span></dt>
<dd><p>Método para aplicar el algoritmo PINN-LOF a una matriz de datos.</p>
<dl class="field-list simple">
<dt class="field-odd">Parámetros</dt>
<dd class="field-odd"><p><strong>numpy.array</strong> – data, matriz de datos</p>
</dd>
<dt class="field-even">Tipo del valor devuelto</dt>
<dd class="field-even"><p>numpy.array de puntuaciones de anomalía</p>
</dd>
</dl>
</dd></dl>

</div>
<div class="section" id="outres">
<h1>OUTRES<a class="headerlink" href="#outres" title="Enlazar permanentemente con este título">¶</a></h1>
<p>Outres es un algoritmo que propone desarrollar una puntuación de anomalı́as basada
en la desviación de objetos en las proyecciones subespaciales. Para la selección de
dichos subespacios se analiza la uniformidad de los datos en ellos.</p>
<dl class="function">
<dt id="OUTRES">
<code class="descname">OUTRES</code><span class="sig-paren">(</span><em>epsilon=15</em>, <em>alpha=0.01</em><span class="sig-paren">)</span><a class="headerlink" href="#OUTRES" title="Enlazar permanentemente con esta definición">¶</a></dt>
<dd><p>Constructor para la creación del objeto de la clase OUTRES.</p>
<dl class="field-list simple">
<dt class="field-odd">Parámetros</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>int</strong> – epsilon, radio para la selección del vecindario</p></li>
<li><p><strong>float</strong> – alpha, limite de uniformidad que se permite como interesante</p></li>
</ul>
</dd>
<dt class="field-even">Tipo del valor devuelto</dt>
<dd class="field-even"><p>objeto de la clase OUTRES</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt>
<code class="descname">fit_predict</code><span class="sig-paren">(</span><em>data</em><span class="sig-paren">)</span></dt>
<dd><p>Método para aplicar el algoritmo OUTRES a una matriz de datos.</p>
<dl class="field-list simple">
<dt class="field-odd">Parámetros</dt>
<dd class="field-odd"><p><strong>numpy.array</strong> – data, matriz de datos</p>
</dd>
<dt class="field-even">Tipo del valor devuelto</dt>
<dd class="field-even"><p>numpy.array de puntuaciones de anomalía</p>
</dd>
</dl>
</dd></dl>

</div>
<div class="section" id="odin">
<h1>ODIN<a class="headerlink" href="#odin" title="Enlazar permanentemente con este título">¶</a></h1>
<p>Outlier Detection using Indegree Number (ODIN),es un algoritmo que hace
uso del grafico de los k-vecinos más cercanos y usa el grado de los nodos
para el calculo de anomalías</p>
<dl class="function">
<dt id="ODIN">
<code class="descname">ODIN</code><span class="sig-paren">(</span><em>k=20</em>, <em>t=0.01</em><span class="sig-paren">)</span><a class="headerlink" href="#ODIN" title="Enlazar permanentemente con esta definición">¶</a></dt>
<dd><p>Constructor para la creación del objeto de la clase ODIN.</p>
<dl class="field-list simple">
<dt class="field-odd">Parámetros</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>int</strong> – k, número de k vecinos a calcular</p></li>
<li><p><strong>int</strong> – t, umbral de dicisión</p></li>
</ul>
</dd>
<dt class="field-even">Tipo del valor devuelto</dt>
<dd class="field-even"><p>objeto de la clase ODIN</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt>
<code class="descname">fit_predict</code><span class="sig-paren">(</span><em>data</em><span class="sig-paren">)</span></dt>
<dd><p>Método para aplicar el algoritmo ODIN a una matriz de datos.</p>
<dl class="field-list simple">
<dt class="field-odd">Parámetros</dt>
<dd class="field-odd"><p><strong>numpy.array</strong> – data, matriz de datos</p>
</dd>
<dt class="field-even">Tipo del valor devuelto</dt>
<dd class="field-even"><p>numpy.array de decisión 1-0</p>
</dd>
</dl>
</dd></dl>

</div>
<div class="section" id="meandist">
<h1>MeanDIST<a class="headerlink" href="#meandist" title="Enlazar permanentemente con este título">¶</a></h1>
<p>El algoritmo MeanDIST usa la la media de las distancias en su vecindario
para ordenar a los vérticesy seleccionar los que más se desvian.</p>
<dl class="function">
<dt id="MeanDIST">
<code class="descname">MeanDIST</code><span class="sig-paren">(</span><em>k=20</em>, <em>t=1.5</em><span class="sig-paren">)</span><a class="headerlink" href="#MeanDIST" title="Enlazar permanentemente con esta definición">¶</a></dt>
<dd><p>Constructor para la creación del objeto de la clase MeanDIST.</p>
<dl class="field-list simple">
<dt class="field-odd">Parámetros</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>int</strong> – k, número de k vecinos a calcular</p></li>
<li><p><strong>int</strong> – t, parámatro para ampliar o reducir el umbral.</p></li>
</ul>
</dd>
<dt class="field-even">Tipo del valor devuelto</dt>
<dd class="field-even"><p>objeto de la clase MeanDIST</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt>
<code class="descname">fit_predict</code><span class="sig-paren">(</span><em>data</em><span class="sig-paren">)</span></dt>
<dd><p>Método para aplicar el algoritmo MeanDIST a una matriz de datos.</p>
<dl class="field-list simple">
<dt class="field-odd">Parámetros</dt>
<dd class="field-odd"><p><strong>numpy.array</strong> – data, matriz de datos</p>
</dd>
<dt class="field-even">Tipo del valor devuelto</dt>
<dd class="field-even"><p>numpy.array de decisión 1-0</p>
</dd>
</dl>
</dd></dl>

</div>
<div class="section" id="kdist">
<h1>KDIST<a class="headerlink" href="#kdist" title="Enlazar permanentemente con este título">¶</a></h1>
<p>El algoritmo KDIST el máximo de las distancias a
sus k-vecinos más cercanos para ordenar a los vértices y
seleccionar los que más se desvian.</p>
<dl class="function">
<dt id="KDIST">
<code class="descname">KDIST</code><span class="sig-paren">(</span><em>k=20</em>, <em>t=1.5</em><span class="sig-paren">)</span><a class="headerlink" href="#KDIST" title="Enlazar permanentemente con esta definición">¶</a></dt>
<dd><p>Constructor para la creación del objeto de la clase KDIST.</p>
<dl class="field-list simple">
<dt class="field-odd">Parámetros</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>int</strong> – k, número de k vecinos a calcular</p></li>
<li><p><strong>int</strong> – t, parámatro para ampliar o reducir el umbral.</p></li>
</ul>
</dd>
<dt class="field-even">Tipo del valor devuelto</dt>
<dd class="field-even"><p>objeto de la clase KDIST</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt>
<code class="descname">fit_predict</code><span class="sig-paren">(</span><em>data</em><span class="sig-paren">)</span></dt>
<dd><p>Método para aplicar el algoritmo KDIST a una matriz de datos.</p>
<dl class="field-list simple">
<dt class="field-odd">Parámetros</dt>
<dd class="field-odd"><p><strong>numpy.array</strong> – data, matriz de datos</p>
</dd>
<dt class="field-even">Tipo del valor devuelto</dt>
<dd class="field-even"><p>numpy.array de decisión 1-0</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="enumerate">
<code class="descname">enumerate</code><span class="sig-paren">(</span><em>sequence</em><span class="optional">[</span>, <em>start=0</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#enumerate" title="Enlazar permanentemente con esta definición">¶</a></dt>
<dd></dd></dl>

<ul class="simple">
<li><p><a class="reference internal" href="genindex.html"><span class="std std-ref">Índice</span></a></p></li>
<li><p><a class="reference internal" href="py-modindex.html"><span class="std std-ref">Índice de Módulos</span></a></p></li>
<li><p><a class="reference internal" href="search.html"><span class="std std-ref">Página de Búsqueda</span></a></p></li>
</ul>
</div>


          </div>
          
        </div>
      </div>
      <div class="sphinxsidebar" role="navigation" aria-label="main navigation">
        <div class="sphinxsidebarwrapper">
<h1 class="logo"><a href="#">PyDBOD</a></h1>








<h3>Navegación</h3>

<div class="relations">
<h3>Related Topics</h3>
<ul>
  <li><a href="#">Documentation overview</a><ul>
  </ul></li>
</ul>
</div>
<div id="searchbox" style="display: none" role="search">
  <h3>Búsqueda rápida</h3>
    <div class="searchformwrapper">
    <form class="search" action="search.html" method="get">
      <input type="text" name="q" />
      <input type="submit" value="Ir a" />
    </form>
    </div>
</div>
<script type="text/javascript">$('#searchbox').show(0);</script>








        </div>
      </div>
      <div class="clearer"></div>
    </div>
    <div class="footer">
      &copy;2019, Miguel Ángel López Robles.
      
      |
      Powered by <a href="http://sphinx-doc.org/">Sphinx 2.0.1</a>
      &amp; <a href="https://github.com/bitprophet/alabaster">Alabaster 0.7.12</a>
      
      |
      <a href="_sources/index.rst.txt"
          rel="nofollow">Page source</a>
    </div>

    

    
  </body>
</html>