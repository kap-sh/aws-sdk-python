"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.resource_type

ResourceTypeList: TypeAlias = list[
    "aws_sdk_config_service.types.resource_type.ResourceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTypeList) -> list:
    import aws_sdk_config_service.types.resource_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.resource_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceTypeList:
    import aws_sdk_config_service.types.resource_type

    out: ResourceTypeList = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.resource_type.deserialize_aws_json_1_1(item)
        )
    return out
