"""Generated from Smithy shape ``com.amazonaws.s3tables#CreateTableRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3tables.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_s3tables.types.encryption_configuration
    import aws_sdk_s3tables.types.namespace_name
    import aws_sdk_s3tables.types.open_table_format
    import aws_sdk_s3tables.types.storage_class_configuration
    import aws_sdk_s3tables.types.table_bucket_arn
    import aws_sdk_s3tables.types.table_metadata
    import aws_sdk_s3tables.types.table_name
    import aws_sdk_s3tables.types.tags

class CreateTableRequest(TypedDict):
    table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket to create the table in.</p>"""
    namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName"
    """<p>The namespace to associated with the table.</p>"""
    name: "aws_sdk_s3tables.types.table_name.TableName"
    """<p>The name for the table.</p>"""
    format: "aws_sdk_s3tables.types.open_table_format.OpenTableFormat"
    """<p>The format for the table.</p>"""
    metadata: NotRequired["aws_sdk_s3tables.types.table_metadata.TableMetadata"]
    """<p>The metadata for the table.</p>"""
    encryption_configuration: NotRequired["aws_sdk_s3tables.types.encryption_configuration.EncryptionConfiguration"]
    """<p>The encryption configuration to use for the table. This configuration specifies the encryption algorithm and, if using SSE-KMS, the KMS key to use for encrypting the table. </p> <note> <p>If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html\">Permissions requirements for S3 Tables SSE-KMS encryption</a>.</p> </note>"""
    storage_class_configuration: NotRequired["aws_sdk_s3tables.types.storage_class_configuration.StorageClassConfiguration"]
    """<p>The storage class configuration for the table. If not specified, the table inherits the storage class configuration from its table bucket. Specify this parameter to override the bucket's default storage class for this table.</p>"""
    tags: NotRequired["aws_sdk_s3tables.types.tags.Tags"]
    """<p>A map of user-defined tags that you would like to apply to the table that you are creating. A tag is a key-value pair that you apply to your resources. Tags can help you organize, track costs for, and control access to resources. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html\">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p> <note> <p>You must have the <code>s3tables:TagResource</code> permission in addition to <code>s3tables:CreateTable</code> permission to create a table with tags.</p> </note>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateTableRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_s3tables.types.open_table_format
    out["format"] = aws_sdk_s3tables.types.open_table_format.serialize_json(value["format"])
    if "metadata" in value:
        import aws_sdk_s3tables.types.table_metadata
        out["metadata"] = aws_sdk_s3tables.types.table_metadata.serialize_json(value["metadata"])
    if "encryption_configuration" in value:
        import aws_sdk_s3tables.types.encryption_configuration
        out["encryptionConfiguration"] = aws_sdk_s3tables.types.encryption_configuration.serialize_json(value["encryption_configuration"])
    if "storage_class_configuration" in value:
        import aws_sdk_s3tables.types.storage_class_configuration
        out["storageClassConfiguration"] = aws_sdk_s3tables.types.storage_class_configuration.serialize_json(value["storage_class_configuration"])
    if "tags" in value:
        import aws_sdk_s3tables.types.tags
        out["tags"] = aws_sdk_s3tables.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateTableRequest:
    out: CreateTableRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateTableRequest.name required")
    if "format" in data:
        import aws_sdk_s3tables.types.open_table_format
        out["format"] = aws_sdk_s3tables.types.open_table_format.deserialize_json(data["format"])
    else:
        raise DeserializationError("CreateTableRequest.format required")
    if "metadata" in data:
        import aws_sdk_s3tables.types.table_metadata
        out["metadata"] = aws_sdk_s3tables.types.table_metadata.deserialize_json(data["metadata"])
    if "encryptionConfiguration" in data:
        import aws_sdk_s3tables.types.encryption_configuration
        out["encryption_configuration"] = aws_sdk_s3tables.types.encryption_configuration.deserialize_json(data["encryptionConfiguration"])
    if "storageClassConfiguration" in data:
        import aws_sdk_s3tables.types.storage_class_configuration
        out["storage_class_configuration"] = aws_sdk_s3tables.types.storage_class_configuration.deserialize_json(data["storageClassConfiguration"])
    if "tags" in data:
        import aws_sdk_s3tables.types.tags
        out["tags"] = aws_sdk_s3tables.types.tags.deserialize_json(data["tags"])
    return out