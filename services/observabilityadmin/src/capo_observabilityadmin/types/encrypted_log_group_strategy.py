"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#EncryptedLogGroupStrategy``."""

from typing import Literal, TypeAlias, cast

EncryptedLogGroupStrategy: TypeAlias = Literal[
    "ALLOW",
    "SKIP",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptedLogGroupStrategy) -> str:
    return value


def deserialize_json(data: str) -> EncryptedLogGroupStrategy:
    return cast(EncryptedLogGroupStrategy, data)
