"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#TsEncryptionMethod``."""

from typing import Literal, TypeAlias, cast

TsEncryptionMethod: TypeAlias = Literal[
    "AES_128",
    "SAMPLE_AES",
]


# --- restJson1 ser/de ---
def serialize_json(value: TsEncryptionMethod) -> str:
    return value


def deserialize_json(data: str) -> TsEncryptionMethod:
    return cast(TsEncryptionMethod, data)
