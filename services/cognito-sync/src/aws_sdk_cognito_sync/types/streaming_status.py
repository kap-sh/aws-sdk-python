"""Generated from Smithy shape ``com.amazonaws.cognitosync#StreamingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_sync.errors import DeserializationError

StreamingStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: StreamingStatus) -> str:
    return value


def deserialize_json(data: str) -> StreamingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StreamingStatus value: {data!r}")
    return cast(StreamingStatus, data)
