"""Generated from Smithy shape ``com.amazonaws.wickr#DataRetentionActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wickr.errors import DeserializationError

DataRetentionActionType: TypeAlias = Literal[
    "ENABLE",
    "DISABLE",
    "PUBKEY_MSG_ACK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLE",
        "DISABLE",
        "PUBKEY_MSG_ACK",
    )
)


def serialize_json(value: DataRetentionActionType) -> str:
    return value


def deserialize_json(data: str) -> DataRetentionActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataRetentionActionType value: {data!r}")
    return cast(DataRetentionActionType, data)
