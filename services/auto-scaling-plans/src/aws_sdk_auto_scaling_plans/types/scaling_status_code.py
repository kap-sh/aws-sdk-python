"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ScalingStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling_plans.errors import DeserializationError

ScalingStatusCode: TypeAlias = Literal[
    "Inactive",
    "PartiallyActive",
    "Active",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Inactive",
        "PartiallyActive",
        "Active",
    )
)


def serialize_aws_json_1_1(value: ScalingStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalingStatusCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScalingStatusCode value: {data!r}")
    return cast(ScalingStatusCode, data)
