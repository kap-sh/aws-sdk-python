"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationRecorderNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.recorder_name

ConfigurationRecorderNameList: TypeAlias = list[
    "capo_config_service.types.recorder_name.RecorderName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationRecorderNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ConfigurationRecorderNameList:
    return list(data)
