"""Generated from Smithy shape ``com.amazonaws.appflow#PardotConnectorOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: PardotConnectorOperator) -> str:
    return value


def deserialize_json(data: str) -> PardotConnectorOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PardotConnectorOperator value: {data!r}")
    return cast(PardotConnectorOperator, data)
