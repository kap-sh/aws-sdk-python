"""Generated from Smithy shape ``com.amazonaws.connect#ActiveRegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.region_name

ActiveRegionList: TypeAlias = list["capo_connect.types.region_name.RegionName"]


# --- restJson1 ser/de ---
def serialize_json(value: ActiveRegionList) -> list:
    return list(value)


def deserialize_json(data: list) -> ActiveRegionList:
    return list(data)
