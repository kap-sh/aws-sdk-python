"""Generated from Smithy shape ``com.amazonaws.lambda#LogFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

LogFormat: TypeAlias = Literal[
    "JSON",
    "Text",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JSON",
        "Text",
    )
)


def serialize_json(value: LogFormat) -> str:
    return value


def deserialize_json(data: str) -> LogFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogFormat value: {data!r}")
    return cast(LogFormat, data)
