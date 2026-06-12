"""Generated from Smithy shape ``com.amazonaws.medialive#NodeState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Used in DescribeNodeSummary."""
NodeState: TypeAlias = Literal[
    "CREATED",
    "REGISTERING",
    "READY_TO_ACTIVATE",
    "REGISTRATION_FAILED",
    "ACTIVATION_FAILED",
    "ACTIVE",
    "READY",
    "IN_USE",
    "DEREGISTERING",
    "DRAINING",
    "DEREGISTRATION_FAILED",
    "DEREGISTERED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "REGISTERING",
        "READY_TO_ACTIVATE",
        "REGISTRATION_FAILED",
        "ACTIVATION_FAILED",
        "ACTIVE",
        "READY",
        "IN_USE",
        "DEREGISTERING",
        "DRAINING",
        "DEREGISTRATION_FAILED",
        "DEREGISTERED",
    )
)


def serialize_json(value: NodeState) -> str:
    return value


def deserialize_json(data: str) -> NodeState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodeState value: {data!r}")
    return cast(NodeState, data)
