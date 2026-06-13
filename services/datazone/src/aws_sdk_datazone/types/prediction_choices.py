"""Generated from Smithy shape ``com.amazonaws.datazone#PredictionChoices``."""

from typing import TypeAlias

PredictionChoices: TypeAlias = list["int"]


# --- restJson1 ser/de ---
def serialize_json(value: PredictionChoices) -> list:
    return list(value)


def deserialize_json(data: list) -> PredictionChoices:
    return list(data)
