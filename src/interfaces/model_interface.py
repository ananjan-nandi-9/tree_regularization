import torch
from typing import Dict, Any
from interfaces.result import Result


class ModelInterface:
    def create_input(self, data: Dict[str, torch.Tensor]) -> torch.Tensor:
        raise NotImplementedError

    def decode_outputs(self, outputs: Result) -> Any:
        raise NotImplementedError

    def __call__(self, data: Dict[str, torch.Tensor]) -> Result:
        raise NotImplementedError
