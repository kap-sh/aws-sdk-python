"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrafficType``."""

from typing import Literal, TypeAlias, cast

TrafficType: TypeAlias = Literal[
    "PHASES",
    "STAIRS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrafficType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrafficType:
    return cast(TrafficType, data)
