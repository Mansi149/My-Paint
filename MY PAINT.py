# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 11:04:21 2020

@author: Mansi
"""

# Imports
from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
import PIL
from PIL import Image, ImageDraw, ImageGrab, ImageTk
from tkinter import messagebox

root = Tk()
root.title( 'MY PAINT' )
root.geometry( '800x800' )
brush_color = "black"

def paint( e ) :
	# Paint Background Change
	brush_width = '%0.0f' % float( my_slider.get() )
	brush_type2 = brush_type.get()
	# Startng osition
	a1 = e.x-1
	b1 = e.y-1
	
	# Ending Position
	a2 = e.x+1
	b2 = e.y+1

	# Create Line
	my_canvas.create_line( a1, b1, a2, b2, fill = brush_color, width = brush_width, capstyle = brush_type2, smooth = True )
	
# Changing the Brush Size
def change_brush_size( thing ) :
	slider_label.config( text = '%0.0f' % float( my_slider.get() ) )
    
# Changing the Brush Color
def change_brush_color():
	global brush_color
	brush_color = "black"
	brush_color = colorchooser.askcolor( color = brush_color )[1]
    
# Changing the Canvas Color
def change_canvas_color( ) :
	global bg_color
	bg_color = "black"
	bg_color = colorchooser.askcolor( color = bg_color )[1]
	my_canvas.config( bg = bg_color )

def clear_screen( )   :
	my_canvas.delete( ALL )
	my_canvas.config( bg = 'white' )

# Saving the Image
def save_as_png():
	result = filedialog.asksaveasfilename( initialdir = 'C:\\Users\\Mansi\\Desktop\\Projects\\Python Projects', filetypes = ( ( "png files", "*.png" ), ( "all files", "*.*" ) ) )
	if result.endswith( '.png' ):
		pass
	else:
		result+='.png'
	result_label = Label( root, text = result )
	result_label.pack( pady = 20 )
	if result:
		a = root.winfo_rooty()+my_canvas.winfo_a()
		b = root.winfo_rooty()+my_canvas.winfo_b()
		a1 = a+my_canvas.winfo_width()
		b1 = b+my_canvas.winfo_height()
		ImageGrab.grab().crop( ( a, b, a1, b1 ) ).save( result )
        
		# Image saved successfully 
		messagebox.showinfo( "Saved successfully","Heya Artist, your canavs has been saved !" )

# Create Canvas	
w = 1000
h = 500
bgcolor = 'black'
my_canvas = Canvas( root, width = w, height = h, bg = 'white' )
my_canvas.pack( pady = 20 )
my_canvas.bind('<B1-Motion>', paint )

# Brush Options 
brush_options_frame = Frame( root )
brush_options_frame.pack( pady = 20 )

# Brush Width
brush_size_frame = LabelFrame( brush_options_frame, text = 'Brush Size')
brush_size_frame.grid( row = 0, column = 0, padx = 50 )

# Brush Slider
my_slider = ttk.Scale( brush_size_frame, from_ = 1, to = 100, command = change_brush_size, orient = HORIZONTAL, value = 10 )
my_slider.pack( padx = 10, pady = 10 )

# Brush Slider Label
slider_label=Label( brush_size_frame,text = my_slider.get() )
slider_label.pack( pady = 5 )

# Brush Types
brush_type_frame = LabelFrame( brush_options_frame, text = 'Brush Type', height = 400 )
brush_type_frame.grid( row = 0, column = 1, padx = 50 )
brush_type=StringVar()
brush_type.set( 'round' )

# Buttons for Brush Types
brush_type_radio1 = Radiobutton( brush_type_frame, text = 'Round ', variable = brush_type, value = 'round' )
brush_type_radio2 = Radiobutton( brush_type_frame, text = 'Slash ', variable = brush_type, value = 'butt' )
brush_type_radio3 = Radiobutton( brush_type_frame, text = 'Diamond ', variable = brush_type, value = 'projecting' )
brush_type_radio1.pack( anchor = W )
brush_type_radio2.pack( anchor = W )
brush_type_radio3.pack( anchor = W )

# Change Color
change_colors_frame = LabelFrame( brush_options_frame, text = "Change Colors" )
change_colors_frame.grid( row = 0, column = 2 )

# Button for Brush Color Change
brush_color_button = Button( change_colors_frame, text = "Brush Color", command = change_brush_color )
brush_color_button.pack( pady = 10, padx = 10 )

# Button for Canvas Color Change
canvas_color_button = Button( change_colors_frame, text = "Canvas Color", command = change_canvas_color )
canvas_color_button.pack( pady = 10, padx = 10 )

# Options
options_frame = LabelFrame( brush_options_frame, text = "Options" )
options_frame.grid( row = 0, column = 3, padx = 50 )

# Clear Screen Button
clear_button = Button( options_frame, text = "Clear Screen", command = clear_screen )
clear_button.pack( padx = 10, pady = 10 )

# Save Image Button
sav_image_button = Button( options_frame, text = "Save", command = save_as_png )
sav_image_button.pack( padx = 10, pady = 10 )

root.mainloop()