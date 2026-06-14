"""Generated from Smithy shape ``com.amazonaws.textract#OutputConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_textract.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_textract.types.s3_bucket
    import aws_sdk_textract.types.s3_object_name


class OutputConfig(TypedDict):
    s3_bucket: "aws_sdk_textract.types.s3_bucket.S3Bucket"
    """<p>The name of the bucket your output will go to.</p>"""
    s3_prefix: NotRequired["aws_sdk_textract.types.s3_object_name.S3ObjectName"]
    r"""<p>The prefix of the object key that the output will be saved to. When not enabled, the prefix will be “textract_output\".</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputConfig) -> dict:
    out: dict = {}
    out["S3Bucket"] = value["s3_bucket"]
    if "s3_prefix" in value:
        out["S3Prefix"] = value["s3_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OutputConfig:
    out: OutputConfig = {}  # type: ignore[typeddict-item]
    if "S3Bucket" in data:
        out["s3_bucket"] = data["S3Bucket"]
    else:
        raise DeserializationError("OutputConfig.s3_bucket required")
    if "S3Prefix" in data:
        out["s3_prefix"] = data["S3Prefix"]
    return out
