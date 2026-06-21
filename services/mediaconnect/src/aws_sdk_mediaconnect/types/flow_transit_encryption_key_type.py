"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FlowTransitEncryptionKeyType``."""

from typing import Literal, TypeAlias, cast

FlowTransitEncryptionKeyType: TypeAlias = Literal[
    "SECRETS_MANAGER",
    "AUTOMATIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowTransitEncryptionKeyType) -> str:
    return value


def deserialize_json(data: str) -> FlowTransitEncryptionKeyType:
    return cast(FlowTransitEncryptionKeyType, data)
