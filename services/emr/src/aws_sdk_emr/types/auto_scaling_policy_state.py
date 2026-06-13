"""Generated from Smithy shape ``com.amazonaws.emr#AutoScalingPolicyState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

AutoScalingPolicyState: TypeAlias = Literal[
    "PENDING",
    "ATTACHING",
    "ATTACHED",
    "DETACHING",
    "DETACHED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "ATTACHING",
        "ATTACHED",
        "DETACHING",
        "DETACHED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: AutoScalingPolicyState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoScalingPolicyState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoScalingPolicyState value: {data!r}")
    return cast(AutoScalingPolicyState, data)
