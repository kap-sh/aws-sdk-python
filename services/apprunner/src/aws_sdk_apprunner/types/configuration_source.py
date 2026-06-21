"""Generated from Smithy shape ``com.amazonaws.apprunner#ConfigurationSource``."""

from typing import Literal, TypeAlias, cast

ConfigurationSource: TypeAlias = Literal[
    "REPOSITORY",
    "API",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConfigurationSource) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConfigurationSource:
    return cast(ConfigurationSource, data)
