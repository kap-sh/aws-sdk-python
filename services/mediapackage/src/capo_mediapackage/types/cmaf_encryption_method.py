"""Generated from Smithy shape ``com.amazonaws.mediapackage#CmafEncryptionMethod``."""

from typing import Literal, TypeAlias, cast

"""The encryption method to use."""
CmafEncryptionMethod: TypeAlias = Literal[
    "SAMPLE_AES",
    "AES_CTR",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafEncryptionMethod) -> str:
    return value


def deserialize_json(data: str) -> CmafEncryptionMethod:
    return cast(CmafEncryptionMethod, data)
