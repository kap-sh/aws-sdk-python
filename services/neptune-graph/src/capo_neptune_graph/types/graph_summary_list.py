"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GraphSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_neptune_graph.types.graph_summary

GraphSummaryList: TypeAlias = list[
    "capo_neptune_graph.types.graph_summary.GraphSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: GraphSummaryList) -> list:
    import capo_neptune_graph.types.graph_summary

    out: list = []
    for item in value:
        out.append(capo_neptune_graph.types.graph_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> GraphSummaryList:
    import capo_neptune_graph.types.graph_summary

    out: GraphSummaryList = []
    for item in data:
        out.append(capo_neptune_graph.types.graph_summary.deserialize_json(item))
    return out
