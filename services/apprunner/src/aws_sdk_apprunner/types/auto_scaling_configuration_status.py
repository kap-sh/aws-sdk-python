"""Generated from Smithy shape ``com.amazonaws.apprunner#AutoScalingConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

AutoScalingConfigurationStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoScalingConfigurationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AutoScalingConfigurationStatus:
    return cast(AutoScalingConfigurationStatus, data)
