"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplateValidationStatusDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_template_validation_status
    import aws_sdk_cleanrooms.types.analysis_template_validation_status_reason_list
    import aws_sdk_cleanrooms.types.analysis_template_validation_type


class AnalysisTemplateValidationStatusDetail(TypedDict):
    type: "aws_sdk_cleanrooms.types.analysis_template_validation_type.AnalysisTemplateValidationType"
    """<p>The type of validation that was performed.</p>"""
    status: "aws_sdk_cleanrooms.types.analysis_template_validation_status.AnalysisTemplateValidationStatus"
    """<p>The status of the validation.</p>"""
    reasons: NotRequired[
        "aws_sdk_cleanrooms.types.analysis_template_validation_status_reason_list.AnalysisTemplateValidationStatusReasonList"
    ]
    """<p>The reasons for the validation results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTemplateValidationStatusDetail) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.analysis_template_validation_type

    out["type"] = (
        aws_sdk_cleanrooms.types.analysis_template_validation_type.serialize_json(
            value["type"]
        )
    )
    import aws_sdk_cleanrooms.types.analysis_template_validation_status

    out["status"] = (
        aws_sdk_cleanrooms.types.analysis_template_validation_status.serialize_json(
            value["status"]
        )
    )
    if "reasons" in value:
        import aws_sdk_cleanrooms.types.analysis_template_validation_status_reason_list

        out["reasons"] = (
            aws_sdk_cleanrooms.types.analysis_template_validation_status_reason_list.serialize_json(
                value["reasons"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalysisTemplateValidationStatusDetail:
    out: AnalysisTemplateValidationStatusDetail = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_cleanrooms.types.analysis_template_validation_type

        out["type"] = (
            aws_sdk_cleanrooms.types.analysis_template_validation_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError(
            "AnalysisTemplateValidationStatusDetail.type required"
        )
    if "status" in data:
        import aws_sdk_cleanrooms.types.analysis_template_validation_status

        out["status"] = (
            aws_sdk_cleanrooms.types.analysis_template_validation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "AnalysisTemplateValidationStatusDetail.status required"
        )
    if "reasons" in data:
        import aws_sdk_cleanrooms.types.analysis_template_validation_status_reason_list

        out["reasons"] = (
            aws_sdk_cleanrooms.types.analysis_template_validation_status_reason_list.deserialize_json(
                data["reasons"]
            )
        )
    return out
