"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputTransitEncryptionKeyType``."""

from typing import Literal, TypeAlias, cast

RouterInputTransitEncryptionKeyType: TypeAlias = Literal[
    "SECRETS_MANAGER",
    "AUTOMATIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputTransitEncryptionKeyType) -> str:
    return value


def deserialize_json(data: str) -> RouterInputTransitEncryptionKeyType:
    return cast(RouterInputTransitEncryptionKeyType, data)
