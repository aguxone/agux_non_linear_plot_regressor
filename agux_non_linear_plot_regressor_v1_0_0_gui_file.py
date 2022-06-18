# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Agux's Non Linear Plot Regressor", pos = wx.Point( -1,-1 ), size = wx.Size( 1059,1331 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_splitter1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME )
		self.m_splitter1.SetSashGravity( 0 )
		self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )
		self.m_splitter1.SetMinimumPaneSize( 1 )

		self.m_splitter1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.m_splitter1.SetBackgroundColour( wx.Colour( 254, 220, 156 ) )

		self.m_panel1 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_panel1.SetBackgroundColour( wx.Colour( 15, 147, 185 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText8 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Choose .csv or .txt file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )

		bSizer121 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl1 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, u"glutation_errors.csv", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer121.Add( self.m_textCtrl1, 1, wx.ALL, 5 )

		self.m_button51 = wx.Button( self.m_panel1, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer121.Add( self.m_button51, 1, wx.ALL, 5 )


		bSizer2.Add( bSizer121, 0, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		m_radioBox3Choices = [ u";", u",", u"space", u"tab" ]
		self.m_radioBox3 = wx.RadioBox( self.m_panel1, wx.ID_ANY, u"Delimiter", wx.DefaultPosition, wx.DefaultSize, m_radioBox3Choices, 4, wx.RA_SPECIFY_COLS )
		self.m_radioBox3.SetSelection( 1 )
		bSizer5.Add( self.m_radioBox3, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer5, 0, 0, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		wSizer1 = wx.WrapSizer( wx.VERTICAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		m_radioBox31Choices = [ u"Yes", u"No" ]
		self.m_radioBox31 = wx.RadioBox( self.m_panel1, wx.ID_ANY, u"Error cols present?", wx.DefaultPosition, wx.DefaultSize, m_radioBox31Choices, 2, wx.RA_SPECIFY_COLS )
		self.m_radioBox31.SetSelection( 1 )
		wSizer1.Add( self.m_radioBox31, 1, wx.ALL, 5 )

		self.m_staticText121 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Plot error bars?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )

		wSizer1.Add( self.m_staticText121, 0, wx.ALL, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox1 = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		self.m_checkBox2 = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Y", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox2.SetValue(True)
		bSizer12.Add( self.m_checkBox2, 0, wx.ALL, 5 )


		wSizer1.Add( bSizer12, 1, wx.EXPAND, 5 )


		bSizer4.Add( wSizer1, 0, wx.EXPAND, 5 )


		bSizer2.Add( bSizer4, 0, 0, 5 )

		self.m_panel6 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText17 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"% error estimates", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		bSizer17.Add( self.m_staticText17, 0, wx.ALL, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText15 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer13.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self.m_panel6, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_textCtrl12, 0, wx.ALL, 5 )

		self.m_staticText141 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Y", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )

		bSizer13.Add( self.m_staticText141, 0, wx.ALL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self.m_panel6, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_textCtrl13, 0, wx.ALL, 5 )


		bSizer17.Add( bSizer13, 1, wx.EXPAND, 5 )


		self.m_panel6.SetSizer( bSizer17 )
		self.m_panel6.Layout()
		bSizer17.Fit( self.m_panel6 )
		bSizer2.Add( self.m_panel6, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )

		m_radioBox4Choices = [ u"Continous", u"Scatter" ]
		self.m_radioBox4 = wx.RadioBox( self.m_panel1, wx.ID_ANY, u"Plot Type", wx.DefaultPosition, wx.DefaultSize, m_radioBox4Choices, 2, wx.RA_SPECIFY_COLS )
		self.m_radioBox4.SetSelection( 0 )
		bSizer31.Add( self.m_radioBox4, 0, wx.ALL, 5 )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		self.m_button5 = wx.Button( self.m_panel1, wx.ID_ANY, u"Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.m_button5, 1, wx.ALL, 5 )

		self.m_button10 = wx.Button( self.m_panel1, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.m_button10, 1, wx.ALL, 5 )


		bSizer31.Add( bSizer32, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer31, 0, wx.EXPAND, 5 )

		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticline21 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer61.Add( self.m_staticline21, 1, wx.ALL, 5 )


		bSizer2.Add( bSizer61, 0, wx.EXPAND, 5 )

		fgSizer4 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText12 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Choose fit curve", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		fgSizer4.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		fgSizer4.Add( self.m_staticText13, 0, wx.ALL, 5 )

		m_comboBox1Choices = [ u"Custom", u"Linear (a*x+b)", u"Exponential (a*exp(b*x)+c)", u"Quadratic a*(x**2)+(b*x)+c", u"Cubic a*(x**3)+b*(x**2)+c*x+d", u"Quartic a*(x**4)+b*(x**3)+c*(x**2)+d*x+e", u"Quintic a*(x**5)+b*(x**4)+c*(x**3)+d*(x**2)+e*x+f", u"Sine a*(sin(b*x+c))+d", u"Cosine a*(cos(b*x+c))+d", u"Squared Sine a*((sin(b*x+c))**2)+d", u"Sin+Cos a*(sin(x*b))+ c*(cos(x*d)+e", u"DampSine a*(exp((b*x+c)))*(sin(d*x+e))+f", u"Gaussian a*exp(-(x-b)**2/(2*c**2))+d", u"MBoltz (a/pi)**3/2*4*pi*(x**2)*exp(-a*(x**2))+b", u"Tangent a*tan(b*x)+c", u"Arctan a*arctan(b*x)+c", u"Ln Natural Log a*ln(b*x)+c", u"Logarithm base 10 a*log10(b*x)+c", u"Logarithm base 2 a*log2(b*x)+c", u"Logistic a/(1+(np.exp(-b*(x-c))))+d", u"Sigmoideal classical 1/(1+(exp(-a*x)))", u"Hyperbolic Tangent a*tanh(b*(x-c))+d" ]
		self.m_comboBox1 = wx.ComboBox( self.m_panel1, wx.ID_ANY, u"Exponential (a*exp(b*x)+c)", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		self.m_comboBox1.SetSelection( 2 )
		fgSizer4.Add( self.m_comboBox1, 0, wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		fgSizer4.Add( self.m_staticText20, 0, wx.ALL, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		m_radioBox41Choices = [ u"Yes", u"No" ]
		self.m_radioBox41 = wx.RadioBox( self.m_panel1, wx.ID_ANY, u"Account for  y_errors in regression?", wx.DefaultPosition, wx.DefaultSize, m_radioBox41Choices, 2, wx.RA_SPECIFY_COLS )
		self.m_radioBox41.SetSelection( 0 )
		bSizer16.Add( self.m_radioBox41, 0, wx.ALL, 5 )

		self.BT_fitear = wx.Button( self.m_panel1, wx.ID_ANY, u"Fit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.BT_fitear, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer4.Add( bSizer16, 1, wx.EXPAND, 5 )


		bSizer2.Add( fgSizer4, 0, 0, 5 )

		self.m_panel5 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer2 = wx.FlexGridSizer( 3, 4, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText3 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"a0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		fgSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, u"0.001", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"b0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		fgSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, u"0.001", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"c0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		fgSizer2.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, u"0.001", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl5, 0, wx.ALL, 5 )

		self.m_staticText171 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"d0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171.Wrap( -1 )

		fgSizer2.Add( self.m_staticText171, 0, wx.ALL, 5 )

		self.m_textCtrl14 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, u"0.001", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl14, 0, wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"e0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		fgSizer2.Add( self.m_staticText18, 0, wx.ALL, 5 )

		self.m_textCtrl15 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, u"0.001", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl15, 0, wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"f0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		fgSizer2.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.m_textCtrl16 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, u"0.001", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl16, 0, wx.ALL, 5 )


		self.m_panel5.SetSizer( fgSizer2 )
		self.m_panel5.Layout()
		fgSizer2.Fit( self.m_panel5 )
		bSizer2.Add( self.m_panel5, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_panel4 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.m_button8 = wx.Button( self.m_panel4, wx.ID_ANY, u"Instructions", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button8, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer26.Add( bSizer28, 0, wx.EXPAND, 5 )

		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText9 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Expression", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer27.Add( self.m_staticText9, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl61 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, u"(1/x**3)*a + (1/x**2)*b + (1/x)*c +d", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_textCtrl61, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer26.Add( bSizer27, 0, wx.EXPAND, 5 )

		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText11 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Nº params", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer30.Add( self.m_staticText11, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_textCtrl7, 1, wx.ALL, 5 )


		bSizer26.Add( bSizer30, 0, wx.EXPAND, 5 )

		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText10 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Initial Params", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer29.Add( self.m_staticText10, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, u"0.01 0.01 0.01 0.01", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.m_textCtrl8, 1, wx.ALL, 5 )


		bSizer26.Add( bSizer29, 0, wx.EXPAND, 5 )


		self.m_panel4.SetSizer( bSizer26 )
		self.m_panel4.Layout()
		bSizer26.Fit( self.m_panel4 )
		bSizer2.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		self.m_panel2 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel3 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel3.SetBackgroundColour( wx.Colour( 16, 207, 193 ) )

		bSizer3.Add( self.m_panel3, 0, wx.ALL|wx.TOP|wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl6 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,25 ), wx.TE_READONLY|wx.TE_WORDWRAP )
		bSizer21.Add( self.m_textCtrl6, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,25 ), wx.TE_READONLY|wx.TE_WORDWRAP )
		bSizer21.Add( self.m_textCtrl9, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,25 ), wx.TE_READONLY|wx.TE_WORDWRAP )
		bSizer21.Add( self.m_textCtrl10, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,25 ), wx.TE_READONLY|wx.TE_WORDWRAP )
		bSizer21.Add( self.m_textCtrl11, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( bSizer21, 0, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer3 )
		self.m_panel2.Layout()
		bSizer3.Fit( self.m_panel2 )
		self.m_splitter1.SplitVertically( self.m_panel1, self.m_panel2, 315 )
		bSizer1.Add( self.m_splitter1, 1, wx.EXPAND|wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.wxclose )
		self.m_button51.Bind( wx.EVT_BUTTON, self.wx_file_select_dialog )
		self.m_radioBox3.Bind( wx.EVT_RADIOBOX, self.wxradiobuttons )
		self.m_radioBox31.Bind( wx.EVT_RADIOBOX, self.wx_pop_error_est )
		self.m_radioBox4.Bind( wx.EVT_RADIOBOX, self.wxradiobuttons )
		self.m_button5.Bind( wx.EVT_BUTTON, self.wxplotear )
		self.m_button10.Bind( wx.EVT_BUTTON, self.wxborrar )
		self.BT_fitear.Bind( wx.EVT_BUTTON, self.wxfitear )
		self.m_button8.Bind( wx.EVT_BUTTON, self.wxinstructions )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def wxclose( self, event ):
		event.Skip()

	def wx_file_select_dialog( self, event ):
		event.Skip()

	def wxradiobuttons( self, event ):
		event.Skip()

	def wx_pop_error_est( self, event ):
		event.Skip()


	def wxplotear( self, event ):
		event.Skip()

	def wxborrar( self, event ):
		event.Skip()

	def wxfitear( self, event ):
		event.Skip()

	def wxinstructions( self, event ):
		event.Skip()

	def m_splitter1OnIdle( self, event ):
		self.m_splitter1.SetSashPosition( 315 )
		self.m_splitter1.Unbind( wx.EVT_IDLE )


###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1513,1247 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Instructions", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		self.m_staticText18.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )

		bSizer20.Add( self.m_staticText18, 0, wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"In order tu use a custom fit curve you'll need to follow these guidelines:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		bSizer20.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"- Expression: You'll have to use python and numpy syntax for the expression to be recognized. \nYou can use up to 25 parameters (standard alphabet except \"x\" character)\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		bSizer20.Add( self.m_staticText20, 0, wx.ALL, 5 )

		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Operations:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer20.Add( self.m_staticText24, 0, wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Addition: + , Substraction: - , Multiplication : * , Divition: / , Power: **", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		bSizer20.Add( self.m_staticText25, 0, wx.ALL, 5 )

		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Functions:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		bSizer20.Add( self.m_staticText26, 0, wx.ALL, 5 )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Exponential: np.exp() , Sine: np.sin() , Natural Logarithm: np.log(),\n Logarithm base 10:p.log10() ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		bSizer20.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"You can check the complete list at:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer20.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.m_hyperlink1 = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"https://numpy.org/doc/stable/reference/routines.math.html", u"https://numpy.org/doc/stable/reference/routines.math.html", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		bSizer20.Add( self.m_hyperlink1, 0, wx.ALL, 5 )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"- Nº of params: Use a integer number to specify number of parameters for your model", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer20.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"-Initial Params: Specify the initial parameters for each parameter (use the closest estimate you can for the algorithm to work properly) they'll be assigned to parameters in alphabetical order.\nInitial params use a point as decimal separator, and use a whitespace (bar)\nto separate between the different initial parameters. For example: 0.1 0.001 3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		bSizer20.Add( self.m_staticText23, 0, wx.ALL, 5 )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Custom Curve example:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		self.m_staticText28.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, wx.EmptyString ) )

		bSizer20.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.m_bpButton1 = wx.BitmapButton( self.m_panel7, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton1.SetBitmap( wx.Bitmap( u"example_eq.png", wx.BITMAP_TYPE_ANY ) )
		bSizer22.Add( self.m_bpButton1, 1, wx.ALL, 5 )


		self.m_panel7.SetSizer( bSizer22 )
		self.m_panel7.Layout()
		bSizer22.Fit( self.m_panel7 )
		bSizer20.Add( self.m_panel7, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Expression: a*np.log10(x) + b . np.sin(x) + ( c / (x**2) )", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		bSizer20.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Nº Params: 3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		bSizer20.Add( self.m_staticText30, 0, wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Initial Params: 0.01 3 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		bSizer20.Add( self.m_staticText31, 0, wx.ALL, 5 )


		self.SetSizer( bSizer20 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


