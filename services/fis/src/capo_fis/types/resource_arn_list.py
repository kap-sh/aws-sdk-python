"""Generated from Smithy shape ``com.amazonaws.fis#ResourceArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.resource_arn

ResourceArnList: TypeAlias = list["capo_fis.types.resource_arn.ResourceArn"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceArnList:
    return list(data)
