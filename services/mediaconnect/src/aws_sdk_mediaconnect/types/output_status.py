"""Generated from Smithy shape ``com.amazonaws.mediaconnect#OutputStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

OutputStatus: TypeAlias = Literal[
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


def serialize_json(value: OutputStatus) -> str:
    return value


def deserialize_json(data: str) -> OutputStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OutputStatus value: {data!r}")
    return cast(OutputStatus, data)
