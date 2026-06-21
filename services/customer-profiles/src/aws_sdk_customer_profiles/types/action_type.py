"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ActionType``."""

from typing import Literal, TypeAlias, cast

ActionType: TypeAlias = Literal[
    "ADDED_PROFILE_KEY",
    "DELETED_PROFILE_KEY",
    "CREATED",
    "UPDATED",
    "INGESTED",
    "DELETED_BY_CUSTOMER",
    "EXPIRED",
    "MERGED",
    "DELETED_BY_MERGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionType) -> str:
    return value


def deserialize_json(data: str) -> ActionType:
    return cast(ActionType, data)
