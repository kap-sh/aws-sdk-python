"""Generated from Smithy shape ``com.amazonaws.medialive#InputLossImageType``."""

from typing import Literal, TypeAlias, cast

"""Input Loss Image Type"""
InputLossImageType: TypeAlias = Literal[
    "COLOR",
    "SLATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputLossImageType) -> str:
    return value


def deserialize_json(data: str) -> InputLossImageType:
    return cast(InputLossImageType, data)
