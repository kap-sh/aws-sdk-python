"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationRecorderFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.configuration_recorder_filter

ConfigurationRecorderFilterList: TypeAlias = list[
    "aws_sdk_config_service.types.configuration_recorder_filter.ConfigurationRecorderFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationRecorderFilterList) -> list:
    import aws_sdk_config_service.types.configuration_recorder_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.configuration_recorder_filter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConfigurationRecorderFilterList:
    import aws_sdk_config_service.types.configuration_recorder_filter

    out: ConfigurationRecorderFilterList = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.configuration_recorder_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
