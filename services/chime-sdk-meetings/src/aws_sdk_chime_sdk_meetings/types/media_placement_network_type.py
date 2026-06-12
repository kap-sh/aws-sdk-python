"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#MediaPlacementNetworkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_meetings.errors import DeserializationError

MediaPlacementNetworkType: TypeAlias = Literal[
    "Ipv4Only",
    "DualStack",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Ipv4Only",
        "DualStack",
    )
)


def serialize_json(value: MediaPlacementNetworkType) -> str:
    return value


def deserialize_json(data: str) -> MediaPlacementNetworkType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MediaPlacementNetworkType value: {data!r}")
    return cast(MediaPlacementNetworkType, data)
