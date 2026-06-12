"""Generated from Smithy shape ``com.amazonaws.mediatailor#Audiences``."""

from typing import TypeAlias

Audiences: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: Audiences) -> list:
    return list(value)


def deserialize_json(data: list) -> Audiences:
    return list(data)
