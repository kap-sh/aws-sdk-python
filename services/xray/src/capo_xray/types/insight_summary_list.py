"""Generated from Smithy shape ``com.amazonaws.xray#InsightSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.insight_summary

InsightSummaryList: TypeAlias = list["capo_xray.types.insight_summary.InsightSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: InsightSummaryList) -> list:
    import capo_xray.types.insight_summary

    out: list = []
    for item in value:
        out.append(capo_xray.types.insight_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightSummaryList:
    import capo_xray.types.insight_summary

    out: InsightSummaryList = []
    for item in data:
        out.append(capo_xray.types.insight_summary.deserialize_json(item))
    return out
