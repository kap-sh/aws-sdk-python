"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLineLabelVerticalPosition``."""

from typing import Literal, TypeAlias, cast

ReferenceLineLabelVerticalPosition: TypeAlias = Literal[
    "ABOVE",
    "BELOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceLineLabelVerticalPosition) -> str:
    return value


def deserialize_json(data: str) -> ReferenceLineLabelVerticalPosition:
    return cast(ReferenceLineLabelVerticalPosition, data)
