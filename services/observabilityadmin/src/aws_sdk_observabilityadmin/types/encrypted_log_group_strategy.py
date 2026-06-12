"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#EncryptedLogGroupStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_observabilityadmin.errors import DeserializationError

EncryptedLogGroupStrategy: TypeAlias = Literal[
    "ALLOW",
    "SKIP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "SKIP",
    )
)


def serialize_json(value: EncryptedLogGroupStrategy) -> str:
    return value


def deserialize_json(data: str) -> EncryptedLogGroupStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptedLogGroupStrategy value: {data!r}")
    return cast(EncryptedLogGroupStrategy, data)
