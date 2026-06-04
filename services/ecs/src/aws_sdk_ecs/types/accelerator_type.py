"""Generated from Smithy shape ``com.amazonaws.ecs#AcceleratorType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

AcceleratorType: TypeAlias = Literal[
    "gpu",
    "fpga",
    "inference",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "gpu",
        "fpga",
        "inference",
    )
)


def serialize_aws_json_1_1(value: AcceleratorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcceleratorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AcceleratorType value: {data!r}")
    return cast(AcceleratorType, data)
