"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentReportConfigurationOutputsS3Configuration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fis.types.report_configuration_s3_output_prefix
    import aws_sdk_fis.types.s3_bucket_name


class ExperimentReportConfigurationOutputsS3Configuration(TypedDict):
    bucket_name: NotRequired["aws_sdk_fis.types.s3_bucket_name.S3BucketName"]
    """<p>The name of the S3 bucket where the experiment report will be stored.</p>"""
    prefix: NotRequired[
        "aws_sdk_fis.types.report_configuration_s3_output_prefix.ReportConfigurationS3OutputPrefix"
    ]
    """<p>The prefix of the S3 bucket where the experiment report will be stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentReportConfigurationOutputsS3Configuration) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["bucketName"] = value["bucket_name"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> ExperimentReportConfigurationOutputsS3Configuration:
    out: ExperimentReportConfigurationOutputsS3Configuration = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    return out
