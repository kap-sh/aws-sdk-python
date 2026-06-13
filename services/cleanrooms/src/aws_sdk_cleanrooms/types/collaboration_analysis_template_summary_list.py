"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationAnalysisTemplateSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_analysis_template_summary

CollaborationAnalysisTemplateSummaryList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.collaboration_analysis_template_summary.CollaborationAnalysisTemplateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationAnalysisTemplateSummaryList) -> list:
    import aws_sdk_cleanrooms.types.collaboration_analysis_template_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.collaboration_analysis_template_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CollaborationAnalysisTemplateSummaryList:
    import aws_sdk_cleanrooms.types.collaboration_analysis_template_summary

    out: CollaborationAnalysisTemplateSummaryList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.collaboration_analysis_template_summary.deserialize_json(
                item
            )
        )
    return out
