"""Generated from Smithy shape ``com.amazonaws.appflow#SAPODataConnectorOperator``."""

from typing import Literal, TypeAlias, cast

SAPODataConnectorOperator: TypeAlias = Literal[
    "PROJECTION",
    "LESS_THAN",
    "CONTAINS",
    "GREATER_THAN",
    "BETWEEN",
    "LESS_THAN_OR_EQUAL_TO",
    "GREATER_THAN_OR_EQUAL_TO",
    "EQUAL_TO",
    "NOT_EQUAL_TO",
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
    "NO_OP",
]


# --- restJson1 ser/de ---
def serialize_json(value: SAPODataConnectorOperator) -> str:
    return value


def deserialize_json(data: str) -> SAPODataConnectorOperator:
    return cast(SAPODataConnectorOperator, data)
