"""Generated from Smithy shape ``com.amazonaws.opensearch#NodeStatus``."""

from typing import Literal, TypeAlias, cast

NodeStatus: TypeAlias = Literal[
    "Active",
    "StandBy",
    "NotAvailable",
]


# --- restJson1 ser/de ---
def serialize_json(value: NodeStatus) -> str:
    return value


def deserialize_json(data: str) -> NodeStatus:
    return cast(NodeStatus, data)
