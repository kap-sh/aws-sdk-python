"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationRecorderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.configuration_recorder

ConfigurationRecorderList: TypeAlias = list[
    "aws_sdk_config_service.types.configuration_recorder.ConfigurationRecorder"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationRecorderList) -> list:
    import aws_sdk_config_service.types.configuration_recorder

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.configuration_recorder.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConfigurationRecorderList:
    import aws_sdk_config_service.types.configuration_recorder

    out: ConfigurationRecorderList = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.configuration_recorder.deserialize_aws_json_1_1(
                item
            )
        )
    return out
