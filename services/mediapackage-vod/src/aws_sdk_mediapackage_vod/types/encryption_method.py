"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#EncryptionMethod``."""

from typing import Literal, TypeAlias, cast

EncryptionMethod: TypeAlias = Literal[
    "AES_128",
    "SAMPLE_AES",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionMethod) -> str:
    return value


def deserialize_json(data: str) -> EncryptionMethod:
    return cast(EncryptionMethod, data)
