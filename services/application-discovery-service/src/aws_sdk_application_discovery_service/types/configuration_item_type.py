"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ConfigurationItemType``."""

from typing import Literal, TypeAlias, cast

ConfigurationItemType: TypeAlias = Literal[
    "SERVER",
    "PROCESS",
    "CONNECTION",
    "APPLICATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationItemType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfigurationItemType:
    return cast(ConfigurationItemType, data)
