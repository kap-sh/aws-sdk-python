"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#EncryptionStrategy``."""

from typing import Literal, TypeAlias, cast

EncryptionStrategy: TypeAlias = Literal[
    "CUSTOMER_MANAGED",
    "AWS_OWNED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionStrategy) -> str:
    return value


def deserialize_json(data: str) -> EncryptionStrategy:
    return cast(EncryptionStrategy, data)
