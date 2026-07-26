"""Generated from Smithy shape ``com.amazonaws.medialive#RouterEncryptionType``."""

from typing import Literal, TypeAlias, cast

"""Encryption configuration for MediaConnect router. When using SECRETS_MANAGER encryption, you must provide the ARN of the secret used to encrypt data in transit. When using AUTOMATIC encryption, a service-managed secret will be used instead."""
RouterEncryptionType: TypeAlias = Literal[
    "AUTOMATIC",
    "SECRETS_MANAGER",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterEncryptionType) -> str:
    return value


def deserialize_json(data: str) -> RouterEncryptionType:
    return cast(RouterEncryptionType, data)
