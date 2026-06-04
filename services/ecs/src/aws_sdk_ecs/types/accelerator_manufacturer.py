"""Generated from Smithy shape ``com.amazonaws.ecs#AcceleratorManufacturer``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

AcceleratorManufacturer: TypeAlias = Literal[
    "amazon-web-services",
    "amd",
    "nvidia",
    "xilinx",
    "habana",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "amazon-web-services",
        "amd",
        "nvidia",
        "xilinx",
        "habana",
    )
)


def serialize_aws_json_1_1(value: AcceleratorManufacturer) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcceleratorManufacturer:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AcceleratorManufacturer value: {data!r}")
    return cast(AcceleratorManufacturer, data)
