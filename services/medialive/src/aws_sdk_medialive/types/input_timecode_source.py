"""Generated from Smithy shape ``com.amazonaws.medialive#InputTimecodeSource``."""

from typing import Literal, TypeAlias, cast

"""Documentation update needed"""
InputTimecodeSource: TypeAlias = Literal[
    "ZEROBASED",
    "EMBEDDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputTimecodeSource) -> str:
    return value


def deserialize_json(data: str) -> InputTimecodeSource:
    return cast(InputTimecodeSource, data)
