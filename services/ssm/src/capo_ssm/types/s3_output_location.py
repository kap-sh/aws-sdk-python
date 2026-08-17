"""Generated from Smithy shape ``com.amazonaws.ssm#S3OutputLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.s3_bucket_name
    import capo_ssm.types.s3_key_prefix
    import capo_ssm.types.s3_region


class S3OutputLocation(TypedDict, closed=True):
    output_s3_region: NotRequired["capo_ssm.types.s3_region.S3Region"]
    """<p>The Amazon Web Services Region of the S3 bucket.</p>"""
    output_s3_bucket_name: NotRequired["capo_ssm.types.s3_bucket_name.S3BucketName"]
    """<p>The name of the S3 bucket.</p>"""
    output_s3_key_prefix: NotRequired["capo_ssm.types.s3_key_prefix.S3KeyPrefix"]
    """<p>The S3 bucket subfolder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3OutputLocation) -> dict:
    out: dict = {}
    if "output_s3_region" in value:
        out["OutputS3Region"] = value["output_s3_region"]
    if "output_s3_bucket_name" in value:
        out["OutputS3BucketName"] = value["output_s3_bucket_name"]
    if "output_s3_key_prefix" in value:
        out["OutputS3KeyPrefix"] = value["output_s3_key_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3OutputLocation:
    out: S3OutputLocation = {}  # type: ignore[typeddict-item]
    if data.get("OutputS3Region") is not None:
        out["output_s3_region"] = data["OutputS3Region"]
    if data.get("OutputS3BucketName") is not None:
        out["output_s3_bucket_name"] = data["OutputS3BucketName"]
    if data.get("OutputS3KeyPrefix") is not None:
        out["output_s3_key_prefix"] = data["OutputS3KeyPrefix"]
    return out
