"""Generated from Smithy shape ``com.amazonaws.medialive#NodeRole``."""

from typing import Literal, TypeAlias, cast

"""Used in CreateNodeRequest, CreateNodeRegistrationScriptRequest, DescribeNodeResult, DescribeNodeSummary, UpdateNodeRequest."""
NodeRole: TypeAlias = Literal[
    "BACKUP",
    "ACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: NodeRole) -> str:
    return value


def deserialize_json(data: str) -> NodeRole:
    return cast(NodeRole, data)
