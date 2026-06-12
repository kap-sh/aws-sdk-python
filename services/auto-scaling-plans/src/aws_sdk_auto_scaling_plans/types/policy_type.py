"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#PolicyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling_plans.errors import DeserializationError

PolicyType: TypeAlias = Literal["TargetTrackingScaling",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TargetTrackingScaling",))


def serialize_aws_json_1_1(value: PolicyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PolicyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PolicyType value: {data!r}")
    return cast(PolicyType, data)
