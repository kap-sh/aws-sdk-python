"""Generated from Smithy shape ``com.amazonaws.lambda#LayerVersionContentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.blob
    import aws_sdk_lambda.types.s3_bucket
    import aws_sdk_lambda.types.s3_key
    import aws_sdk_lambda.types.s3_object_version


class LayerVersionContentInput(TypedDict, closed=True):
    s3_bucket: NotRequired["aws_sdk_lambda.types.s3_bucket.S3Bucket"]
    """<p>The Amazon S3 bucket of the layer archive.</p>"""
    s3_key: NotRequired["aws_sdk_lambda.types.s3_key.S3Key"]
    """<p>The Amazon S3 key of the layer archive.</p>"""
    s3_object_version: NotRequired[
        "aws_sdk_lambda.types.s3_object_version.S3ObjectVersion"
    ]
    """<p>For versioned objects, the version of the layer archive object to use.</p>"""
    zip_file: NotRequired["aws_sdk_lambda.types.blob.Blob"]
    """<p>The base64-encoded contents of the layer archive. Amazon Web Services SDK and Amazon Web Services CLI clients handle the encoding for you.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LayerVersionContentInput) -> dict:
    out: dict = {}
    if "s3_bucket" in value:
        out["S3Bucket"] = value["s3_bucket"]
    if "s3_key" in value:
        out["S3Key"] = value["s3_key"]
    if "s3_object_version" in value:
        out["S3ObjectVersion"] = value["s3_object_version"]
    if "zip_file" in value:
        import aws_sdk_lambda.types.blob

        out["ZipFile"] = aws_sdk_lambda.types.blob.serialize_json(value["zip_file"])
    return out


def deserialize_json(data: dict) -> LayerVersionContentInput:
    out: LayerVersionContentInput = {}  # type: ignore[typeddict-item]
    if "S3Bucket" in data:
        out["s3_bucket"] = data["S3Bucket"]
    if "S3Key" in data:
        out["s3_key"] = data["S3Key"]
    if "S3ObjectVersion" in data:
        out["s3_object_version"] = data["S3ObjectVersion"]
    if "ZipFile" in data:
        import aws_sdk_lambda.types.blob

        out["zip_file"] = aws_sdk_lambda.types.blob.deserialize_json(data["ZipFile"])
    return out
