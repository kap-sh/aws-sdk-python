"""Generated from Smithy shape ``com.amazonaws.lambda#OperationAction``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_lambda.errors import DeserializationError

OperationAction: TypeAlias = Literal[
    "START",
    "SUCCEED",
    "FAIL",
    "RETRY",
    "CANCEL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "START",
        "SUCCEED",
        "FAIL",
        "RETRY",
        "CANCEL",
    )
)


def serialize_json(value: OperationAction) -> str:
    return value


def deserialize_json(data: str) -> OperationAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperationAction value: {data!r}")
    return cast(OperationAction, data)
