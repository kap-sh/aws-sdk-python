"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplateSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_template_summary

AnalysisTemplateSummaryList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.analysis_template_summary.AnalysisTemplateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTemplateSummaryList) -> list:
    import aws_sdk_cleanrooms.types.analysis_template_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.analysis_template_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalysisTemplateSummaryList:
    import aws_sdk_cleanrooms.types.analysis_template_summary

    out: AnalysisTemplateSummaryList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.analysis_template_summary.deserialize_json(item)
        )
    return out
