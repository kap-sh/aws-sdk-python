"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaLiveTransitEncryptionKeyType``."""

from typing import Literal, TypeAlias, cast

MediaLiveTransitEncryptionKeyType: TypeAlias = Literal[
    "SECRETS_MANAGER",
    "AUTOMATIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaLiveTransitEncryptionKeyType) -> str:
    return value


def deserialize_json(data: str) -> MediaLiveTransitEncryptionKeyType:
    return cast(MediaLiveTransitEncryptionKeyType, data)
