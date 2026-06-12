"""Generated from Smithy shape ``com.amazonaws.guardduty#S3Bucket``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.public_access_configuration
    import aws_sdk_guardduty.types.public_access_status
    import aws_sdk_guardduty.types.s3_object_uids
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.timestamp


class S3Bucket(TypedDict):
    owner_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The owner ID of the associated S3Amazon S3bucket.</p>"""
    created_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the Amazon S3 bucket was created.</p>"""
    encryption_type: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The type of encryption used for the Amazon S3 buckets and its objects. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html\">Protecting data with server-side encryption</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    encryption_key_arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the encryption key that is used to encrypt the Amazon S3 bucket and its objects.</p>"""
    effective_permission: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Describes the effective permissions on this S3 bucket, after factoring all the attached policies.</p>"""
    public_read_access: NotRequired[
        "aws_sdk_guardduty.types.public_access_status.PublicAccessStatus"
    ]
    """<p>Indicates whether or not the public read access is allowed for an Amazon S3 bucket.</p>"""
    public_write_access: NotRequired[
        "aws_sdk_guardduty.types.public_access_status.PublicAccessStatus"
    ]
    """<p>Indicates whether or not the public write access is allowed for an Amazon S3 bucket.</p>"""
    account_public_access: NotRequired[
        "aws_sdk_guardduty.types.public_access_configuration.PublicAccessConfiguration"
    ]
    """<p>Contains information about the public access policies that apply to the Amazon S3 bucket at the account level.</p>"""
    bucket_public_access: NotRequired[
        "aws_sdk_guardduty.types.public_access_configuration.PublicAccessConfiguration"
    ]
    """<p>Contains information about public access policies that apply to the Amazon S3 bucket.</p>"""
    s3_object_uids: NotRequired["aws_sdk_guardduty.types.s3_object_uids.S3ObjectUids"]
    """<p>Represents a list of Amazon S3 object identifiers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Bucket) -> dict:
    out: dict = {}
    if "owner_id" in value:
        out["ownerId"] = value["owner_id"]
    if "created_at" in value:
        import aws_sdk_guardduty.types.timestamp

        out["createdAt"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "encryption_type" in value:
        out["encryptionType"] = value["encryption_type"]
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    if "effective_permission" in value:
        out["effectivePermission"] = value["effective_permission"]
    if "public_read_access" in value:
        import aws_sdk_guardduty.types.public_access_status

        out["publicReadAccess"] = (
            aws_sdk_guardduty.types.public_access_status.serialize_json(
                value["public_read_access"]
            )
        )
    if "public_write_access" in value:
        import aws_sdk_guardduty.types.public_access_status

        out["publicWriteAccess"] = (
            aws_sdk_guardduty.types.public_access_status.serialize_json(
                value["public_write_access"]
            )
        )
    if "account_public_access" in value:
        import aws_sdk_guardduty.types.public_access_configuration

        out["accountPublicAccess"] = (
            aws_sdk_guardduty.types.public_access_configuration.serialize_json(
                value["account_public_access"]
            )
        )
    if "bucket_public_access" in value:
        import aws_sdk_guardduty.types.public_access_configuration

        out["bucketPublicAccess"] = (
            aws_sdk_guardduty.types.public_access_configuration.serialize_json(
                value["bucket_public_access"]
            )
        )
    if "s3_object_uids" in value:
        import aws_sdk_guardduty.types.s3_object_uids

        out["s3ObjectUids"] = aws_sdk_guardduty.types.s3_object_uids.serialize_json(
            value["s3_object_uids"]
        )
    return out


def deserialize_json(data: dict) -> S3Bucket:
    out: S3Bucket = {}  # type: ignore[typeddict-item]
    if "ownerId" in data:
        out["owner_id"] = data["ownerId"]
    if "createdAt" in data:
        import aws_sdk_guardduty.types.timestamp

        out["created_at"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "encryptionType" in data:
        out["encryption_type"] = data["encryptionType"]
    if "encryptionKeyArn" in data:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    if "effectivePermission" in data:
        out["effective_permission"] = data["effectivePermission"]
    if "publicReadAccess" in data:
        import aws_sdk_guardduty.types.public_access_status

        out["public_read_access"] = (
            aws_sdk_guardduty.types.public_access_status.deserialize_json(
                data["publicReadAccess"]
            )
        )
    if "publicWriteAccess" in data:
        import aws_sdk_guardduty.types.public_access_status

        out["public_write_access"] = (
            aws_sdk_guardduty.types.public_access_status.deserialize_json(
                data["publicWriteAccess"]
            )
        )
    if "accountPublicAccess" in data:
        import aws_sdk_guardduty.types.public_access_configuration

        out["account_public_access"] = (
            aws_sdk_guardduty.types.public_access_configuration.deserialize_json(
                data["accountPublicAccess"]
            )
        )
    if "bucketPublicAccess" in data:
        import aws_sdk_guardduty.types.public_access_configuration

        out["bucket_public_access"] = (
            aws_sdk_guardduty.types.public_access_configuration.deserialize_json(
                data["bucketPublicAccess"]
            )
        )
    if "s3ObjectUids" in data:
        import aws_sdk_guardduty.types.s3_object_uids

        out["s3_object_uids"] = aws_sdk_guardduty.types.s3_object_uids.deserialize_json(
            data["s3ObjectUids"]
        )
    return out
