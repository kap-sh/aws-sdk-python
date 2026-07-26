"""Generated from Smithy shape ``com.amazonaws.lakeformation#ResourceInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.resource_info

ResourceInfoList: TypeAlias = list[
    "capo_lakeformation.types.resource_info.ResourceInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceInfoList) -> list:
    import capo_lakeformation.types.resource_info

    out: list = []
    for item in value:
        out.append(capo_lakeformation.types.resource_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceInfoList:
    import capo_lakeformation.types.resource_info

    out: ResourceInfoList = []
    for item in data:
        out.append(capo_lakeformation.types.resource_info.deserialize_json(item))
    return out
