"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ShareStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

ShareStatus: TypeAlias = Literal[
    "NOT_SHARED",
    "INITIATED",
    "SHARED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_SHARED",
        "INITIATED",
        "SHARED",
    )
)


def serialize_json(value: ShareStatus) -> str:
    return value


def deserialize_json(data: str) -> ShareStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShareStatus value: {data!r}")
    return cast(ShareStatus, data)
