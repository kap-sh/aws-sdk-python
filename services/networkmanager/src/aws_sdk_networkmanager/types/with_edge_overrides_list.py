"""Generated from Smithy shape ``com.amazonaws.networkmanager#WithEdgeOverridesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.edge_override

WithEdgeOverridesList: TypeAlias = list[
    "aws_sdk_networkmanager.types.edge_override.EdgeOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: WithEdgeOverridesList) -> list:
    import aws_sdk_networkmanager.types.edge_override

    out: list = []
    for item in value:
        out.append(aws_sdk_networkmanager.types.edge_override.serialize_json(item))
    return out


def deserialize_json(data: list) -> WithEdgeOverridesList:
    import aws_sdk_networkmanager.types.edge_override

    out: WithEdgeOverridesList = []
    for item in data:
        out.append(aws_sdk_networkmanager.types.edge_override.deserialize_json(item))
    return out
