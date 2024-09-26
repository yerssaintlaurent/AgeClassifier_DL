from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.image_1.source = file
    self.file = file

  def model_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if hasattr(self, 'file'):
      predicted_class = anvil.server.call('predict_item', self.file)
      self.label_3.visible = True
      self.label_3.text = f'Predicted Class: {predicted_class}'
    else:
      alert("load an image first.")
