"""Generated from Smithy shape ``com.amazonaws.guardduty#S3BucketDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.default_server_side_encryption
    import aws_sdk_guardduty.types.owner
    import aws_sdk_guardduty.types.public_access
    import aws_sdk_guardduty.types.s3_object_details
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.tags
    import aws_sdk_guardduty.types.timestamp


class S3BucketDetail(TypedDict):
    arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the S3 bucket.</p>"""
    name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the S3 bucket.</p>"""
    type: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Describes whether the bucket is a source or destination bucket.</p>"""
    created_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The date and time the bucket was created at.</p>"""
    owner: NotRequired["aws_sdk_guardduty.types.owner.Owner"]
    """<p>The owner of the S3 bucket.</p>"""
    tags: NotRequired["aws_sdk_guardduty.types.tags.Tags"]
    """<p>All tags attached to the S3 bucket</p>"""
    default_server_side_encryption: NotRequired[
        "aws_sdk_guardduty.types.default_server_side_encryption.DefaultServerSideEncryption"
    ]
    """<p>Describes the server side encryption method used in the S3 bucket.</p>"""
    public_access: NotRequired["aws_sdk_guardduty.types.public_access.PublicAccess"]
    """<p>Describes the public access policies that apply to the S3 bucket.</p>"""
    s3_object_details: NotRequired[
        "aws_sdk_guardduty.types.s3_object_details.S3ObjectDetails"
    ]
    """<p>Information about the S3 object that was scanned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3BucketDetail) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    if "created_at" in value:
        import aws_sdk_guardduty.types.timestamp

        out["createdAt"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "owner" in value:
        import aws_sdk_guardduty.types.owner

        out["owner"] = aws_sdk_guardduty.types.owner.serialize_json(value["owner"])
    if "tags" in value:
        import aws_sdk_guardduty.types.tags

        out["tags"] = aws_sdk_guardduty.types.tags.serialize_json(value["tags"])
    if "default_server_side_encryption" in value:
        import aws_sdk_guardduty.types.default_server_side_encryption

        out["defaultServerSideEncryption"] = (
            aws_sdk_guardduty.types.default_server_side_encryption.serialize_json(
                value["default_server_side_encryption"]
            )
        )
    if "public_access" in value:
        import aws_sdk_guardduty.types.public_access

        out["publicAccess"] = aws_sdk_guardduty.types.public_access.serialize_json(
            value["public_access"]
        )
    if "s3_object_details" in value:
        import aws_sdk_guardduty.types.s3_object_details

        out["s3ObjectDetails"] = (
            aws_sdk_guardduty.types.s3_object_details.serialize_json(
                value["s3_object_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3BucketDetail:
    out: S3BucketDetail = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        out["type"] = data["type"]
    if "createdAt" in data:
        import aws_sdk_guardduty.types.timestamp

        out["created_at"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "owner" in data:
        import aws_sdk_guardduty.types.owner

        out["owner"] = aws_sdk_guardduty.types.owner.deserialize_json(data["owner"])
    if "tags" in data:
        import aws_sdk_guardduty.types.tags

        out["tags"] = aws_sdk_guardduty.types.tags.deserialize_json(data["tags"])
    if "defaultServerSideEncryption" in data:
        import aws_sdk_guardduty.types.default_server_side_encryption

        out["default_server_side_encryption"] = (
            aws_sdk_guardduty.types.default_server_side_encryption.deserialize_json(
                data["defaultServerSideEncryption"]
            )
        )
    if "publicAccess" in data:
        import aws_sdk_guardduty.types.public_access

        out["public_access"] = aws_sdk_guardduty.types.public_access.deserialize_json(
            data["publicAccess"]
        )
    if "s3ObjectDetails" in data:
        import aws_sdk_guardduty.types.s3_object_details

        out["s3_object_details"] = (
            aws_sdk_guardduty.types.s3_object_details.deserialize_json(
                data["s3ObjectDetails"]
            )
        )
    return out
