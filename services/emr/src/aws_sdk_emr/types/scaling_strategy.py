"""Generated from Smithy shape ``com.amazonaws.emr#ScalingStrategy``."""

from typing import Literal, TypeAlias, cast

ScalingStrategy: TypeAlias = Literal[
    "DEFAULT",
    "ADVANCED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalingStrategy:
    return cast(ScalingStrategy, data)
