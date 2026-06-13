"""Generated from Smithy shape ``com.amazonaws.emr#InstanceGroupState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

InstanceGroupState: TypeAlias = Literal[
    "PROVISIONING",
    "BOOTSTRAPPING",
    "RUNNING",
    "RECONFIGURING",
    "RESIZING",
    "SUSPENDED",
    "TERMINATING",
    "TERMINATED",
    "ARRESTED",
    "SHUTTING_DOWN",
    "ENDED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROVISIONING",
        "BOOTSTRAPPING",
        "RUNNING",
        "RECONFIGURING",
        "RESIZING",
        "SUSPENDED",
        "TERMINATING",
        "TERMINATED",
        "ARRESTED",
        "SHUTTING_DOWN",
        "ENDED",
    )
)


def serialize_aws_json_1_1(value: InstanceGroupState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceGroupState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceGroupState value: {data!r}")
    return cast(InstanceGroupState, data)
