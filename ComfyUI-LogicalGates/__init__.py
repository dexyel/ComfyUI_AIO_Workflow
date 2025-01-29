class ORGate:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "text1": ("STRING", {"forceInput": True}),
                "text2": ("STRING", {"forceInput": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)
    FUNCTION = "or_gate"
    CATEGORY = "Logical Gates"
    
    def or_gate(self, text1=None, text2=None):
        return (text1 or text2,)    

NODE_CLASS_MAPPINGS = {
    "OR Gate": ORGate,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OR Gate": "OR Gate",
}