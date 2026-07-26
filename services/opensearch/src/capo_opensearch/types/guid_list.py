"""Generated from Smithy shape ``com.amazonaws.opensearch#GUIDList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.guid

GUIDList: TypeAlias = list["capo_opensearch.types.guid.GUID"]


# --- restJson1 ser/de ---
def serialize_json(value: GUIDList) -> list:
    return list(value)


def deserialize_json(data: list) -> GUIDList:
    return list(data)
