"""Generated from Smithy shape ``com.amazonaws.ecs#AcceleratorManufacturer``."""

from typing import Literal, TypeAlias, cast

AcceleratorManufacturer: TypeAlias = Literal[
    "amazon-web-services",
    "amd",
    "nvidia",
    "xilinx",
    "habana",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceleratorManufacturer) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcceleratorManufacturer:
    return cast(AcceleratorManufacturer, data)
