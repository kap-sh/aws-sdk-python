"""Generated from Smithy shape ``com.amazonaws.wickr#DataRetentionActionType``."""

from typing import Literal, TypeAlias, cast

DataRetentionActionType: TypeAlias = Literal[
    "ENABLE",
    "DISABLE",
    "PUBKEY_MSG_ACK",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataRetentionActionType) -> str:
    return value


def deserialize_json(data: str) -> DataRetentionActionType:
    return cast(DataRetentionActionType, data)
