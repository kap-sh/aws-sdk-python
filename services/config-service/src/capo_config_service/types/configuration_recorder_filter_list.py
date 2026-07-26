"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationRecorderFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.configuration_recorder_filter

ConfigurationRecorderFilterList: TypeAlias = list[
    "capo_config_service.types.configuration_recorder_filter.ConfigurationRecorderFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationRecorderFilterList) -> list:
    import capo_config_service.types.configuration_recorder_filter

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.configuration_recorder_filter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConfigurationRecorderFilterList:
    import capo_config_service.types.configuration_recorder_filter

    out: ConfigurationRecorderFilterList = []
    for item in data:
        out.append(
            capo_config_service.types.configuration_recorder_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
