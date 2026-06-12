"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceTypeValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.resource_type_value

ResourceTypeValueList: TypeAlias = list[
    "aws_sdk_config_service.types.resource_type_value.ResourceTypeValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTypeValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceTypeValueList:
    return list(data)
