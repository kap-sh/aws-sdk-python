"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppAssessmentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.app_assessment_summary

AppAssessmentSummaryList: TypeAlias = list[
    "capo_resiliencehub.types.app_assessment_summary.AppAssessmentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppAssessmentSummaryList) -> list:
    import capo_resiliencehub.types.app_assessment_summary

    out: list = []
    for item in value:
        out.append(capo_resiliencehub.types.app_assessment_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AppAssessmentSummaryList:
    import capo_resiliencehub.types.app_assessment_summary

    out: AppAssessmentSummaryList = []
    for item in data:
        out.append(
            capo_resiliencehub.types.app_assessment_summary.deserialize_json(item)
        )
    return out
