"""Generated from Smithy shape ``com.amazonaws.emr#AutoScalingPolicyStateChangeReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

AutoScalingPolicyStateChangeReasonCode: TypeAlias = Literal[
    "USER_REQUEST",
    "PROVISION_FAILURE",
    "CLEANUP_FAILURE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER_REQUEST",
        "PROVISION_FAILURE",
        "CLEANUP_FAILURE",
    )
)


def serialize_aws_json_1_1(value: AutoScalingPolicyStateChangeReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoScalingPolicyStateChangeReasonCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutoScalingPolicyStateChangeReasonCode value: {data!r}"
        )
    return cast(AutoScalingPolicyStateChangeReasonCode, data)
