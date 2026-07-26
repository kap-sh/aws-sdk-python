"""Generated from Smithy shape ``com.amazonaws.opensearch#RegionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.region

RegionsList: TypeAlias = list["capo_opensearch.types.region.Region"]


# --- restJson1 ser/de ---
def serialize_json(value: RegionsList) -> list:
    return list(value)


def deserialize_json(data: list) -> RegionsList:
    return list(data)
