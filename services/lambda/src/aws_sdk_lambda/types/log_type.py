"""Generated from Smithy shape ``com.amazonaws.lambda#LogType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_lambda.errors import DeserializationError

LogType: TypeAlias = Literal[
    "None",
    "Tail",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "None",
        "Tail",
    )
)


def serialize_json(value: LogType) -> str:
    return value


def deserialize_json(data: str) -> LogType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogType value: {data!r}")
    return cast(LogType, data)
