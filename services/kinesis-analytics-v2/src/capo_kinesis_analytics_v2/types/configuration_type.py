"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ConfigurationType``."""

from typing import Literal, TypeAlias, cast

ConfigurationType: TypeAlias = Literal[
    "DEFAULT",
    "CUSTOM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfigurationType:
    return cast(ConfigurationType, data)
