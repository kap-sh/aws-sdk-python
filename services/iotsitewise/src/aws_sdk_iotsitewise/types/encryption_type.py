"""Generated from Smithy shape ``com.amazonaws.iotsitewise#EncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

EncryptionType: TypeAlias = Literal[
    "SITEWISE_DEFAULT_ENCRYPTION",
    "KMS_BASED_ENCRYPTION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SITEWISE_DEFAULT_ENCRYPTION",
        "KMS_BASED_ENCRYPTION",
    )
)


def serialize_json(value: EncryptionType) -> str:
    return value


def deserialize_json(data: str) -> EncryptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionType value: {data!r}")
    return cast(EncryptionType, data)
