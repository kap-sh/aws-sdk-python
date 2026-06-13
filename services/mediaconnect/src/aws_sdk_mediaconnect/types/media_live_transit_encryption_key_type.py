"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaLiveTransitEncryptionKeyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

MediaLiveTransitEncryptionKeyType: TypeAlias = Literal[
    "SECRETS_MANAGER",
    "AUTOMATIC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SECRETS_MANAGER",
        "AUTOMATIC",
    )
)


def serialize_json(value: MediaLiveTransitEncryptionKeyType) -> str:
    return value


def deserialize_json(data: str) -> MediaLiveTransitEncryptionKeyType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MediaLiveTransitEncryptionKeyType value: {data!r}"
        )
    return cast(MediaLiveTransitEncryptionKeyType, data)
