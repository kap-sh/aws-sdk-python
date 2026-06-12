"""Generated from Smithy shape ``com.amazonaws.appflow#InforNexusConnectorOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

InforNexusConnectorOperator: TypeAlias = Literal[
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


def serialize_json(value: InforNexusConnectorOperator) -> str:
    return value


def deserialize_json(data: str) -> InforNexusConnectorOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InforNexusConnectorOperator value: {data!r}"
        )
    return cast(InforNexusConnectorOperator, data)
