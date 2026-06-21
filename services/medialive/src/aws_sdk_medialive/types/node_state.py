"""Generated from Smithy shape ``com.amazonaws.medialive#NodeState``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: NodeState) -> str:
    return value


def deserialize_json(data: str) -> NodeState:
    return cast(NodeState, data)
