"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#Sinks``."""

from typing import TypeAlias

Sinks: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: Sinks) -> list:
    return list(value)


def deserialize_json(data: list) -> Sinks:
    return list(data)
