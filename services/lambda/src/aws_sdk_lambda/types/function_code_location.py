"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionCodeLocation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class FunctionCodeLocation(TypedDict):
    repository_type: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The service that's hosting the file.</p>"""
    location: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>A presigned URL that you can use to download the deployment package.</p>"""
    image_uri: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>URI of a container image in the Amazon ECR registry.</p>"""
    resolved_image_uri: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The resolved URI for the image.</p>"""
    source_kms_key_arn: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt your function's .zip deployment package. If you don't provide a customer managed key, Lambda uses an <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk\">Amazon Web Services owned key</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionCodeLocation) -> dict:
    out: dict = {}
    if "repository_type" in value:
        out["RepositoryType"] = value["repository_type"]
    if "location" in value:
        out["Location"] = value["location"]
    if "image_uri" in value:
        out["ImageUri"] = value["image_uri"]
    if "resolved_image_uri" in value:
        out["ResolvedImageUri"] = value["resolved_image_uri"]
    if "source_kms_key_arn" in value:
        out["SourceKMSKeyArn"] = value["source_kms_key_arn"]
    return out


def deserialize_json(data: dict) -> FunctionCodeLocation:
    out: FunctionCodeLocation = {}  # type: ignore[typeddict-item]
    if "RepositoryType" in data:
        out["repository_type"] = data["RepositoryType"]
    if "Location" in data:
        out["location"] = data["Location"]
    if "ImageUri" in data:
        out["image_uri"] = data["ImageUri"]
    if "ResolvedImageUri" in data:
        out["resolved_image_uri"] = data["ResolvedImageUri"]
    if "SourceKMSKeyArn" in data:
        out["source_kms_key_arn"] = data["SourceKMSKeyArn"]
    return out
