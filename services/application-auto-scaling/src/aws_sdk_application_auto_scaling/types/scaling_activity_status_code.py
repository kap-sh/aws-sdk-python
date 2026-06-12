"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#ScalingActivityStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_auto_scaling.errors import DeserializationError

ScalingActivityStatusCode: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Successful",
    "Overridden",
    "Unfulfilled",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "InProgress",
        "Successful",
        "Overridden",
        "Unfulfilled",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: ScalingActivityStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalingActivityStatusCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScalingActivityStatusCode value: {data!r}")
    return cast(ScalingActivityStatusCode, data)
