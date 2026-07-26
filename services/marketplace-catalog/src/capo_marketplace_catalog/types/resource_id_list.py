"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResourceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resource_id

ResourceIdList: TypeAlias = list[
    "capo_marketplace_catalog.types.resource_id.ResourceId"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceIdList:
    return list(data)
