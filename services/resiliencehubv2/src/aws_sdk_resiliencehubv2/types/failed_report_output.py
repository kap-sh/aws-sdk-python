"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#FailedReportOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.report_generation_error_code


class FailedReportOutput(TypedDict):
    error_code: "aws_sdk_resiliencehubv2.types.report_generation_error_code.ReportGenerationErrorCode"
    """<p>The error code describing why the report generation failed.</p>"""
    error_message: NotRequired["str"]
    """<p>The error message describing why the report generation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedReportOutput) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.report_generation_error_code

    out["errorCode"] = (
        aws_sdk_resiliencehubv2.types.report_generation_error_code.serialize_json(
            value["error_code"]
        )
    )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> FailedReportOutput:
    out: FailedReportOutput = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        import aws_sdk_resiliencehubv2.types.report_generation_error_code

        out["error_code"] = (
            aws_sdk_resiliencehubv2.types.report_generation_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    else:
        raise DeserializationError("FailedReportOutput.error_code required")
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
