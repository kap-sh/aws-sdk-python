"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ExportS3DataInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.kms_key
    import aws_sdk_sagemaker_geospatial.types.s3_uri


class ExportS3DataInput(TypedDict):
    s3_uri: "aws_sdk_sagemaker_geospatial.types.s3_uri.S3Uri"
    """<p>The URL to the Amazon S3 data input.</p>"""
    kms_key_id: NotRequired["aws_sdk_sagemaker_geospatial.types.kms_key.KmsKey"]
    """<p>The Key Management Service key ID for server-side encryption.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportS3DataInput) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> ExportS3DataInput:
    out: ExportS3DataInput = {}  # type: ignore[typeddict-item]
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    else:
        raise DeserializationError("ExportS3DataInput.s3_uri required")
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
