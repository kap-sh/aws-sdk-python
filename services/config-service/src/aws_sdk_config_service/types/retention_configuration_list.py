"""Generated from Smithy shape ``com.amazonaws.configservice#RetentionConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.retention_configuration

RetentionConfigurationList: TypeAlias = list[
    "aws_sdk_config_service.types.retention_configuration.RetentionConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetentionConfigurationList) -> list:
    import aws_sdk_config_service.types.retention_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.retention_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RetentionConfigurationList:
    import aws_sdk_config_service.types.retention_configuration

    out: RetentionConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.retention_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
