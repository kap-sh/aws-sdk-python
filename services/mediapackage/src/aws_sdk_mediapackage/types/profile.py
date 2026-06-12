"""Generated from Smithy shape ``com.amazonaws.mediapackage#Profile``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackage.errors import DeserializationError

Profile: TypeAlias = Literal[
    "NONE",
    "HBBTV_1_5",
    "HYBRIDCAST",
    "DVB_DASH_2014",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "HBBTV_1_5",
        "HYBRIDCAST",
        "DVB_DASH_2014",
    )
)


def serialize_json(value: Profile) -> str:
    return value


def deserialize_json(data: str) -> Profile:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Profile value: {data!r}")
    return cast(Profile, data)
