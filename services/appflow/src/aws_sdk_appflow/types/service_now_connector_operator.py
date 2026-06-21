"""Generated from Smithy shape ``com.amazonaws.appflow#ServiceNowConnectorOperator``."""

from typing import Literal, TypeAlias, cast

ServiceNowConnectorOperator: TypeAlias = Literal[
    "PROJECTION",
    "CONTAINS",
    "LESS_THAN",
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
def serialize_json(value: ServiceNowConnectorOperator) -> str:
    return value


def deserialize_json(data: str) -> ServiceNowConnectorOperator:
    return cast(ServiceNowConnectorOperator, data)
