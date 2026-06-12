"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#ContentResolution``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_meetings.errors import DeserializationError

ContentResolution: TypeAlias = Literal[
    "None",
    "FHD",
    "UHD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "None",
        "FHD",
        "UHD",
    )
)


def serialize_json(value: ContentResolution) -> str:
    return value


def deserialize_json(data: str) -> ContentResolution:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentResolution value: {data!r}")
    return cast(ContentResolution, data)
