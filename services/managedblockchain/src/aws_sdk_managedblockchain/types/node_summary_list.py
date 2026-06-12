"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NodeSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.node_summary

NodeSummaryList: TypeAlias = list[
    "aws_sdk_managedblockchain.types.node_summary.NodeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: NodeSummaryList) -> list:
    import aws_sdk_managedblockchain.types.node_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_managedblockchain.types.node_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> NodeSummaryList:
    import aws_sdk_managedblockchain.types.node_summary

    out: NodeSummaryList = []
    for item in data:
        out.append(aws_sdk_managedblockchain.types.node_summary.deserialize_json(item))
    return out
