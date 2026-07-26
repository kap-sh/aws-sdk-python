"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AssessmentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.assessment_summary

AssessmentSummaryList: TypeAlias = list[
    "capo_resiliencehubv2.types.assessment_summary.AssessmentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentSummaryList) -> list:
    import capo_resiliencehubv2.types.assessment_summary

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.assessment_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssessmentSummaryList:
    import capo_resiliencehubv2.types.assessment_summary

    out: AssessmentSummaryList = []
    for item in data:
        out.append(capo_resiliencehubv2.types.assessment_summary.deserialize_json(item))
    return out
