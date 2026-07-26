"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GraphSnapshotSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_neptune_graph.types.graph_snapshot_summary

GraphSnapshotSummaryList: TypeAlias = list[
    "capo_neptune_graph.types.graph_snapshot_summary.GraphSnapshotSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: GraphSnapshotSummaryList) -> list:
    import capo_neptune_graph.types.graph_snapshot_summary

    out: list = []
    for item in value:
        out.append(capo_neptune_graph.types.graph_snapshot_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> GraphSnapshotSummaryList:
    import capo_neptune_graph.types.graph_snapshot_summary

    out: GraphSnapshotSummaryList = []
    for item in data:
        out.append(
            capo_neptune_graph.types.graph_snapshot_summary.deserialize_json(item)
        )
    return out
