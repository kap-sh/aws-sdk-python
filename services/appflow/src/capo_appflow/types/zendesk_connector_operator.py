"""Generated from Smithy shape ``com.amazonaws.appflow#ZendeskConnectorOperator``."""

from typing import Literal, TypeAlias, cast

ZendeskConnectorOperator: TypeAlias = Literal[
    "PROJECTION",
    "GREATER_THAN",
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
def serialize_json(value: ZendeskConnectorOperator) -> str:
    return value


def deserialize_json(data: str) -> ZendeskConnectorOperator:
    return cast(ZendeskConnectorOperator, data)
