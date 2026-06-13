"""Generated from Smithy shape ``com.amazonaws.dsql#EncryptionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dsql.errors import DeserializationError

EncryptionStatus: TypeAlias = Literal[
    "ENABLED",
    "UPDATING",
    "KMS_KEY_INACCESSIBLE",
    "ENABLING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "UPDATING",
        "KMS_KEY_INACCESSIBLE",
        "ENABLING",
    )
)


def serialize_json(value: EncryptionStatus) -> str:
    return value


def deserialize_json(data: str) -> EncryptionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionStatus value: {data!r}")
    return cast(EncryptionStatus, data)
