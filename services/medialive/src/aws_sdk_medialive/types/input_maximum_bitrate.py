"""Generated from Smithy shape ``com.amazonaws.medialive#InputMaximumBitrate``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Maximum input bitrate in megabits per second. Bitrates up to 50 Mbps are supported currently."""
InputMaximumBitrate: TypeAlias = Literal[
    "MAX_10_MBPS",
    "MAX_20_MBPS",
    "MAX_50_MBPS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MAX_10_MBPS",
        "MAX_20_MBPS",
        "MAX_50_MBPS",
    )
)


def serialize_json(value: InputMaximumBitrate) -> str:
    return value


def deserialize_json(data: str) -> InputMaximumBitrate:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputMaximumBitrate value: {data!r}")
    return cast(InputMaximumBitrate, data)
