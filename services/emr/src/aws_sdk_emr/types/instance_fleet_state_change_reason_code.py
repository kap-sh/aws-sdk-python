"""Generated from Smithy shape ``com.amazonaws.emr#InstanceFleetStateChangeReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

InstanceFleetStateChangeReasonCode: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: InstanceFleetStateChangeReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceFleetStateChangeReasonCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InstanceFleetStateChangeReasonCode value: {data!r}"
        )
    return cast(InstanceFleetStateChangeReasonCode, data)
