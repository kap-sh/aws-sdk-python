"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowS3Source``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_s3_object_key
    import aws_sdk_supplychain.types.s3_bucket_name


class DataIntegrationFlowS3Source(TypedDict, closed=True):
    bucket_name: "aws_sdk_supplychain.types.s3_bucket_name.S3BucketName"
    """<p>The S3 bucket name of the S3 source.</p>"""
    key: "aws_sdk_supplychain.types.data_integration_s3_object_key.DataIntegrationS3ObjectKey"
    """<p>The S3 object key of the S3 source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowS3Source) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    out["key"] = value["key"]
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowS3Source:
    out: DataIntegrationFlowS3Source = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("DataIntegrationFlowS3Source.bucket_name required")
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("DataIntegrationFlowS3Source.key required")
    return out
