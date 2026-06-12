"""Generated from Smithy shape ``com.amazonaws.gamelift#ScalingAdjustmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

ScalingAdjustmentType: TypeAlias = Literal[
    "ChangeInCapacity",
    "ExactCapacity",
    "PercentChangeInCapacity",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ChangeInCapacity",
        "ExactCapacity",
        "PercentChangeInCapacity",
    )
)


def serialize_aws_json_1_1(value: ScalingAdjustmentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalingAdjustmentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScalingAdjustmentType value: {data!r}")
    return cast(ScalingAdjustmentType, data)
