"""Generated from Smithy shape ``com.amazonaws.appflow#PardotConnectorOperator``."""

from typing import Literal, TypeAlias, cast

PardotConnectorOperator: TypeAlias = Literal[
    "PROJECTION",
    "EQUAL_TO",
    "NO_OP",
    "ADDITION",
    "MULTIPLICATION",
    "DIVISION",
    "SUBTRACTION",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NUMERIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: PardotConnectorOperator) -> str:
    return value


def deserialize_json(data: str) -> PardotConnectorOperator:
    return cast(PardotConnectorOperator, data)
