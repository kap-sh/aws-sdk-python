"""Generated from Smithy shape ``com.amazonaws.configservice#RetentionConfigurationNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.retention_configuration_name

RetentionConfigurationNameList: TypeAlias = list[
    "aws_sdk_config_service.types.retention_configuration_name.RetentionConfigurationName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetentionConfigurationNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RetentionConfigurationNameList:
    return list(data)
