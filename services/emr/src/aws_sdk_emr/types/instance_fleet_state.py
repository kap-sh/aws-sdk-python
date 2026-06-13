"""Generated from Smithy shape ``com.amazonaws.emr#InstanceFleetState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

InstanceFleetState: TypeAlias = Literal[
    "PROVISIONING",
    "BOOTSTRAPPING",
    "RUNNING",
    "RESIZING",
    "RECONFIGURING",
    "SUSPENDED",
    "TERMINATING",
    "TERMINATED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROVISIONING",
        "BOOTSTRAPPING",
        "RUNNING",
        "RESIZING",
        "RECONFIGURING",
        "SUSPENDED",
        "TERMINATING",
        "TERMINATED",
    )
)


def serialize_aws_json_1_1(value: InstanceFleetState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceFleetState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceFleetState value: {data!r}")
    return cast(InstanceFleetState, data)
