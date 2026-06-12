"""Generated from Smithy shape ``com.amazonaws.xray#InsightImpactGraphServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.insight_impact_graph_service

InsightImpactGraphServiceList: TypeAlias = list[
    "aws_sdk_xray.types.insight_impact_graph_service.InsightImpactGraphService"
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightImpactGraphServiceList) -> list:
    import aws_sdk_xray.types.insight_impact_graph_service

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.insight_impact_graph_service.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightImpactGraphServiceList:
    import aws_sdk_xray.types.insight_impact_graph_service

    out: InsightImpactGraphServiceList = []
    for item in data:
        out.append(
            aws_sdk_xray.types.insight_impact_graph_service.deserialize_json(item)
        )
    return out
