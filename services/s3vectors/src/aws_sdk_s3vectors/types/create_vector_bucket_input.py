"""Generated from Smithy shape ``com.amazonaws.s3vectors#CreateVectorBucketInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3vectors.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.encryption_configuration
    import aws_sdk_s3vectors.types.tags_map
    import aws_sdk_s3vectors.types.vector_bucket_name

class CreateVectorBucketInput(TypedDict):
    vector_bucket_name: "aws_sdk_s3vectors.types.vector_bucket_name.VectorBucketName"
    """<p>The name of the vector bucket to create. </p>"""
    encryption_configuration: NotRequired["aws_sdk_s3vectors.types.encryption_configuration.EncryptionConfiguration"]
    """<p>The encryption configuration for the vector bucket. By default, if you don't specify, all new vectors in Amazon S3 vector buckets use server-side encryption with Amazon S3 managed keys (SSE-S3), specifically <code>AES256</code>. </p>"""
    tags: NotRequired["aws_sdk_s3vectors.types.tags_map.TagsMap"]
    """<p>An array of user-defined tags that you would like to apply to the vector bucket that you are creating. A tag is a key-value pair that you apply to your resources. Tags can help you organize and control access to resources. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html\">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p> <note> <p>You must have the <code>s3vectors:TagResource</code> permission in addition to <code>s3vectors:CreateVectorBucket</code> permission to create a vector bucket with tags.</p> </note>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateVectorBucketInput) -> dict:
    out: dict = {}
    out["vectorBucketName"] = value["vector_bucket_name"]
    if "encryption_configuration" in value:
        import aws_sdk_s3vectors.types.encryption_configuration
        out["encryptionConfiguration"] = aws_sdk_s3vectors.types.encryption_configuration.serialize_json(value["encryption_configuration"])
    if "tags" in value:
        import aws_sdk_s3vectors.types.tags_map
        out["tags"] = aws_sdk_s3vectors.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateVectorBucketInput:
    out: CreateVectorBucketInput = {}  # type: ignore[typeddict-item]
    if "vectorBucketName" in data:
        out["vector_bucket_name"] = data["vectorBucketName"]
    else:
        raise DeserializationError("CreateVectorBucketInput.vector_bucket_name required")
    if "encryptionConfiguration" in data:
        import aws_sdk_s3vectors.types.encryption_configuration
        out["encryption_configuration"] = aws_sdk_s3vectors.types.encryption_configuration.deserialize_json(data["encryptionConfiguration"])
    if "tags" in data:
        import aws_sdk_s3vectors.types.tags_map
        out["tags"] = aws_sdk_s3vectors.types.tags_map.deserialize_json(data["tags"])
    return out