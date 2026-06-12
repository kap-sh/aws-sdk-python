"""Generated from Smithy shape ``com.amazonaws.appstream#LastReportGenerationExecutionError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.string
    import aws_sdk_appstream.types.usage_report_execution_error_code


class LastReportGenerationExecutionError(TypedDict):
    error_code: NotRequired[
        "aws_sdk_appstream.types.usage_report_execution_error_code.UsageReportExecutionErrorCode"
    ]
    """<p>The error code for the error that is returned when a usage report can't be generated.</p>"""
    error_message: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The error message for the error that is returned when a usage report can't be generated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastReportGenerationExecutionError) -> dict:
    out: dict = {}
    if "error_code" in value:
        import aws_sdk_appstream.types.usage_report_execution_error_code

        out["ErrorCode"] = (
            aws_sdk_appstream.types.usage_report_execution_error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LastReportGenerationExecutionError:
    out: LastReportGenerationExecutionError = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        import aws_sdk_appstream.types.usage_report_execution_error_code

        out["error_code"] = (
            aws_sdk_appstream.types.usage_report_execution_error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
