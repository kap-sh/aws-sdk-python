"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DrmSystem``."""

from typing import Literal, TypeAlias, cast

DrmSystem: TypeAlias = Literal[
    "CLEAR_KEY_AES_128",
    "FAIRPLAY",
    "PLAYREADY",
    "WIDEVINE",
    "IRDETO",
]


# --- restJson1 ser/de ---
def serialize_json(value: DrmSystem) -> str:
    return value


def deserialize_json(data: str) -> DrmSystem:
    return cast(DrmSystem, data)
