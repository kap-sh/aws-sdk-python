"""Generated from Smithy shape ``com.amazonaws.entityresolution#DisconnectedUniqueIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_entityresolution.types.header_safe_unique_id

DisconnectedUniqueIdsList: TypeAlias = list[
    "capo_entityresolution.types.header_safe_unique_id.HeaderSafeUniqueId"
]


# --- restJson1 ser/de ---
def serialize_json(value: DisconnectedUniqueIdsList) -> list:
    return list(value)


def deserialize_json(data: list) -> DisconnectedUniqueIdsList:
    return list(data)
