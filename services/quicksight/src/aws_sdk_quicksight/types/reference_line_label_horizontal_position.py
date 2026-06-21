"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLineLabelHorizontalPosition``."""

from typing import Literal, TypeAlias, cast

ReferenceLineLabelHorizontalPosition: TypeAlias = Literal[
    "LEFT",
    "CENTER",
    "RIGHT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceLineLabelHorizontalPosition) -> str:
    return value


def deserialize_json(data: str) -> ReferenceLineLabelHorizontalPosition:
    return cast(ReferenceLineLabelHorizontalPosition, data)
