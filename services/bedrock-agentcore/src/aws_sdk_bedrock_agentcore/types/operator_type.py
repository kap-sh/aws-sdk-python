"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#OperatorType``."""

from typing import Literal, TypeAlias, cast

OperatorType: TypeAlias = Literal[
    "EQUALS_TO",
    "EXISTS",
    "NOT_EXISTS",
]


# --- restJson1 ser/de ---
def serialize_json(value: OperatorType) -> str:
    return value


def deserialize_json(data: str) -> OperatorType:
    return cast(OperatorType, data)
