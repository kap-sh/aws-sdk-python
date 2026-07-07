"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsLambdaFunctionCode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsLambdaFunctionCode(TypedDict, closed=True):
    s3_bucket: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>An Amazon S3 bucket in the same Amazon Web Services Region as your function. The bucket can be in a different Amazon Web Services account.</p>"""
    s3_key: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon S3 key of the deployment package.</p>"""
    s3_object_version: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>For versioned objects, the version of the deployment package object to use.</p>"""
    zip_file: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The base64-encoded contents of the deployment package. Amazon Web Services SDK and Amazon Web Services CLI clients handle the encoding for you.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsLambdaFunctionCode) -> dict:
    out: dict = {}
    if "s3_bucket" in value:
        out["S3Bucket"] = value["s3_bucket"]
    if "s3_key" in value:
        out["S3Key"] = value["s3_key"]
    if "s3_object_version" in value:
        out["S3ObjectVersion"] = value["s3_object_version"]
    if "zip_file" in value:
        out["ZipFile"] = value["zip_file"]
    return out


def deserialize_json(data: dict) -> AwsLambdaFunctionCode:
    out: AwsLambdaFunctionCode = {}  # type: ignore[typeddict-item]
    if "S3Bucket" in data:
        out["s3_bucket"] = data["S3Bucket"]
    if "S3Key" in data:
        out["s3_key"] = data["S3Key"]
    if "S3ObjectVersion" in data:
        out["s3_object_version"] = data["S3ObjectVersion"]
    if "ZipFile" in data:
        out["zip_file"] = data["ZipFile"]
    return out
