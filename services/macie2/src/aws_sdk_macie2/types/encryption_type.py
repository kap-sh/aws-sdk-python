"""Generated from Smithy shape ``com.amazonaws.macie2#EncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The server-side encryption algorithm that was used to encrypt an S3 object or is used by default to encrypt objects that are added to an S3 bucket. Possible values are:</p>"""
EncryptionType: TypeAlias = Literal[
    "NONE",
    "AES256",
    "aws:kms",
    "UNKNOWN",
    "aws:kms:dsse",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "AES256",
        "aws:kms",
        "UNKNOWN",
        "aws:kms:dsse",
    )
)


def serialize_json(value: EncryptionType) -> str:
    return value


def deserialize_json(data: str) -> EncryptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionType value: {data!r}")
    return cast(EncryptionType, data)
