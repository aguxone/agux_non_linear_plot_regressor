#coding=<utf-8>
#Graficdor con extracción de Texto
import agux_non_linear_plot_regressor_v1_1_0_gui_file as GUI
from agux_non_linear_plot_regressor_v1_1_0_gui_file import *

def imports():
	global np, curve_fit, Figure, FigureCanvas, NavigationToolbar
	import numpy as np
	from scipy.optimize import curve_fit
	from matplotlib.figure import Figure
	from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
	from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar

#COLOCAR LA API DE MATPLOTLIB PRIMERO
#NOTA IMPORTANTE: La API del matplotlib tiene un re bug con no mostrar el gráfico cuando se abre la aplicación. Lo muestra solo recién cuando maximizamos la ventana o al resizeamos. En su momento encontré que dándole a self.canvas.draw() se solucionaba, pero no siempre. Encontré otro workaround más permanente, que es agregar un atributo al FRAME (en wxBuilder). Porque ejemplo agregarle wx_Iconize en la sección de "Fram Style", supuestamente debería iniciar la aplicación minimiazaba esto pero no hace nada, a costa de eso parece que algo hace y hace aparecer el canvas de matplotlib, es el menor esfuerzo para corregir esa tontera creo yo.
# ADEMÁS en la clase siguiente, colocaré los vínculos de los botones usando la convención que inventé. Para el vínculo en sí se llamará "wxfunción". Dentro del vínculo irá el nombre de la función a secas "función". Y después definiremos externamente a la clase esa "función".

#Definimos la clase derivada que agarra el output del WxBuilder.

class MyMPLFrame1(GUI.MyFrame1):
	def __init__(self, parent):
		GUI.MyFrame1.__init__(self, parent)
		#ACÁ le decimos que herede todo el init que venía en el init del "MyFrame1" que estaba en el output del WxBuilder. O sea herederá todas las clases de Wx y los botoncitos, paneles y cosas que hayamos creado allí.

		# Emepcemos deifniiendo un size RELATIVO que es MUY fácil con
		# GetDisplaySize, 0 es el tamaño horizontal y 1 el vertical
		# wxFormBuilder no me permite hacerlo relativo.
		# Tambien le damos un SetPosition un poco más grande
		# self.SetPosition(wx.Point(wx.GetDisplaySize()[0]/10, wx.GetDisplaySize()[1]/10))
		displaysize=wx.GetDisplaySize()
		self.SetPosition(wx.Point(displaysize[0]/12, displaysize[1]/100))
		self.Size = (displaysize[0]/1.2,displaysize[1]/1.07)

		# Resizeo el panel 3, el único método que funcioan es SetSizeHints
		self.m_panel3.SetSizeHints(-1, displaysize[1]/1.5)

		# Y oculto un panelcito que tiene la regresión custom, así en wxformbuilder lo veo
		self.m_panel4.Hide()
		if self.m_radioBox31.GetSelection()==0:
			self.m_panel6.Hide()
			displaysize=wx.GetDisplaySize()
			self.m_splitter1.SetSashPosition(displaysize[0]/3.31)

		#Ahora vamos a empezar añanadiendo las cosas del matplotlib a los paneles y lugares que corresponda. Lo pondré como un método de la clase, y abajo de todo decido cargarlo. Esto es para que primero cargue la GUI con algunos botoncito y de una sensación de un menor tiempo de carga inicial!

		# AGREGO UN BIND de un EVENTO A MANO
		# porque wxformbuilder NO puede hacerlo por tener un bug
		# porque se les chanfleó para python y nadie lo actualizó
		# desde entonces, el evento al cerrar el dropdown menu
		# o sea closeup, el de dropwond tampoco funca.
		self.m_comboBox1.Bind( wx.EVT_COMBOBOX_CLOSEUP, self.wxfit_custom)

		# Primero defino las variables de algunos elementos de la GUI
		# que que combiene renombrar para tener a mano para el código
		# y que sea más entendible.
		# Aunque estoy quemando memoria a lo loco... pero bueno.
		self.delimiter = self.m_radioBox3
		self.delimiter_value = ""
		self.checkbox_errorbar_x = self.m_checkBox1
		self.checkbox_errorbar_y = self.m_checkBox2
		self.filename  = self.m_textCtrl1
		self.graphtype = self.m_radioBox4
		self.x_err_estimate_box = self.m_textCtrl12
		self.y_err_estimate_box = self.m_textCtrl13		
		self.statusbar = self.m_textCtrl6
		self.statusbar2 = self.m_textCtrl9
		self.statusbar3 = self.m_textCtrl10
		self.statusbar4 = self.m_textCtrl11
		self.tipos_de_fiteo = self.m_comboBox1
		self.param_ini_a0 = self.m_textCtrl3
		self.param_ini_b0 = self.m_textCtrl4
		self.param_ini_c0 = self.m_textCtrl5
		self.param_ini_d0 = self.m_textCtrl14
		self.param_ini_e0 = self.m_textCtrl15
		self.param_ini_f0 = self.m_textCtrl16
		self.panel_param_ini = self.m_panel5
		self.panel_custom_fit = self.m_panel4
		self.nparams = self.m_textCtrl7
		self.expression = self.m_textCtrl61
		self.initial_params = self.m_textCtrl8

	def cargar_mpl(self):
		imports()
		#---------------SIZER Y LAYOUT-----------------------------------------##
		self.bSizer4 = wx.BoxSizer( wx.VERTICAL ) #NOTA IMPORTANTE: LA CLASE DERIVADA, por algún MOTIVO como que no hereda los SIZER que venían en MyFrame1. Es porque WxFormBuilder no los crea como self.sizer, sino como sizer a secas lo cual es una cagada. YO EN ESTA CLASE DERIVADA LOS PONGO COMO SELF, así si quiero que alguien más los herede lo puede hacer. Por ende para independizar TODO, conviene dentro del panel (2), crear un SIZER (número 3), y dentro del mismo OTRO panel (panel 3 aquí). Dentro de este panel3 creamos un sizer4 manualmente acá y queda atrapado matplot en ese sizer y este panel, pero puede seguir coexistiendo y ajustándose con las cosas del panel2 que están ordenadas por el sizer3. Es una garcha un pasito más pero bueno safa.
		#VAN EN ESTE ORDEN LAS COSAS. SE CREA EL SIZER. SE LO FITEA AL PANEL 3. Y POR ULTIMO SE DICE AL PANEL 3 QUE LO COLOQUE DENTRO DE SI MISMO.
		# self.bSizer4 = wx.FlexGridSizer( 2, 0,0,0)
		# self.bSizer4.SetFlexibleDirection( wx.VERTICAL )
		# self.bSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL)
		self.bSizer4.Fit( self.m_panel3 )
		self.m_panel3.SetSizer( self.bSizer4 )
		self.m_panel3.Layout() #Este comando no sé para qué garcha es la verdad, no hace nada si está o no, pero el wxbuilder lo pone.

		#AHORA OJO, YO QUIERO CARGUE HASTA ACÁ!!! ME LLEVÓ BOCHAZA DE TIEMPO ESTOOOOO,
		self.Show() #SE PUEDE PONER SHOW EN EL MEDIO DEL INIT JAJAJ, LOCURA PERO SI BUENO SIMPLIFICA LA VIDA. LE DAMOS SHOW.
		# Y DPS DE QUE MUESTRE, BUENO HACEMOS LOS IMPORTS Y ESO
				#--------Panel de MPL----------------------------------------##		

		self.figure = Figure(tight_layout=True) #Very important the tight layour
		# in order to fit the plot on the whole panel
		self.axes = self.figure.add_subplot(111)
		# self.axes = self.figure.subplots(1)
		# self.axes.set_position([1000,1000,1000,1000])
		# self.figure.set_position([500,500,500,500])
		self.canvas = FigureCanvas(self.m_panel3, -1, self.figure) #NOTAR QUE DENTRO DEL PARENTESIS, hay que especificar el PANEL en el que va a estar nuestra ventana (y no el sizer)
		self.bSizer4.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.EXPAND) #Acá especficiamos el SIZER. Poner el nombre del sizer que corresponda acá para que aparezca allí, ojo con mayúsculas y minúsculas.
		#Con esto se agrego el toolbar del matplotlib, requiere una función adicional
		
		#----------------TOOLBAR intrinseca de MPL------------------------------##
		#A partir de acá agregamos la Toolbar intrínseca del Matplotlib!
		self.toolbar = NavigationToolbar(self.canvas)
		# self.toolbar.figsize([10,10])
		self.toolbar.Realize()
		self.bSizer4.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND) #Acá hay que agregarla al Sizer!, ojo con las mayúsculas y eso
		self.toolbar.update()
		self.canvas.draw()

		#COMANDO UTILES PARA LA VIDA.
		# self.canvas.draw() : ESTO REFRESCA el canvas y hace que las cosas aparezcan, parecido al "show"
		# self.axes.cla() : Esto BORRA las cosas graficadas todito.


	#-----------------VINCULOS-----------------------------------------------------------
	
	#Primero una función que extraiga todos los "TextCtrl" para no tener que andar tecleando ochenta cosas en cada función, después solo llamamos a parámetros y listo.
	def parametros(self):
		a0= float(self.param_ini_a0.GetValue()) #Ojo convertirlos a float porque si no queda como un string creo u algo, y scipy se vuelve loco con ello
		b0= float(self.param_ini_b0.GetValue())
		c0= float(self.param_ini_c0.GetValue())
		d0= float(self.param_ini_d0.GetValue())
		e0= float(self.param_ini_e0.GetValue())
		f0= float(self.param_ini_f0.GetValue())
		entrada= open(self.filename.GetValue(), 'r')
		modelo=str(self.tipos_de_fiteo.GetValue())
		return a0, b0, c0,d0,e0,f0,entrada, modelo

	# Quiero una función que asigne strings
	# a cada radiobutton para que interprete después
	# numpy qué delimitador usar
	def wxradiobuttons(self, event):
		# "tab"
		if self.delimiter.GetSelection()==3:
			self.delimiter_value="	"

		# "space"
		if self.delimiter.GetSelection()==2:
			self.delimiter_value=" "

		# ","
		if self.delimiter.GetSelection()==1:
			self.delimiter_value=","

		# ";"
		if self.delimiter.GetSelection()==0:
			self.delimiter_value=";"


	def wx_file_select_dialog(self, event):
		with wx.FileDialog(self, "Open Txt or CSV file", wildcard="All supported (*.csv;*.txt)|*.csv;*.txt", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return
	        # the user changed their mind

	        # Proceed loading the file chosen by the user
			pathname = fileDialog.GetPath()
			try:
				with open(pathname, 'r') as file:
					self.m_textCtrl1.SetValue(pathname)
			except IOError:
					wx.LogError("Cannot open file '%s'." % newfile)
					frame.statusbar.SetValue("Cannot open file")
					frame.statusbar2.SetValue("")
					frame.statusbar3.SetValue("")
					frame.statusbar4.SetValue("")

	def wx_pop_error_est(self,event):
		if self.m_radioBox31.GetSelection()==1:
			self.m_radioBox5.Show()
			self.m_panel6.Show()
			# self.m_splitter1.SetSashPosition(799)
			displaysize=wx.GetDisplaySize()
			self.m_splitter1.SetSashPosition(displaysize[0]/3.32)
		else:
			self.m_radioBox5.Hide()
			self.m_panel6.Hide()
			# self.m_splitter1.SetSashPosition(802)
			displaysize=wx.GetDisplaySize()
			self.m_splitter1.SetSashPosition(displaysize[0]/3.29)

	def wx_change_errors(self,event):
		# If constant error "No" is selected, then
		if self.m_radioBox5.GetSelection()==1:
			self.m_staticText40.Hide()
			self.m_staticText17.Show()
			self.m_textCtrl13.SetValue(str(5))
			displaysize=wx.GetDisplaySize()
			self.m_splitter1.SetSashPosition(displaysize[0]/3.33)
		else:
			# If constant error "Yes" is selected, then
			self.m_staticText17.Hide()
			self.m_staticText40.Show()
			self.m_textCtrl13.SetValue(str(0.5))
			displaysize=wx.GetDisplaySize()
			self.m_splitter1.SetSashPosition(displaysize[0]/3.34)

	def wxborrar(self,event):
		# Primero le decimos que borre
		self.axes.cla()
		# Después que haga el draw que es un commit
		# de algún modo
		self.canvas.draw()
	
	def wxextraercolumnas( self, event ):
		entrada=open(self.m_textCtrl1.GetValue(),'r')
		datos1=extraeryfitear(None,None,None,entrada,None)
	
	def wxprintear( self, event ):
		a0, b0, c0, entrada, modelo=self.parametros()
		print(a0,b0,c0,modelo)


	def ploteo_general(self, graf1, fit_switch):
		# FITEO O PLOT: Chekeamos si quiere hacer un plot del FITEO o un ploteo de los DATOS nomás
		if fit_switch == True: # Si True, entonces va a plotear el fiteo y no tienen barra de error el fit
			fuente_datos_y = graf1.valoresfiteados
			x_err_param = None
			y_err_param = None			
		else:
			# Si es False bueno graficaremos los errores porque serán los datos
			# y además se plotearan los datos y claramente.
			# BARRAS DE ERROR: De acuerdo si están chekados los checkboxes plotearemos las barras o no
			fuente_datos_y = graf1.datos_y
			if self.checkbox_errorbar_x.GetValue()==True:
				x_err_param = graf1.error_x
			else:
				x_err_param = None
			if self.checkbox_errorbar_y.GetValue()==True:
				y_err_param = graf1.error_y
			else:
				y_err_param=None

		# LINESTYLE: Si está seleccionado Scatter (1)queremos que el linestyle sea none, ninguna línea
		if self.graphtype.GetSelection()==1:
			line_param = "none"
			marker_param= "."
		else:
			line_param="-"
			marker_param= None

		# Y finalmente llamamos a la función para plotear con errorbars que puede incluir TODO lo anterior en una sola función. #Capsize es el topecito de las barras de error.
		self.axes.errorbar(x=graf1.datos_x, y=fuente_datos_y, xerr= x_err_param , yerr=y_err_param, marker=marker_param, markersize=3, linestyle=line_param, capsize=2)
		self.canvas.draw() # Esto es otra cosa fundamental, es el análogo a plt.show. Con esto "refresca" el canvas digamos. Literalmente hace eso. Curiosamente al maximizar la ventan también lo refresca pero bueno.

	def wxplotear( self, event ):
		fit_switch= False
		a0, b0, c0, d0, e0, f0, entrada, modelo=self.parametros()
		frame.statusbar.SetValue("")
		frame.statusbar2.SetValue("")
		frame.statusbar3.SetValue("")
		frame.statusbar4.SetValue("")
		try:
			graf1=extraeryfitear(a0,b0,c0,d0,e0,f0, entrada, modelo)
			graf1.extraercolumnas()
			self.ploteo_general(graf1, fit_switch)
		except Exception as e:
			frame.statusbar.SetValue(str(e))
			frame.statusbar2.SetValue("Error")
			frame.statusbar3.SetValue("Error")
			frame.statusbar4.SetValue("Error")

	def wxfitear( self, event ):
		fit_switch = True
		a0, b0, c0, d0, e0, f0, entrada, modelo=self.parametros()
		frame.statusbar.SetValue("")
		frame.statusbar2.SetValue("")
		frame.statusbar3.SetValue("")
		frame.statusbar4.SetValue("")
		try:
			graf1=extraeryfitear(a0,b0,c0,d0,e0,f0,entrada,modelo)
			# ACA DIFIERE con plotear, que haremos que fitee
			graf1.fitear()
			self.ploteo_general(graf1, fit_switch)
		except Exception as e:
			frame.statusbar.SetValue(str(e))
			frame.statusbar2.SetValue("Error")
			frame.statusbar3.SetValue("Error")
			frame.statusbar4.SetValue("Error")

	def wxfit_custom (self,event):
		# Si el combobox queda en custom que es la primera opción
		# (pero no la default que es 1), entonces al cerrarse
		# el menu closeup
		if self.tipos_de_fiteo.GetSelection()==0:
			self.panel_param_ini.Hide() # Que se esconda
			self.panel_custom_fit.Show()# Que muestre el de fit
			# Cambio el sashposition un mero pixel
			# porque si no se buguea y aparece todo mezclado 
			# self.m_splitter1.SetSashPosition(798)
			displaysize=wx.GetDisplaySize()
			self.m_splitter1.SetSashPosition(displaysize[0]/3.28)

		else:
			self.panel_custom_fit.Hide()
			self.panel_param_ini.Show() # Que se esconda
			 # Que muestre el de fit

	def wxinstructions (self, event):
		dialog.Show()

	def wx_about_button (self, event):
		about_dialog.Show()

	def wxclose(self,event):
		# self.Destroy()
		# wxGetApp().ExitMainLoop()
		# pass
		# wx.CallAfter(self.Destroy(), wx.Exit())
		wx.Exit() # Este anda bábaro pero en principio es algo de emergencia
		# sys.exit()

	#-------------------------------------------------------------------------------


###---------FUNCIONES EXTERNAS DE VERDAD QUE CALCULAN LO QUE HAYA QUE CALCULAR-----------###

class extraeryfitear:
	# La idea es que SAIPAI cree instancias, cuyos variables de instancia A ELEGIR sean los parámetros iniciales de fiteo, y el modelo que queremos fitear.
	#ADEMÁS cada instancia va a nacer con 3 listitas PROPIAS que no se van a mezclar con el resto de las instancias. Una es la de datos_x y datos_y (que salrán del archivo.txt del que extraigamos los datos) y otras listita llamada "valoresfiteados" que guardará los los valores "y" del fiteo que le hagamos posteriormente.

	#SciPy tendrá métodos después, todos los métodos dependen del método "extraercolumnas" que extrae los datos. Pero tanto extraercolumnas como el resto se pueden usar "intuitivamente" de forma independiente. Son sencillos siguen los métodos "graficar", "fitear" y "graficar_y_fitear" para que meramente nos tire un gráfico con una de esas cosas.

	def __init__(self, a0,b0,c0,d0,e0,f0, entrada,seleccion_de_modelo):

		#Variables a elegir de la instancia
		self.a0=a0
		self.b0=b0
		self.c0=c0
		self.d0=d0
		self.e0=e0
		self.f0=f0
		self.seleccion_de_modelo=seleccion_de_modelo

		#Variables con las que nace la instancia
		self.entrada=entrada
		self.datos_x=[]
		self.datos_y=[]
		self.error_x=[]
		self.error_y=[]
		self.valoresfiteados=[]
		self.full_dict= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","z"]

	def extraercolumnas(self):
		# self.datos_x=[]
		# self.datos_y=[]		
		# n=0
		extraction = np.genfromtxt(frame.filename.GetValue(), delimiter=frame.delimiter_value, skip_header=0)
		self.datos_x= extraction[:,0]
		self.datos_y= extraction[:,1]

		# Si el radiobox dice 0 o "Yes", extraemos las columnas de error
		if frame.m_radioBox31.GetSelection()==0:
			self.error_x = extraction[:,2]
			self.error_y = extraction[:,3]
		# Si el radiobox es 0 o "No" entonces estimamos error y a la mierda
		if frame.m_radioBox31.GetSelection()==1:
			self.error_x =  self.datos_x * (float(frame.x_err_estimate_box.GetValue())/100) 
			self.error_y = self.datos_y * (float(frame.y_err_estimate_box.GetValue())/100)

	def mapeo_letras_a_params(self, popt):
		dict_mapeo = {"x": "hola", "np": np}
		for i in range(len(popt)):
			dict_mapeo[self.full_dict[i]]= popt[i]

		return dict_mapeo

	def mapeo_letras_a_errores(self, pcov):
		# Le sacamos la diagonal a pcov (error consigo mismo de cada parámetro) y le sacamos raíz cuadrada porque pcov da a varianza.
		matriz_error = np.sqrt(np.diag(pcov))
		dict_error = {}
		for i in range(len(matriz_error)):
			dict_error[self.full_dict[i]]= matriz_error[i]

		return dict_error

	def calculador_r_squared(self, datos_y,valoresfiteados ):
		ssres = np.sum( np.square(datos_y - valoresfiteados) )
		sstot = np.sum( np.square(datos_y - np.mean(datos_y) ))
		r_squared = 1- (ssres/sstot)

		# Ahora el adjusted
		n = datos_y.size #numero de filas
		p = 1 # p es nro variables explicatorias, acá siempre 1
		adjusted_r_squared= 1 - ( 1- r_squared ) * (n-1) / (n-p)
		return r_squared, adjusted_r_squared

	def calculador_rmse(self, datos_y, valoresfiteados):
		n= datos_y.size
		ssres_sobre_n = np.sum( (np.square(datos_y - valoresfiteados))/n  )
		rmse = np.sqrt(ssres_sobre_n)
		return rmse

	def calculador_chi2(self, datos_y, valoresfiteados, n_params, error_x, error_y):
		# En rigor cada dato podría tener su error medido.
		# Acá por ahora estimaremos con el desvío de nuestras
		# mediciones lo cual mucho sentido no tiene pero bueno.
		
		residuos = datos_y - valoresfiteados
		# df degrees of freedom para chi2 es n datos - número PARAMETROS (no variables)
		# para una lineal serán 2 por ej
		df = datos_y.size - n_params
		desv = np.std(residuos)
		media = np.mean(residuos)
		restand = residuos/media
		desvstand = np.std(restand)
		sigmarel= 0.01

		# Si error_y NO está vacía, entonces calcula chi2 con los errores
		# del usuario
		if len(self.error_y)!=0:
			chi2 = np.sum( np.square(residuos/ error_y  ) )
		# Si está vacía como inicializó, estimo con alguna magnitud.
		else:
			chi2 = np.sum( np.square(residuos/ (sigmarel*datos_y)  ) )
		redchi2 = chi2/df
		return df, chi2, redchi2

	def calculo_y_output_regresion(self, modelo, expression, p0):
		# Primero definimos si el usuario quiere tener en cuenta los errores en y
		# para la regresión que sería lo correcto (0 es Yes)
		if frame.m_radioBox41.GetSelection()==0:
			sigma_param = self.error_y
		else:
			sigma_param = None
		# Primero el fiteo, con un try por si no puede

		popt,pcov=curve_fit(modelo,self.datos_x,self.datos_y,p0, sigma=sigma_param, method="trf")

		# Se extraen los parámetros necesarios en un diccionario
		mapeo_letras_a_params_memoria = self.mapeo_letras_a_params(popt)
		# Se calculan los valores predichos
		for valor_de_x in self.datos_x:	
			mapeo_letras_a_params_memoria["x"] = valor_de_x
			operacion= eval(expression, mapeo_letras_a_params_memoria)
			# operacion= pruebucha3(valor_de_x, *eval( pruebucha2() ) )
			self.valoresfiteados.append(operacion)

		# Por un motivo que desconozco, después del último
		#"for" queda bugueadísimo el diccionario, le agrega mil keys
		# que nada que ver no sé por qué, horas debugueando y nada.
		# Por eso lo vuelvo a recargar en la memoria, así no lo re-cargo
		# dentro del for cada vez, a costa de cargarlo una vez más nomás.
		# Además le quito los campos x y np para que no se muestren
		mapeo_letras_a_params_memoria = self.mapeo_letras_a_params(popt)
		del mapeo_letras_a_params_memoria['x']
		del mapeo_letras_a_params_memoria['np']

		# Guardamos el diccionario que mapea los errores a los parámetros
		# por último
		dict_error = self.mapeo_letras_a_errores(pcov)
		# Sacamos el números de parametros ahora a partir del mapeo
		n_params= len(mapeo_letras_a_params_memoria.keys())

		# Por último calculamos todas las métricas de
		# performance
		r_squared=self.calculador_r_squared(self.datos_y, self.valoresfiteados )
		rmse = self.calculador_rmse( self.datos_y, self.valoresfiteados)
		r_squared, adjusted_r_squared = self.calculador_r_squared(self.datos_y, self.valoresfiteados)
		df,chi2 ,redchi2= self.calculador_chi2(self.datos_y, self.valoresfiteados, n_params, self.error_x, self.error_y)
		# Posteamos los resultados en las status bar
		frame.statusbar.SetValue("Params : " +str(mapeo_letras_a_params_memoria))
		frame.statusbar2.SetValue("St. Dev : " +str(dict_error))
		frame.statusbar3.SetValue("Rsquared : " + str(adjusted_r_squared) + "; RMSE : " + str(rmse) )
		frame.statusbar4.SetValue("Chi2 : " + str(chi2) + "; DF : " + str(df) + " ;  Reduced Chi2 : " + str(redchi2))

	def fitear(self):
		self.datos_x=[] #Con estas listas hago que RESETEE sus listas las instancia
		self.datos_y=[]
		self.valoresfiteados=[]
		self.extraercolumnas()	#Extraigo los datos del archivo y los guardo en la lista de la instancia

		if self.seleccion_de_modelo=="Linear (a*x+b)":
			expression = "a*x+b"
			modelo = lambda x,a,b: eval(expression)
			p0=[self.a0,self.b0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="Exponential (a*exp(b*x)+c)":
			# IDEM a lineal, cambia expression y p0 solamente
			expression = "a*(np.exp(x*b))+c"
			modelo = lambda x,a,b,c: eval(expression)
			p0=[self.a0,self.b0,self.c0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="Quadratic a*(x**2)+(b*x)+c":
			expression = "a*(x**2)+(b*x)+c"
			modelo = lambda x,a,b,c: eval(expression)
			p0=[self.a0,self.b0,self.c0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="Cubic a*(x**3)+b*(x**2)+c*x+d":
			expression = "a*(x**3)+b*(x**2)+c*x+d"
			modelo = lambda x,a,b,c,d: eval(expression)
			p0=[self.a0,self.b0,self.c0, self.d0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="Quartic a*(x**4)+b*(x**3)+c*(x**2)+d*x+e":
			expression = "a*(x**4)+b*(x**3)+c*(x**2)+d*x+e"
			modelo = lambda x,a,b,c,d,e: eval(expression)
			p0=[self.a0,self.b0,self.c0, self.d0, self.e0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="Quintic a*(x**5)+b*(x**4)+c*(x**3)+d*(x**2)+e*x+f":
			expression = "a*(x**5)+b*(x**4)+c*(x**3)+d*(x**2)+e*x+f"
			modelo = lambda x,a,b,c,d,e,f: eval(expression)
			p0=[self.a0,self.b0,self.c0, self.d0, self.e0, self.f0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="Sine a*(sin(b*x+c))+d":
			# IDEM a lineal, cambia expression y p0 solamente
			expression = "a*(np.sin(x*b+c))+d"
			modelo = lambda x,a,b,c,d: eval(expression)
			p0=[self.a0,self.b0,self.c0, self.d0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="Cosine a*(cos(b*x+c))+d":
			# IDEM a lineal, cambia expression y p0 solamente
			expression = "a*(np.cos(b*x+c))+d"
			modelo = lambda x,a,b,c,d: eval(expression)
			p0=[self.a0,self.b0,self.c0, self.d0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="Squared Sine a*((sin(b*x+c))**2)+d":
			expression = "a*((np.sin(b*x+c))**2)+d"
			modelo = lambda x,a,b,c,d: eval(expression)
			p0=[self.a0,self.b0,self.c0, self.d0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="Sin+Cos a*(sin(x*b))+ c*(cos(x*d)+e":
			expression = "a*(np.sin(x*b))+ c*(np.cos(x*d)+e)"
			modelo = lambda x,a,b,c,d,e: eval(expression)
			p0=[self.a0,self.b0,self.c0, self.d0, self.e0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="DampSine a*(exp((b*x+c)))*(sin(d*x+e))+f":
			expression = "a*(np.exp((b*x+c)))*(np.sin(d*x+e))+f"
			modelo = lambda x,a,b,c,d,e,f: eval(expression)
			p0=[self.a0,self.b0,self.c0, self.d0, self.e0, self.e0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="Tangent a*tan(b*x)+c":
			expression = "a*np.tan(b*x)+c"
			modelo = lambda x,a,b,c: eval(expression)
			p0=[self.a0,self.b0,self.c0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="Arctan a*arctan(b*x)+c":
			expression = "a*np.arctan(b*x)+c"
			modelo = lambda x,a,b,c: eval(expression)
			p0=[self.a0,self.b0,self.c0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="Ln Natural Log a*ln(b*x)+c":
			expression = "a*np.log(b*x)+c"
			modelo = lambda x,a,b,c: eval(expression)
			p0=[self.a0,self.b0,self.c0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="Logarithm base 10 a*log10(b*x)+c":
			expression = "a*np.log10(b*x)+c"
			modelo = lambda x,a,b,c: eval(expression)
			p0=[self.a0,self.b0,self.c0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="Logarithm base 2 a*log2(b*x)+c":
			expression = "a*np.log2(b*x)+c"
			modelo = lambda x,a,b,c: eval(expression)
			p0=[self.a0,self.b0,self.c0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="Gaussian a*exp(-(x-b)**2/(2*c**2))+d":
			expression = "a*np.exp(-(x-b)**2/(2*c**2))+d"
			modelo = lambda x,a,b,c,d: eval(expression)
			p0=[self.a0,self.b0,self.c0, self.d0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="MBoltz (a/pi)**3/2*4*pi*(x**2)*exp(-a*(x**2))+b":
			expression = "( (a/(np.pi) )**(1.5) )*4*(np.pi)*(x**2)*np.exp(-a*(x**2))+b"
			modelo = lambda x,a,b: eval(expression)
			p0=[self.a0, self.b0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="Logistic a/(1+(np.exp(-b*(x-c))))+d":
			expression = "(a/ ( 1+ (np.exp( -b*(x-c) ) ) ) )+ d"
			modelo = lambda x,a,b,c,d: eval(expression)
			p0=[self.a0,self.b0,self.c0, self.d0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="Sigmoideal classical 1/(1+(exp(-a*x)))":
			expression = "1/(1+(np.exp(-a*x)))"
			modelo = lambda x,a: eval(expression)
			p0=[self.a0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="Hyperbolic Tangent a*tanh(b*(x-c))+d":
			expression = "a*np.tanh(b*(x-c))+d"
			modelo = lambda x,a,b,c,d: eval(expression)
			p0=[self.a0,self.b0,self.c0, self.d0]
			self.calculo_y_output_regresion(modelo, expression,p0)

		if self.seleccion_de_modelo=="Custom":
			# La idea es juntar todos los parámetros ya masticados
			# que necesita scipy curve_fit con dos funciones ya que
			# es bastante exquisito con sus inputs.
			# Al terminar bueno hacer el fiteo obviamente

			# Primero defino algunas variables que voy a usar en todas las
			# funciones.

			# Numero de parametros que puso el usuario
			num = int(frame.nparams.GetValue())
			# Expresion que escribio el usuario
			expression = frame.expression.GetValue()
			# Un diccionario con la cantidad de parametros que puede elegir
			# el usuario. De la "a" a la "z" excepto la x y ñ, 25 letras total
			# full_dict= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","z"]

			# Función que creará un string de tipo lambda x,...: expression a partir del input en las cajitas nparams y expression.
			def crear_string_lambda_expression():
				# Creamos un string que empieza en lambda que le
				# agregaremos cosas
				string_creado="lambda x,"

				# Obtenemos el nro de parámetros del modelo
				# que se puso de input y la expresion escrita
				for i in range (num):
					# Si es el último que lo sume y termine en dos puntos
					if i==num-1:
						string_creado=string_creado+self.full_dict[i]+": "
					#Si no es el último que lo sume y termine en coma
					else:
						string_creado= string_creado+self.full_dict[i]+","

				# Por último le sumamos la "expression" que
				# se escribió de input
				string_creado = string_creado + expression
						
				return(string_creado)

			# Función que creará una lista de parametros iniciales
			# deben estar escritos separados por espacio
			def crear_lista_params_inis():
				# Obtengo los param ins de textCtrl y los saco en una lista
				# con un split
				lista_strings= frame.initial_params.GetValue().split()
				# Los transformo a todos en floats ahora y hago una lista
				return (list(map(float, lista_strings)))

			# Ahora por fin fiteamos
			modelo=eval(crear_string_lambda_expression())
			p0=crear_lista_params_inis()

			# Y ahora fiteo con el método de la clase ya que se encargd de hacer todo

			self.calculo_y_output_regresion(modelo, expression, p0)

	###----------------------------#########----------------------------------------###

class MyInstructions1(GUI.MyDialog1):
	def __init__(self, parent):
		GUI.MyDialog1.__init__(self, parent)
		displaysize=wx.GetDisplaySize()
		self.SetPosition(wx.Point(displaysize[0]/3, displaysize[1]/50))
		self.Size = (displaysize[0]/2.4,displaysize[1]/1.2)

		### CODIGO DE PRUEBAS PARA ESCALADO DE LA IMAGEN #####
		# # Resizeo el panel 3, el único método que funcioan es SetSizeHints
		# print(self.m_bitmap1.GetScaleMode())
		# self.m_bitmap1.ScaleMode=2
		# print(self.m_bitmap1.GetScaleMode())
		# self.prueba = self.m_bitmap1
		# self.prueba = wx.Image(name="icono_app.png", type=wx.BITMAP_TYPE_ANY)
		# self.prueba.Rescale( displaysize[1]/500,displaysize[1]/500, quality=wx.IMAGE_QUALITY_HIGH)
		# self.m_panel7.SetSizeHints(displaysize[0]/5, displaysize[1]/50)
		# self.prueba.Update()
		# Reemplazo el staticbitmap del código original por wx.bitmap
		# que tiene soporte para python, el otro para c++ nomás
		# self.m_bitmap1 =  wx.GenStaticBitmap('example_eq.jpg', wx.BITMAP_TYPE_JPEG)
		# # self.m_bitmap1.SetScaleMode("Scale_Fill")
		# # self.image = self.m_bitmap1.ConvertToImage()
		# self.m_bitmap1.SetSizeHints(wx.Size(-1, displaysize[1]/50))
		# self.m_bitmap1 = wx.Image("example_eq.jpg", wx.BITMAP_TYPE_ANY)
		# self.m_bitmap1.Scale(displaysize[0]/100, displaysize[1]/100)
        # self.image.Rescale(int(displaysize[0]/1), int(displaysize[1]/1))
		# # # Y oculto un panelcito que tiene la regresión custom, así en wxformbuilder lo veo
		# self..SetSize(displaysize[0]/2.4,displaysize[1]/1.4)
		# self.m_panel7.SetSizeHints(displaysize[0]/5, displaysize[1]/10)
		# self.m_panel4.Hide()
		# if self.m_radioBox31.GetSelection()==0:
		# 	self.m_panel6.Hide()
		# 	self.self.m_splitter1.SetSashPosition(314)

class MyAboutDialog(GUI.MyDialog2):
	def __init__(self, parent):
		GUI.MyDialog2.__init__(self, parent)
		displaysize=wx.GetDisplaySize()
		self.SetPosition(wx.Point(displaysize[0]/3, displaysize[1]/50))
		self.Size = (displaysize[0]/2.4,displaysize[1]/2)

#Imports Externos:
#Los dejo AFUERA SÍ, por qué? Por que no quiero que se llamen cuando EMPIEZA LA GUI. Quiero que se importen un ratito después, entonces los llamo cuando todo termina y listo.

##### Enablign High DPI support for Windows before everything ######################
########################################################################
try:

    from ctypes import OleDLL

    # Turn on high-DPI awareness to make sure rendering is sharp on big

    # monitors with font scaling enabled.

    OleDLL('shcore').SetProcessDpiAwareness(1)

except AttributeError:

    # We're on a non-Windows box.

    pass

except OSError:

    # exc.winerror is often E_ACCESSDENIED (-2147024891/0x80070005).

    # This occurs after the first run, when the parameter is reset in the

    # executable's manifest and then subsequent calls raise this exception

    # See last paragraph of Remarks at

    # [https://msdn.microsoft.com/en-us/library/dn302122(v=vs.85).aspx](https://msdn.microsoft.com/en-us/library/dn302122(v=vs.85).aspx)

    pass
##########################################################################
###################################################################



app = wx.App(False)
app.SetExitOnFrameDelete(True)
frame = MyMPLFrame1(None) #Comando para abrir la ventanucha
frame.wxradiobuttons(None) # Primero le doy el radio buttons para que
# guarde las variables que corresponden a los radiobutton,
# en esta app es solo "delimiter" que guarda strings
frame.SetIcon(wx.Icon("./icono_app.png", wx.BITMAP_TYPE_PNG))

dialog = MyInstructions1(None)
dialog.SetIcon(wx.Icon("./icono_app.png", wx.BITMAP_TYPE_PNG))
dialog.Hide()

about_dialog = MyAboutDialog(None)
about_dialog.SetIcon(wx.Icon("./icono_app.png", wx.BITMAP_TYPE_PNG))
about_dialog.Hide()

frame.Show(True)
# dialog.Show(True)
frame.cargar_mpl()

displaysize=wx.GetDisplaySize()
frame.m_splitter1.SetSashPosition(displaysize[0]/3.3) # Es un workaroud, al mover el sash, maximizar, o minimizar se corrige el bug de que el panel de MPL no aparece, originalmente está en "-1" . El resto de los sash position en el código
# los corro a centésimas del divisor en cada caso y no se nota.
frame.m_splitter1.Update()

app.MainLoop()

#Código opcional de alguna utilidad en algún momento:
#NOTA: Para cargar cosas dps del mainloop en principio AL PARECER existen wx.CallAfter(funcion) y wx.CallLater(milisegundos,funcion). CallLater llamaría una únuca vez una función después de que pasen x milisegundos (un entero). Callafter llamaría una única vez algo, pero después de qué no sé es oscuro aún para mí.

#Ejemplo, puedo agregar acá a lo último atnes del mainloop
# wx.CallLater(2000, frame.pruebaloca)

#Thread:
	# def threadloco(self):
	# 	threadcito=threading.Thread(target=self.cargar_mpl, args=())
	# 	threadcito.daemon=True
	# 	threadcito.start()

#Imports en función
# def imports():
# 	global np, curve_fit, Figure, FigureCanvas, NavigationToolbar
# 	import numpy as np 
# 	from scipy.optimize import curve_fit
# 	from matplotlib.figure import Figure
# 	from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
# 	from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar