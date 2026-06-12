"""Generated from Smithy shape ``com.amazonaws.appflow#DatadogConnectorOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

DatadogConnectorOperator: TypeAlias = Literal[
    "PROJECTION",
    "BETWEEN",
    "EQUAL_TO",
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
        "BETWEEN",
        "EQUAL_TO",
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


def serialize_json(value: DatadogConnectorOperator) -> str:
    return value


def deserialize_json(data: str) -> DatadogConnectorOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatadogConnectorOperator value: {data!r}")
    return cast(DatadogConnectorOperator, data)
