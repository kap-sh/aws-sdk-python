"""Generated from Smithy shape ``com.amazonaws.transfer#S3FileLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transfer.types.s3_bucket
    import aws_sdk_transfer.types.s3_etag
    import aws_sdk_transfer.types.s3_key
    import aws_sdk_transfer.types.s3_version_id


class S3FileLocation(TypedDict, closed=True):
    bucket: NotRequired["aws_sdk_transfer.types.s3_bucket.S3Bucket"]
    """<p>Specifies the S3 bucket that contains the file being used.</p>"""
    key: NotRequired["aws_sdk_transfer.types.s3_key.S3Key"]
    """<p>The name assigned to the file when it was created in Amazon S3. You use the object key to retrieve the object.</p>"""
    version_id: NotRequired["aws_sdk_transfer.types.s3_version_id.S3VersionId"]
    """<p>Specifies the file version.</p>"""
    etag: NotRequired["aws_sdk_transfer.types.s3_etag.S3Etag"]
    """<p>The entity tag is a hash of the object. The ETag reflects changes only to the contents of an object, not its metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3FileLocation) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["Bucket"] = value["bucket"]
    if "key" in value:
        out["Key"] = value["key"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    if "etag" in value:
        out["Etag"] = value["etag"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3FileLocation:
    out: S3FileLocation = {}  # type: ignore[typeddict-item]
    if "Bucket" in data:
        out["bucket"] = data["Bucket"]
    if "Key" in data:
        out["key"] = data["Key"]
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    if "Etag" in data:
        out["etag"] = data["Etag"]
    return out
