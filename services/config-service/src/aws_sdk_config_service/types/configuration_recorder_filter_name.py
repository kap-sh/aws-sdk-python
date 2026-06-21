"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationRecorderFilterName``."""

from typing import Literal, TypeAlias, cast

ConfigurationRecorderFilterName: TypeAlias = Literal["recordingScope",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationRecorderFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfigurationRecorderFilterName:
    return cast(ConfigurationRecorderFilterName, data)
