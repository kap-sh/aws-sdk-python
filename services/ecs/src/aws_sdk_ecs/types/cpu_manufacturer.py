"""Generated from Smithy shape ``com.amazonaws.ecs#CpuManufacturer``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

CpuManufacturer: TypeAlias = Literal[
    "intel",
    "amd",
    "amazon-web-services",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "intel",
        "amd",
        "amazon-web-services",
    )
)


def serialize_aws_json_1_1(value: CpuManufacturer) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CpuManufacturer:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CpuManufacturer value: {data!r}")
    return cast(CpuManufacturer, data)
