"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NodeSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_managedblockchain.types.node_summary

NodeSummaryList: TypeAlias = list[
    "capo_managedblockchain.types.node_summary.NodeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: NodeSummaryList) -> list:
    import capo_managedblockchain.types.node_summary

    out: list = []
    for item in value:
        out.append(capo_managedblockchain.types.node_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> NodeSummaryList:
    import capo_managedblockchain.types.node_summary

    out: NodeSummaryList = []
    for item in data:
        out.append(capo_managedblockchain.types.node_summary.deserialize_json(item))
    return out
