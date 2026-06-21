"""Generated from Smithy shape ``com.amazonaws.ecs#CpuManufacturer``."""

from typing import Literal, TypeAlias, cast

CpuManufacturer: TypeAlias = Literal[
    "intel",
    "amd",
    "amazon-web-services",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CpuManufacturer) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CpuManufacturer:
    return cast(CpuManufacturer, data)
