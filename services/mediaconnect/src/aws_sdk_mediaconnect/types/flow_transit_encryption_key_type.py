"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FlowTransitEncryptionKeyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

FlowTransitEncryptionKeyType: TypeAlias = Literal[
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


def serialize_json(value: FlowTransitEncryptionKeyType) -> str:
    return value


def deserialize_json(data: str) -> FlowTransitEncryptionKeyType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FlowTransitEncryptionKeyType value: {data!r}"
        )
    return cast(FlowTransitEncryptionKeyType, data)
