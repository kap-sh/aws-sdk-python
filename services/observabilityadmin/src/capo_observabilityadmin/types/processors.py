"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#Processors``."""

from typing import TypeAlias

Processors: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: Processors) -> list:
    return list(value)


def deserialize_json(data: list) -> Processors:
    return list(data)
