"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentReportS3ReportList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_report_s3_report

ExperimentReportS3ReportList: TypeAlias = list[
    "aws_sdk_fis.types.experiment_report_s3_report.ExperimentReportS3Report"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentReportS3ReportList) -> list:
    import aws_sdk_fis.types.experiment_report_s3_report

    out: list = []
    for item in value:
        out.append(aws_sdk_fis.types.experiment_report_s3_report.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExperimentReportS3ReportList:
    import aws_sdk_fis.types.experiment_report_s3_report

    out: ExperimentReportS3ReportList = []
    for item in data:
        out.append(aws_sdk_fis.types.experiment_report_s3_report.deserialize_json(item))
    return out
