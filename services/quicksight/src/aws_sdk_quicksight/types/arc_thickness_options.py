"""Generated from Smithy shape ``com.amazonaws.quicksight#ArcThicknessOptions``."""

from typing import Literal, TypeAlias, cast

ArcThicknessOptions: TypeAlias = Literal[
    "SMALL",
    "MEDIUM",
    "LARGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ArcThicknessOptions) -> str:
    return value


def deserialize_json(data: str) -> ArcThicknessOptions:
    return cast(ArcThicknessOptions, data)
