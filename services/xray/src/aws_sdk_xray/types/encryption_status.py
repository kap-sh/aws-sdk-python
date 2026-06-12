"""Generated from Smithy shape ``com.amazonaws.xray#EncryptionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_xray.errors import DeserializationError

EncryptionStatus: TypeAlias = Literal[
    "UPDATING",
    "ACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UPDATING",
        "ACTIVE",
    )
)


def serialize_json(value: EncryptionStatus) -> str:
    return value


def deserialize_json(data: str) -> EncryptionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionStatus value: {data!r}")
    return cast(EncryptionStatus, data)
