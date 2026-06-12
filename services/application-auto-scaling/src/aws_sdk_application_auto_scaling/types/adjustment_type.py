"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#AdjustmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_auto_scaling.errors import DeserializationError

AdjustmentType: TypeAlias = Literal[
    "ChangeInCapacity",
    "PercentChangeInCapacity",
    "ExactCapacity",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ChangeInCapacity",
        "PercentChangeInCapacity",
        "ExactCapacity",
    )
)


def serialize_aws_json_1_1(value: AdjustmentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AdjustmentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AdjustmentType value: {data!r}")
    return cast(AdjustmentType, data)
