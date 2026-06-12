"""Generated from Smithy shape ``com.amazonaws.sagemaker#ReservedCapacityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ReservedCapacityType: TypeAlias = Literal[
    "UltraServer",
    "Instance",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UltraServer",
        "Instance",
    )
)


def serialize_aws_json_1_1(value: ReservedCapacityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReservedCapacityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReservedCapacityType value: {data!r}")
    return cast(ReservedCapacityType, data)
