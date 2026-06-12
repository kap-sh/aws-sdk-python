"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ZendeskConnectorOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: ZendeskConnectorOperator) -> str:
    return value


def deserialize_json(data: str) -> ZendeskConnectorOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ZendeskConnectorOperator value: {data!r}")
    return cast(ZendeskConnectorOperator, data)
