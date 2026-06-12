"""Generated from Smithy shape ``com.amazonaws.medialive#MediaConnectRouterOutputEncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Encryption configuration for MediaConnect router. When using SECRETS_MANAGER encryption, you must provide the ARN of the secret used to encrypt data in transit. When using AUTOMATIC encryption, a service-managed secret will be used instead."""
MediaConnectRouterOutputEncryptionType: TypeAlias = Literal[
    "AUTOMATIC",
    "SECRETS_MANAGER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTOMATIC",
        "SECRETS_MANAGER",
    )
)


def serialize_json(value: MediaConnectRouterOutputEncryptionType) -> str:
    return value


def deserialize_json(data: str) -> MediaConnectRouterOutputEncryptionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MediaConnectRouterOutputEncryptionType value: {data!r}"
        )
    return cast(MediaConnectRouterOutputEncryptionType, data)
