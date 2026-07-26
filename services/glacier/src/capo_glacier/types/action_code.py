"""Generated from Smithy shape ``com.amazonaws.glacier#ActionCode``."""

from typing import Literal, TypeAlias, cast

ActionCode: TypeAlias = Literal[
    "ArchiveRetrieval",
    "InventoryRetrieval",
    "Select",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionCode) -> str:
    return value


def deserialize_json(data: str) -> ActionCode:
    return cast(ActionCode, data)
