"""Generated from Smithy shape ``com.amazonaws.medicalimaging#Operator``."""

from typing import Literal, TypeAlias, cast

Operator: TypeAlias = Literal[
    "EQUAL",
    "BETWEEN",
]


# --- restJson1 ser/de ---
def serialize_json(value: Operator) -> str:
    return value


def deserialize_json(data: str) -> Operator:
    return cast(Operator, data)
