"""Generated from Smithy shape ``com.amazonaws.sagemaker#CapacitySizeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

CapacitySizeType: TypeAlias = Literal[
    "INSTANCE_COUNT",
    "CAPACITY_PERCENT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSTANCE_COUNT",
        "CAPACITY_PERCENT",
    )
)


def serialize_aws_json_1_1(value: CapacitySizeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacitySizeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapacitySizeType value: {data!r}")
    return cast(CapacitySizeType, data)
