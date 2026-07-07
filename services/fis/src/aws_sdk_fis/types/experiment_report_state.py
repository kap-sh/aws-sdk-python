"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentReportState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_report_error
    import aws_sdk_fis.types.experiment_report_reason
    import aws_sdk_fis.types.experiment_report_status


class ExperimentReportState(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_fis.types.experiment_report_status.ExperimentReportStatus"
    ]
    """<p>The state of the experiment report generation.</p>"""
    reason: NotRequired[
        "aws_sdk_fis.types.experiment_report_reason.ExperimentReportReason"
    ]
    """<p>The reason for the state of the experiment report generation.</p>"""
    error: NotRequired[
        "aws_sdk_fis.types.experiment_report_error.ExperimentReportError"
    ]
    """<p>The error information of the experiment when the experiment report generation has failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentReportState) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_fis.types.experiment_report_status

        out["status"] = aws_sdk_fis.types.experiment_report_status.serialize_json(
            value["status"]
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    if "error" in value:
        import aws_sdk_fis.types.experiment_report_error

        out["error"] = aws_sdk_fis.types.experiment_report_error.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> ExperimentReportState:
    out: ExperimentReportState = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_fis.types.experiment_report_status

        out["status"] = aws_sdk_fis.types.experiment_report_status.deserialize_json(
            data["status"]
        )
    if "reason" in data:
        out["reason"] = data["reason"]
    if "error" in data:
        import aws_sdk_fis.types.experiment_report_error

        out["error"] = aws_sdk_fis.types.experiment_report_error.deserialize_json(
            data["error"]
        )
    return out
