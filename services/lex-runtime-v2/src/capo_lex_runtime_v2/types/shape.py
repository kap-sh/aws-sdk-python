"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#Shape``."""

from typing import Literal, TypeAlias, cast

Shape: TypeAlias = Literal[
    "Scalar",
    "List",
    "Composite",
]


# --- restJson1 ser/de ---
def serialize_json(value: Shape) -> str:
    return value


def deserialize_json(data: str) -> Shape:
    return cast(Shape, data)
