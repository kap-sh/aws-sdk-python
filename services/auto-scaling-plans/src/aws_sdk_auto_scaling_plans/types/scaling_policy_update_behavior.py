"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ScalingPolicyUpdateBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling_plans.errors import DeserializationError

ScalingPolicyUpdateBehavior: TypeAlias = Literal[
    "KeepExternalPolicies",
    "ReplaceExternalPolicies",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KeepExternalPolicies",
        "ReplaceExternalPolicies",
    )
)


def serialize_aws_json_1_1(value: ScalingPolicyUpdateBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalingPolicyUpdateBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ScalingPolicyUpdateBehavior value: {data!r}"
        )
    return cast(ScalingPolicyUpdateBehavior, data)
