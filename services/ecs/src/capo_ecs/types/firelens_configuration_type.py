"""Generated from Smithy shape ``com.amazonaws.ecs#FirelensConfigurationType``."""

from typing import Literal, TypeAlias, cast

FirelensConfigurationType: TypeAlias = Literal[
    "fluentd",
    "fluentbit",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirelensConfigurationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FirelensConfigurationType:
    return cast(FirelensConfigurationType, data)
