"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.resource_id

ResourceIdList: TypeAlias = list["aws_sdk_config_service.types.resource_id.ResourceId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceIdList:
    return list(data)
