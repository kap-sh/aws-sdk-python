"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationRecorderFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.configuration_recorder_filter_value

ConfigurationRecorderFilterValues: TypeAlias = list[
    "capo_config_service.types.configuration_recorder_filter_value.ConfigurationRecorderFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationRecorderFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ConfigurationRecorderFilterValues:
    return list(data)
