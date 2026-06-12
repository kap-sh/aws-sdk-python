"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#Profile``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackage_vod.errors import DeserializationError

Profile: TypeAlias = Literal[
    "NONE",
    "HBBTV_1_5",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "HBBTV_1_5",
    )
)


def serialize_json(value: Profile) -> str:
    return value


def deserialize_json(data: str) -> Profile:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Profile value: {data!r}")
    return cast(Profile, data)
