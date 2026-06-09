"""Generated from Smithy shape ``com.amazonaws.lambda#OperationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

OperationType: TypeAlias = Literal[
    "EXECUTION",
    "CONTEXT",
    "STEP",
    "WAIT",
    "CALLBACK",
    "CHAINED_INVOKE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXECUTION",
        "CONTEXT",
        "STEP",
        "WAIT",
        "CALLBACK",
        "CHAINED_INVOKE",
    )
)


def serialize_json(value: OperationType) -> str:
    return value


def deserialize_json(data: str) -> OperationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperationType value: {data!r}")
    return cast(OperationType, data)
