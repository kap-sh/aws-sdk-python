"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentReport``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_report_s3_report_list
    import aws_sdk_fis.types.experiment_report_state


class ExperimentReport(TypedDict):
    state: NotRequired[
        "aws_sdk_fis.types.experiment_report_state.ExperimentReportState"
    ]
    """<p>The state of the experiment report.</p>"""
    s3_reports: NotRequired[
        "aws_sdk_fis.types.experiment_report_s3_report_list.ExperimentReportS3ReportList"
    ]
    """<p>The S3 destination of the experiment report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentReport) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_fis.types.experiment_report_state

        out["state"] = aws_sdk_fis.types.experiment_report_state.serialize_json(
            value["state"]
        )
    if "s3_reports" in value:
        import aws_sdk_fis.types.experiment_report_s3_report_list

        out["s3Reports"] = (
            aws_sdk_fis.types.experiment_report_s3_report_list.serialize_json(
                value["s3_reports"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExperimentReport:
    out: ExperimentReport = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_fis.types.experiment_report_state

        out["state"] = aws_sdk_fis.types.experiment_report_state.deserialize_json(
            data["state"]
        )
    if "s3Reports" in data:
        import aws_sdk_fis.types.experiment_report_s3_report_list

        out["s3_reports"] = (
            aws_sdk_fis.types.experiment_report_s3_report_list.deserialize_json(
                data["s3Reports"]
            )
        )
    return out
