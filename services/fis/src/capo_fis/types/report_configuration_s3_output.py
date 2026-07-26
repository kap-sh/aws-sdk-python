"""Generated from Smithy shape ``com.amazonaws.fis#ReportConfigurationS3Output``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.report_configuration_s3_output_prefix
    import capo_fis.types.s3_bucket_name


class ReportConfigurationS3Output(TypedDict, closed=True):
    bucket_name: NotRequired["capo_fis.types.s3_bucket_name.S3BucketName"]
    """<p>The name of the S3 bucket where the experiment report will be stored.</p>"""
    prefix: NotRequired[
        "capo_fis.types.report_configuration_s3_output_prefix.ReportConfigurationS3OutputPrefix"
    ]
    """<p>The prefix of the S3 bucket where the experiment report will be stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportConfigurationS3Output) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["bucketName"] = value["bucket_name"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> ReportConfigurationS3Output:
    out: ReportConfigurationS3Output = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    return out
