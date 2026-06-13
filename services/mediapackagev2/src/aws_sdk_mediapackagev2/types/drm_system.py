"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DrmSystem``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

DrmSystem: TypeAlias = Literal[
    "CLEAR_KEY_AES_128",
    "FAIRPLAY",
    "PLAYREADY",
    "WIDEVINE",
    "IRDETO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLEAR_KEY_AES_128",
        "FAIRPLAY",
        "PLAYREADY",
        "WIDEVINE",
        "IRDETO",
    )
)


def serialize_json(value: DrmSystem) -> str:
    return value


def deserialize_json(data: str) -> DrmSystem:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DrmSystem value: {data!r}")
    return cast(DrmSystem, data)
