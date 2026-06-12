"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ram.types.resource_share

ResourceShareList: TypeAlias = list["aws_sdk_ram.types.resource_share.ResourceShare"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareList) -> list:
    import aws_sdk_ram.types.resource_share

    out: list = []
    for item in value:
        out.append(aws_sdk_ram.types.resource_share.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceShareList:
    import aws_sdk_ram.types.resource_share

    out: ResourceShareList = []
    for item in data:
        out.append(aws_sdk_ram.types.resource_share.deserialize_json(item))
    return out
