"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsOfflineEncrypted``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Enable this setting to insert the EXT-X-SESSION-KEY element into the master playlist. This allows for offline Apple HLS FairPlay content protection."""
HlsOfflineEncrypted: TypeAlias = Literal[
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


def serialize_json(value: HlsOfflineEncrypted) -> str:
    return value


def deserialize_json(data: str) -> HlsOfflineEncrypted:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsOfflineEncrypted value: {data!r}")
    return cast(HlsOfflineEncrypted, data)
