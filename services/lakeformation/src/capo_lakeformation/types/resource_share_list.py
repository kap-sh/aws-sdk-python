"""Generated from Smithy shape ``com.amazonaws.lakeformation#ResourceShareList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.ram_resource_share_arn

ResourceShareList: TypeAlias = list[
    "capo_lakeformation.types.ram_resource_share_arn.RAMResourceShareArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceShareList:
    return list(data)
