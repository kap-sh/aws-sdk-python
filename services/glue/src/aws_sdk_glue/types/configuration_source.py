"""Generated from Smithy shape ``com.amazonaws.glue#ConfigurationSource``."""

from typing import Literal, TypeAlias, cast

ConfigurationSource: TypeAlias = Literal[
    "catalog",
    "table",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfigurationSource:
    return cast(ConfigurationSource, data)
