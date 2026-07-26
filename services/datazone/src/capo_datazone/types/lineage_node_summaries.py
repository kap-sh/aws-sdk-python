"""Generated from Smithy shape ``com.amazonaws.datazone#LineageNodeSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.lineage_node_summary

LineageNodeSummaries: TypeAlias = list[
    "capo_datazone.types.lineage_node_summary.LineageNodeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: LineageNodeSummaries) -> list:
    import capo_datazone.types.lineage_node_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.lineage_node_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> LineageNodeSummaries:
    import capo_datazone.types.lineage_node_summary

    out: LineageNodeSummaries = []
    for item in data:
        out.append(capo_datazone.types.lineage_node_summary.deserialize_json(item))
    return out
