import kserve
from typing import Dict


class BondModel(kserve.Model):
    def __init__(self, name: str, model_uri: str):
        super().__init__(name)
        self.name = name
        self.model_uri = model_uri
        self.load()

    def load(self):
        self.ready = True

    def predict(self, payload: Dict, headers: Dict[str, str] = None) -> Dict:
        inputs = payload["inputs"][0]["data"]

        return {"predictions": inputs}
