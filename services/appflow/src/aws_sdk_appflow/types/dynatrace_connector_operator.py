"""Generated from Smithy shape ``com.amazonaws.appflow#DynatraceConnectorOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

DynatraceConnectorOperator: TypeAlias = Literal[
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


def serialize_json(value: DynatraceConnectorOperator) -> str:
    return value


def deserialize_json(data: str) -> DynatraceConnectorOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DynatraceConnectorOperator value: {data!r}"
        )
    return cast(DynatraceConnectorOperator, data)
