"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InstanceState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

InstanceState: TypeAlias = Literal[
    "pending",
    "running",
    "shutting-down",
    "terminated",
    "stopping",
    "stopped",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "running",
        "shutting-down",
        "terminated",
        "stopping",
        "stopped",
    )
)


def serialize_aws_json_1_0(value: InstanceState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InstanceState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceState value: {data!r}")
    return cast(InstanceState, data)
