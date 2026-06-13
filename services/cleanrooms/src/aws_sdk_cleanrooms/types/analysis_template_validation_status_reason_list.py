"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplateValidationStatusReasonList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_template_validation_status_reason

AnalysisTemplateValidationStatusReasonList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.analysis_template_validation_status_reason.AnalysisTemplateValidationStatusReason"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTemplateValidationStatusReasonList) -> list:
    import aws_sdk_cleanrooms.types.analysis_template_validation_status_reason

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.analysis_template_validation_status_reason.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalysisTemplateValidationStatusReasonList:
    import aws_sdk_cleanrooms.types.analysis_template_validation_status_reason

    out: AnalysisTemplateValidationStatusReasonList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.analysis_template_validation_status_reason.deserialize_json(
                item
            )
        )
    return out
