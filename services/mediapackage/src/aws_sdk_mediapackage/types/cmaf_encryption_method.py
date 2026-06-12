"""Generated from Smithy shape ``com.amazonaws.mediapackage#CmafEncryptionMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackage.errors import DeserializationError

"""The encryption method to use."""
CmafEncryptionMethod: TypeAlias = Literal[
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


def serialize_json(value: CmafEncryptionMethod) -> str:
    return value


def deserialize_json(data: str) -> CmafEncryptionMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CmafEncryptionMethod value: {data!r}")
    return cast(CmafEncryptionMethod, data)
