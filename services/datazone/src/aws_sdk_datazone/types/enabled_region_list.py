"""Generated from Smithy shape ``com.amazonaws.datazone#EnabledRegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.region_name

EnabledRegionList: TypeAlias = list["aws_sdk_datazone.types.region_name.RegionName"]


# --- restJson1 ser/de ---
def serialize_json(value: EnabledRegionList) -> list:
    return list(value)


def deserialize_json(data: list) -> EnabledRegionList:
    return list(data)
