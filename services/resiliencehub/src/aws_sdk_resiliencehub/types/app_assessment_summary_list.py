"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppAssessmentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.app_assessment_summary

AppAssessmentSummaryList: TypeAlias = list[
    "aws_sdk_resiliencehub.types.app_assessment_summary.AppAssessmentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppAssessmentSummaryList) -> list:
    import aws_sdk_resiliencehub.types.app_assessment_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehub.types.app_assessment_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AppAssessmentSummaryList:
    import aws_sdk_resiliencehub.types.app_assessment_summary

    out: AppAssessmentSummaryList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehub.types.app_assessment_summary.deserialize_json(item)
        )
    return out
