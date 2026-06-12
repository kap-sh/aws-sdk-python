"""Generated from Smithy shape ``com.amazonaws.xray#InsightSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.insight_summary

InsightSummaryList: TypeAlias = list[
    "aws_sdk_xray.types.insight_summary.InsightSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightSummaryList) -> list:
    import aws_sdk_xray.types.insight_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.insight_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightSummaryList:
    import aws_sdk_xray.types.insight_summary

    out: InsightSummaryList = []
    for item in data:
        out.append(aws_sdk_xray.types.insight_summary.deserialize_json(item))
    return out
