"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#GUIDList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.guid

GUIDList: TypeAlias = list["capo_elasticsearch_service.types.guid.GUID"]


# --- restJson1 ser/de ---
def serialize_json(value: GUIDList) -> list:
    return list(value)


def deserialize_json(data: list) -> GUIDList:
    return list(data)
