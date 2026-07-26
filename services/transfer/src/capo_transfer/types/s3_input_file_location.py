"""Generated from Smithy shape ``com.amazonaws.transfer#S3InputFileLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.s3_bucket
    import capo_transfer.types.s3_key


class S3InputFileLocation(TypedDict, closed=True):
    bucket: NotRequired["capo_transfer.types.s3_bucket.S3Bucket"]
    """<p>Specifies the S3 bucket for the customer input file.</p>"""
    key: NotRequired["capo_transfer.types.s3_key.S3Key"]
    """<p>The name assigned to the file when it was created in Amazon S3. You use the object key to retrieve the object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3InputFileLocation) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["Bucket"] = value["bucket"]
    if "key" in value:
        out["Key"] = value["key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3InputFileLocation:
    out: S3InputFileLocation = {}  # type: ignore[typeddict-item]
    if "Bucket" in data:
        out["bucket"] = data["Bucket"]
    if "Key" in data:
        out["key"] = data["Key"]
    return out
