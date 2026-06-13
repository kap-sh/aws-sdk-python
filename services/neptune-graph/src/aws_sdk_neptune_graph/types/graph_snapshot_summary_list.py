"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GraphSnapshotSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.graph_snapshot_summary

GraphSnapshotSummaryList: TypeAlias = list[
    "aws_sdk_neptune_graph.types.graph_snapshot_summary.GraphSnapshotSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: GraphSnapshotSummaryList) -> list:
    import aws_sdk_neptune_graph.types.graph_snapshot_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_neptune_graph.types.graph_snapshot_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GraphSnapshotSummaryList:
    import aws_sdk_neptune_graph.types.graph_snapshot_summary

    out: GraphSnapshotSummaryList = []
    for item in data:
        out.append(
            aws_sdk_neptune_graph.types.graph_snapshot_summary.deserialize_json(item)
        )
    return out
