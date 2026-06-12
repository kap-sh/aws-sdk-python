"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafEncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the encryption scheme that you want the service to use when encrypting your CMAF segments. Choose AES-CBC subsample or AES_CTR."""
CmafEncryptionType: TypeAlias = Literal[
    "SAMPLE_AES",
    "AES_CTR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SAMPLE_AES",
        "AES_CTR",
    )
)


def serialize_json(value: CmafEncryptionType) -> str:
    return value


def deserialize_json(data: str) -> CmafEncryptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CmafEncryptionType value: {data!r}")
    return cast(CmafEncryptionType, data)
