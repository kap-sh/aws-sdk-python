"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplateValidationStatusReasonList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_template_validation_status_reason

AnalysisTemplateValidationStatusReasonList: TypeAlias = list[
    "capo_cleanrooms.types.analysis_template_validation_status_reason.AnalysisTemplateValidationStatusReason"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTemplateValidationStatusReasonList) -> list:
    import capo_cleanrooms.types.analysis_template_validation_status_reason

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.analysis_template_validation_status_reason.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalysisTemplateValidationStatusReasonList:
    import capo_cleanrooms.types.analysis_template_validation_status_reason

    out: AnalysisTemplateValidationStatusReasonList = []
    for item in data:
        out.append(
            capo_cleanrooms.types.analysis_template_validation_status_reason.deserialize_json(
                item
            )
        )
    return out
