"""Generated from Smithy shape ``com.amazonaws.lambda#OperationType``."""

from typing import Literal, TypeAlias, cast

OperationType: TypeAlias = Literal[
    "EXECUTION",
    "CONTEXT",
    "STEP",
    "WAIT",
    "CALLBACK",
    "CHAINED_INVOKE",
]


# --- restJson1 ser/de ---
def serialize_json(value: OperationType) -> str:
    return value


def deserialize_json(data: str) -> OperationType:
    return cast(OperationType, data)
