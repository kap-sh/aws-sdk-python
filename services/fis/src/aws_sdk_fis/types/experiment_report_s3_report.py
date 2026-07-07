"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentReportS3Report``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_report_s3_report_arn
    import aws_sdk_fis.types.experiment_report_s3_report_type


class ExperimentReportS3Report(TypedDict, closed=True):
    arn: NotRequired[
        "aws_sdk_fis.types.experiment_report_s3_report_arn.ExperimentReportS3ReportArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the generated report.</p>"""
    report_type: NotRequired[
        "aws_sdk_fis.types.experiment_report_s3_report_type.ExperimentReportS3ReportType"
    ]
    """<p>The report type for the experiment report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentReportS3Report) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "report_type" in value:
        out["reportType"] = value["report_type"]
    return out


def deserialize_json(data: dict) -> ExperimentReportS3Report:
    out: ExperimentReportS3Report = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "reportType" in data:
        out["report_type"] = data["reportType"]
    return out
