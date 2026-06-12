"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ScalingPlanStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling_plans.errors import DeserializationError

ScalingPlanStatusCode: TypeAlias = Literal[
    "Active",
    "ActiveWithProblems",
    "CreationInProgress",
    "CreationFailed",
    "DeletionInProgress",
    "DeletionFailed",
    "UpdateInProgress",
    "UpdateFailed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "ActiveWithProblems",
        "CreationInProgress",
        "CreationFailed",
        "DeletionInProgress",
        "DeletionFailed",
        "UpdateInProgress",
        "UpdateFailed",
    )
)


def serialize_aws_json_1_1(value: ScalingPlanStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalingPlanStatusCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScalingPlanStatusCode value: {data!r}")
    return cast(ScalingPlanStatusCode, data)
