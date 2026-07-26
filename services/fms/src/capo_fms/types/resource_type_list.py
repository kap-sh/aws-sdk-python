"""Generated from Smithy shape ``com.amazonaws.fms#ResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.resource_type

ResourceTypeList: TypeAlias = list["capo_fms.types.resource_type.ResourceType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTypeList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceTypeList:
    return list(data)
