"""Generated from Smithy shape ``com.amazonaws.datazone#LineageNodeSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.lineage_node_summary

LineageNodeSummaries: TypeAlias = list[
    "aws_sdk_datazone.types.lineage_node_summary.LineageNodeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: LineageNodeSummaries) -> list:
    import aws_sdk_datazone.types.lineage_node_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.lineage_node_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> LineageNodeSummaries:
    import aws_sdk_datazone.types.lineage_node_summary

    out: LineageNodeSummaries = []
    for item in data:
        out.append(aws_sdk_datazone.types.lineage_node_summary.deserialize_json(item))
    return out
