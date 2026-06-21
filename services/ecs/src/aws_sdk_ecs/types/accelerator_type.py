"""Generated from Smithy shape ``com.amazonaws.ecs#AcceleratorType``."""

from typing import Literal, TypeAlias, cast

AcceleratorType: TypeAlias = Literal[
    "gpu",
    "fpga",
    "inference",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceleratorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcceleratorType:
    return cast(AcceleratorType, data)
