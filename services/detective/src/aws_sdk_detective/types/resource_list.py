"""Generated from Smithy shape ``com.amazonaws.detective#ResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_detective.types.resource

ResourceList: TypeAlias = list["aws_sdk_detective.types.resource.Resource"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceList:
    return list(data)
