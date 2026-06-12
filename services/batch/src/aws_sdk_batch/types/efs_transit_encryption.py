"""Generated from Smithy shape ``com.amazonaws.batch#EFSTransitEncryption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

EFSTransitEncryption: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: EFSTransitEncryption) -> str:
    return value


def deserialize_json(data: str) -> EFSTransitEncryption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EFSTransitEncryption value: {data!r}")
    return cast(EFSTransitEncryption, data)
