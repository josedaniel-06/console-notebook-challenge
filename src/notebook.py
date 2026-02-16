import code

from datetime import datetime
class Note:

    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    def  __init__(self, code: str, title: str, text: str, importance: str):
         self.code = code
         self.title = title
         self.text = text
         self.importance = importance
         self.creation_date = datetime.now()
