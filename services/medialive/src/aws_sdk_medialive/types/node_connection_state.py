"""Generated from Smithy shape ``com.amazonaws.medialive#NodeConnectionState``."""

from typing import Literal, TypeAlias, cast

"""Used in DescribeNodeSummary."""
NodeConnectionState: TypeAlias = Literal[
    "CONNECTED",
    "DISCONNECTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: NodeConnectionState) -> str:
    return value


def deserialize_json(data: str) -> NodeConnectionState:
    return cast(NodeConnectionState, data)
