"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafEncryptionType``."""

from typing import Literal, TypeAlias, cast

"""Specify the encryption scheme that you want the service to use when encrypting your CMAF segments. Choose AES-CBC subsample or AES_CTR."""
CmafEncryptionType: TypeAlias = Literal[
    "SAMPLE_AES",
    "AES_CTR",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafEncryptionType) -> str:
    return value


def deserialize_json(data: str) -> CmafEncryptionType:
    return cast(CmafEncryptionType, data)
