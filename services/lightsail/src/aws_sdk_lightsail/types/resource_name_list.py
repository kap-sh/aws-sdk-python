"""Generated from Smithy shape ``com.amazonaws.lightsail#ResourceNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name

ResourceNameList: TypeAlias = list["aws_sdk_lightsail.types.resource_name.ResourceName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceNameList:
    return list(data)
