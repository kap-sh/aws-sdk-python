"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputTransitEncryptionKeyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

RouterInputTransitEncryptionKeyType: TypeAlias = Literal[
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


def serialize_json(value: RouterInputTransitEncryptionKeyType) -> str:
    return value


def deserialize_json(data: str) -> RouterInputTransitEncryptionKeyType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouterInputTransitEncryptionKeyType value: {data!r}"
        )
    return cast(RouterInputTransitEncryptionKeyType, data)
