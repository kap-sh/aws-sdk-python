"""Generated from Smithy shape ``com.amazonaws.medialive#InputClass``."""

from typing import Literal, TypeAlias, cast

"""A standard input has two sources and a single pipeline input only has one."""
InputClass: TypeAlias = Literal[
    "STANDARD",
    "SINGLE_PIPELINE",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputClass) -> str:
    return value


def deserialize_json(data: str) -> InputClass:
    return cast(InputClass, data)
