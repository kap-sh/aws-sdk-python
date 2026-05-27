"""Generated from Smithy shape ``com.amazonaws.lambda#InvokeMode``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_lambda.errors import DeserializationError

InvokeMode: TypeAlias = Literal[
    "BUFFERED",
    "RESPONSE_STREAM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BUFFERED",
        "RESPONSE_STREAM",
    )
)


def serialize_json(value: InvokeMode) -> str:
    return value


def deserialize_json(data: str) -> InvokeMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InvokeMode value: {data!r}")
    return cast(InvokeMode, data)
