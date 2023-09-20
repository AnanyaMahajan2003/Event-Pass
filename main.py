from PIL import Image, ImageDraw, ImageFont

# Sample data for the event pass (you can replace this with actual data)
event_data = {
    'participant_name' : 'John Doe',
    'image': 'person.jpg',
    'roll_no' : '21STUCHH010...'
}

# Load the event pass image template
event_pass_template = Image.open('pass.jpg')

# Create a drawing context
draw = ImageDraw.Draw(event_pass_template)

# You can add the font in the pass
font_path = "sample_font.ttf"  
text_font = ImageFont.truetype(font_path, size=24)
text_color = (0, 0, 0)

# Updating the ICFAI roll number:
rlnm_position = (1000, 260) 
event_name = event_data['roll_no'] 
draw.text(rlnm_position, event_name, font=text_font, fill=text_color)

# Updating the name
name = (620,470)
name_2 = (500,470)
event_name = event_data['participant_name']
draw.text(name_2, 'NAME :  ', font=text_font, fill=text_color)
draw.text(name, event_name, font=text_font, fill=text_color)


# Add the picture
participant_image = Image.open(event_data['image'])
participant_image = participant_image.resize((250, 250))
image_position = (1000, 325)
event_pass_template.paste(participant_image, image_position)


# Save the updated event pass as a new image file
event_pass_template.save(f'{event_data["participant_name"]}_pass.png')

