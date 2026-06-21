"""Generated from Smithy shape ``com.amazonaws.connect#Comparison``."""

from typing import Literal, TypeAlias, cast

Comparison: TypeAlias = Literal["LT",]


# --- restJson1 ser/de ---
def serialize_json(value: Comparison) -> str:
    return value


def deserialize_json(data: str) -> Comparison:
    return cast(Comparison, data)
