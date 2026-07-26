"""Generated from Smithy shape ``com.amazonaws.eks#InsightSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.insight_summary

InsightSummaries: TypeAlias = list["capo_eks.types.insight_summary.InsightSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: InsightSummaries) -> list:
    import capo_eks.types.insight_summary

    out: list = []
    for item in value:
        out.append(capo_eks.types.insight_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightSummaries:
    import capo_eks.types.insight_summary

    out: InsightSummaries = []
    for item in data:
        out.append(capo_eks.types.insight_summary.deserialize_json(item))
    return out
