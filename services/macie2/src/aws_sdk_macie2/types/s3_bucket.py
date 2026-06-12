"""Generated from Smithy shape ``com.amazonaws.macie2#S3Bucket``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.__timestamp_iso8601
    import aws_sdk_macie2.types.allows_unencrypted_object_uploads
    import aws_sdk_macie2.types.bucket_public_access
    import aws_sdk_macie2.types.key_value_pair_list
    import aws_sdk_macie2.types.s3_bucket_owner
    import aws_sdk_macie2.types.server_side_encryption


class S3Bucket(TypedDict):
    allows_unencrypted_object_uploads: NotRequired[
        "aws_sdk_macie2.types.allows_unencrypted_object_uploads.AllowsUnencryptedObjectUploads"
    ]
    """<p>Specifies whether the bucket policy for the bucket requires server-side encryption of objects when objects are added to the bucket. Possible values are:</p> <ul><li><p>FALSE - The bucket policy requires server-side encryption of new objects. PutObject requests must include a valid server-side encryption header.</p></li> <li><p>TRUE - The bucket doesn't have a bucket policy or it has a bucket policy that doesn't require server-side encryption of new objects. If a bucket policy exists, it doesn't require PutObject requests to include a valid server-side encryption header.</p></li> <li><p>UNKNOWN - Amazon Macie can't determine whether the bucket policy requires server-side encryption of new objects.</p></li></ul> <p>Valid server-side encryption headers are: x-amz-server-side-encryption with a value of AES256 or aws:kms, and x-amz-server-side-encryption-customer-algorithm with a value of AES256.</p>"""
    arn: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the bucket.</p>"""
    created_at: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the bucket was created. This value can also indicate when changes such as edits to the bucket's policy were most recently made to the bucket, relative to when the finding was created or last updated.</p>"""
    default_server_side_encryption: NotRequired[
        "aws_sdk_macie2.types.server_side_encryption.ServerSideEncryption"
    ]
    """<p>The default server-side encryption settings for the bucket.</p>"""
    name: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The name of the bucket.</p>"""
    owner: NotRequired["aws_sdk_macie2.types.s3_bucket_owner.S3BucketOwner"]
    """<p>The display name and canonical user ID for the Amazon Web Services account that owns the bucket.</p>"""
    public_access: NotRequired[
        "aws_sdk_macie2.types.bucket_public_access.BucketPublicAccess"
    ]
    """<p>The permissions settings that determine whether the bucket is publicly accessible.</p>"""
    tags: NotRequired["aws_sdk_macie2.types.key_value_pair_list.KeyValuePairList"]
    """<p>The tags that are associated with the bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Bucket) -> dict:
    out: dict = {}
    if "allows_unencrypted_object_uploads" in value:
        import aws_sdk_macie2.types.allows_unencrypted_object_uploads

        out["allowsUnencryptedObjectUploads"] = (
            aws_sdk_macie2.types.allows_unencrypted_object_uploads.serialize_json(
                value["allows_unencrypted_object_uploads"]
            )
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["createdAt"] = aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
            value["created_at"]
        )
    if "default_server_side_encryption" in value:
        import aws_sdk_macie2.types.server_side_encryption

        out["defaultServerSideEncryption"] = (
            aws_sdk_macie2.types.server_side_encryption.serialize_json(
                value["default_server_side_encryption"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "owner" in value:
        import aws_sdk_macie2.types.s3_bucket_owner

        out["owner"] = aws_sdk_macie2.types.s3_bucket_owner.serialize_json(
            value["owner"]
        )
    if "public_access" in value:
        import aws_sdk_macie2.types.bucket_public_access

        out["publicAccess"] = aws_sdk_macie2.types.bucket_public_access.serialize_json(
            value["public_access"]
        )
    if "tags" in value:
        import aws_sdk_macie2.types.key_value_pair_list

        out["tags"] = aws_sdk_macie2.types.key_value_pair_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> S3Bucket:
    out: S3Bucket = {}  # type: ignore[typeddict-item]
    if "allowsUnencryptedObjectUploads" in data:
        import aws_sdk_macie2.types.allows_unencrypted_object_uploads

        out["allows_unencrypted_object_uploads"] = (
            aws_sdk_macie2.types.allows_unencrypted_object_uploads.deserialize_json(
                data["allowsUnencryptedObjectUploads"]
            )
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["created_at"] = aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
            data["createdAt"]
        )
    if "defaultServerSideEncryption" in data:
        import aws_sdk_macie2.types.server_side_encryption

        out["default_server_side_encryption"] = (
            aws_sdk_macie2.types.server_side_encryption.deserialize_json(
                data["defaultServerSideEncryption"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "owner" in data:
        import aws_sdk_macie2.types.s3_bucket_owner

        out["owner"] = aws_sdk_macie2.types.s3_bucket_owner.deserialize_json(
            data["owner"]
        )
    if "publicAccess" in data:
        import aws_sdk_macie2.types.bucket_public_access

        out["public_access"] = (
            aws_sdk_macie2.types.bucket_public_access.deserialize_json(
                data["publicAccess"]
            )
        )
    if "tags" in data:
        import aws_sdk_macie2.types.key_value_pair_list

        out["tags"] = aws_sdk_macie2.types.key_value_pair_list.deserialize_json(
            data["tags"]
        )
    return out
