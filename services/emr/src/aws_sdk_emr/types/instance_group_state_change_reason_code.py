"""Generated from Smithy shape ``com.amazonaws.emr#InstanceGroupStateChangeReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

InstanceGroupStateChangeReasonCode: TypeAlias = Literal[
    "INTERNAL_ERROR",
    "VALIDATION_ERROR",
    "INSTANCE_FAILURE",
    "CLUSTER_TERMINATED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERNAL_ERROR",
        "VALIDATION_ERROR",
        "INSTANCE_FAILURE",
        "CLUSTER_TERMINATED",
    )
)


def serialize_aws_json_1_1(value: InstanceGroupStateChangeReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceGroupStateChangeReasonCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InstanceGroupStateChangeReasonCode value: {data!r}"
        )
    return cast(InstanceGroupStateChangeReasonCode, data)
