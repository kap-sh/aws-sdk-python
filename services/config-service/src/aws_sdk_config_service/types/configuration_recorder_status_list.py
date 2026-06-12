"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationRecorderStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.configuration_recorder_status

ConfigurationRecorderStatusList: TypeAlias = list[
    "aws_sdk_config_service.types.configuration_recorder_status.ConfigurationRecorderStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationRecorderStatusList) -> list:
    import aws_sdk_config_service.types.configuration_recorder_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.configuration_recorder_status.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConfigurationRecorderStatusList:
    import aws_sdk_config_service.types.configuration_recorder_status

    out: ConfigurationRecorderStatusList = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.configuration_recorder_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
