"""Generated from Smithy shape ``com.amazonaws.xray#InsightImpactGraphServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.insight_impact_graph_service

InsightImpactGraphServiceList: TypeAlias = list[
    "capo_xray.types.insight_impact_graph_service.InsightImpactGraphService"
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightImpactGraphServiceList) -> list:
    import capo_xray.types.insight_impact_graph_service

    out: list = []
    for item in value:
        out.append(capo_xray.types.insight_impact_graph_service.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightImpactGraphServiceList:
    import capo_xray.types.insight_impact_graph_service

    out: InsightImpactGraphServiceList = []
    for item in data:
        out.append(capo_xray.types.insight_impact_graph_service.deserialize_json(item))
    return out
