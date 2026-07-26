"""Generated from Smithy shape ``com.amazonaws.pinpoint#Operator``."""

from typing import Literal, TypeAlias, cast

Operator: TypeAlias = Literal[
    "ALL",
    "ANY",
]


# --- restJson1 ser/de ---
def serialize_json(value: Operator) -> str:
    return value


def deserialize_json(data: str) -> Operator:
    return cast(Operator, data)
