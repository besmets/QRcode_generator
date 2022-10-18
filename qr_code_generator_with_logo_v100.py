'''
===============================================================================

   QR CODE GENERATOR WITH CENTRAL LOGO

===============================================================================

Version 1.0, 18/10/2022

Author:
    Prof. Dr. Benoît SMETS
    Royal Museum for Central Africa / Vrije Universiteit Brussel
    Belgium
    Contact: benoit.smets@africamuseum.be / benoit.smets@vub.be

Repository:
    https://github.com/besmets/QRcode_generator
    
Citation:
    Smets, B. (2022) - Generator of QR codes with a central logo.
    https://github.com/besmets/QRcode_generator
    
Script written with Python 3.9.13

Required Python packages:
    - Pillow (PIL) v9 or above
    - qrcode

License:
    MIT License (https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt)
===============================================================================
'''

# Import
from PIL import Image
import qrcode

#=======================================================================#
#==========================   SETUP SECTION   ==========================#

url_to_code = 'https://georiska.africamuseum.be/en/'

folder_logo = '/Users/username/Documents/LOGOS/GeoRiskA/'
   # With a '/' at the end of the path
logo_filename = 'GeoRiskA_Logo_normal2018_circle.jpg'

output_folder_qrcode = '/Users/username/Documents/LOGOS/QR_codes/'
   # With a '/' at the end of the path
qrcode_name = 'QR_georiska_website'

qrcode_file_extension = '.png'

color_for_code = 'Black'

dpi = 300

display_after_creation = 'y'    # 'y' or 'n'

#=======================   END OF SETUP SECTION   ======================#
#=======================================================================#

# 1. Preparing the logo for the QR code
#-------------------------------------- 

logo_path = folder_logo + logo_filename
logo = Image.open(logo_path)
 
# adjust image size
width_percent = (100/float(logo.size[0]))
height_size = int((float(logo.size[1])*float(width_percent)))
logo = logo.resize((100, height_size), Image.Resampling.LANCZOS)
QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
 
# 2. Generate the QRcode
#-----------------------

# Add url
QRcode.add_data(url_to_code)
 
# Create the QR code
QRcode.make()

# Colorize the QR code
QR_image = QRcode.make_image(fill_color=color_for_code, back_color="white").convert('RGB')
 
# Set size of QR code and insert logo
pos = ((QR_image.size[0] - logo.size[0]) // 2, (QR_image.size[1] - logo.size[1]) // 2)
QR_image.paste(logo, pos)
 
# 3. Save and/or display
#-----------------------

QR_image.save(output_folder_qrcode + qrcode_name + qrcode_file_extension, dpi=(dpi, dpi))

if display_after_creation == 'y':
    QR_image.show()

# 4. Print info in the console
#-----------------------------

print(' ')
print('================================================================')
print('=      QR Code Generator with central logo  (version 1.0)      =')
print('================================================================')
print('(c) B. Smets, RMCA/VUB, 2022')
print(' ')
print(' ')
print('A QR code has been generated for ')
print('--> ' + str(url_to_code))
print(' ')
print('It has been saved to ')
print('--> ' + str(output_folder_qrcode))
print(' ')
print(' ')
print('----------------------------------------------------------------')
print('   PROCESSING ENDED SUCCESSFULLY')
print('----------------------------------------------------------------')
print(' ')
