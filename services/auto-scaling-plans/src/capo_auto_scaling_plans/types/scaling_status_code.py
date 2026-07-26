"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ScalingStatusCode``."""

from typing import Literal, TypeAlias, cast

ScalingStatusCode: TypeAlias = Literal[
    "Inactive",
    "PartiallyActive",
    "Active",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalingStatusCode:
    return cast(ScalingStatusCode, data)
