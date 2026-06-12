"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#VideoAspectRatio``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ivs_realtime.errors import DeserializationError

VideoAspectRatio: TypeAlias = Literal[
    "AUTO",
    "VIDEO",
    "SQUARE",
    "PORTRAIT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "VIDEO",
        "SQUARE",
        "PORTRAIT",
    )
)


def serialize_json(value: VideoAspectRatio) -> str:
    return value


def deserialize_json(data: str) -> VideoAspectRatio:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VideoAspectRatio value: {data!r}")
    return cast(VideoAspectRatio, data)
