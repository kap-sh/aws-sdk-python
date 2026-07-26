"""Generated from Smithy shape ``com.amazonaws.medialive#InputFilter``."""

from typing import Literal, TypeAlias, cast

"""Input Filter"""
InputFilter: TypeAlias = Literal[
    "AUTO",
    "DISABLED",
    "FORCED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputFilter) -> str:
    return value


def deserialize_json(data: str) -> InputFilter:
    return cast(InputFilter, data)
