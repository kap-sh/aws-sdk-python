"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

RouterOutputType: TypeAlias = Literal[
    "STANDARD",
    "MEDIACONNECT_FLOW",
    "MEDIALIVE_INPUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "MEDIACONNECT_FLOW",
        "MEDIALIVE_INPUT",
    )
)


def serialize_json(value: RouterOutputType) -> str:
    return value


def deserialize_json(data: str) -> RouterOutputType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouterOutputType value: {data!r}")
    return cast(RouterOutputType, data)
