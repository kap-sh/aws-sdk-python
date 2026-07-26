"""Generated from Smithy shape ``com.amazonaws.xray#InsightImpactGraphEdgeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.insight_impact_graph_edge

InsightImpactGraphEdgeList: TypeAlias = list[
    "capo_xray.types.insight_impact_graph_edge.InsightImpactGraphEdge"
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightImpactGraphEdgeList) -> list:
    import capo_xray.types.insight_impact_graph_edge

    out: list = []
    for item in value:
        out.append(capo_xray.types.insight_impact_graph_edge.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightImpactGraphEdgeList:
    import capo_xray.types.insight_impact_graph_edge

    out: InsightImpactGraphEdgeList = []
    for item in data:
        out.append(capo_xray.types.insight_impact_graph_edge.deserialize_json(item))
    return out
