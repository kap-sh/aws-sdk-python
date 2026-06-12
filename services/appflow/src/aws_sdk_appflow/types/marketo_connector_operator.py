"""Generated from Smithy shape ``com.amazonaws.appflow#MarketoConnectorOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

MarketoConnectorOperator: TypeAlias = Literal[
    "PROJECTION",
    "LESS_THAN",
    "GREATER_THAN",
    "BETWEEN",
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
        "LESS_THAN",
        "GREATER_THAN",
        "BETWEEN",
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


def serialize_json(value: MarketoConnectorOperator) -> str:
    return value


def deserialize_json(data: str) -> MarketoConnectorOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MarketoConnectorOperator value: {data!r}")
    return cast(MarketoConnectorOperator, data)
