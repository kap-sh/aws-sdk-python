"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_s3_account_public_access_block_details
    import aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_details
    import aws_sdk_securityhub.types.aws_s3_bucket_bucket_versioning_configuration
    import aws_sdk_securityhub.types.aws_s3_bucket_logging_configuration
    import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration
    import aws_sdk_securityhub.types.aws_s3_bucket_object_lock_configuration
    import aws_sdk_securityhub.types.aws_s3_bucket_server_side_encryption_configuration
    import aws_sdk_securityhub.types.aws_s3_bucket_website_configuration
    import aws_sdk_securityhub.types.non_empty_string


class AwsS3BucketDetails(TypedDict, closed=True):
    owner_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The canonical user ID of the owner of the S3 bucket.</p>"""
    owner_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The display name of the owner of the S3 bucket.</p>"""
    owner_account_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Web Services account identifier of the account that owns the S3 bucket.</p>"""
    created_at: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    r"""<p>Indicates when the S3 bucket was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    server_side_encryption_configuration: NotRequired[
        "aws_sdk_securityhub.types.aws_s3_bucket_server_side_encryption_configuration.AwsS3BucketServerSideEncryptionConfiguration"
    ]
    """<p>The encryption rules that are applied to the S3 bucket.</p>"""
    bucket_lifecycle_configuration: NotRequired[
        "aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_details.AwsS3BucketBucketLifecycleConfigurationDetails"
    ]
    """<p>The lifecycle configuration for objects in the specified bucket.</p>"""
    public_access_block_configuration: NotRequired[
        "aws_sdk_securityhub.types.aws_s3_account_public_access_block_details.AwsS3AccountPublicAccessBlockDetails"
    ]
    """<p>Provides information about the Amazon S3 Public Access Block configuration for the S3 bucket.</p>"""
    access_control_list: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The access control list for the S3 bucket.</p>"""
    bucket_logging_configuration: NotRequired[
        "aws_sdk_securityhub.types.aws_s3_bucket_logging_configuration.AwsS3BucketLoggingConfiguration"
    ]
    """<p>The logging configuration for the S3 bucket.</p>"""
    bucket_website_configuration: NotRequired[
        "aws_sdk_securityhub.types.aws_s3_bucket_website_configuration.AwsS3BucketWebsiteConfiguration"
    ]
    """<p>The website configuration parameters for the S3 bucket.</p>"""
    bucket_notification_configuration: NotRequired[
        "aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration.AwsS3BucketNotificationConfiguration"
    ]
    """<p>The notification configuration for the S3 bucket.</p>"""
    bucket_versioning_configuration: NotRequired[
        "aws_sdk_securityhub.types.aws_s3_bucket_bucket_versioning_configuration.AwsS3BucketBucketVersioningConfiguration"
    ]
    """<p>The versioning state of an S3 bucket.</p>"""
    object_lock_configuration: NotRequired[
        "aws_sdk_securityhub.types.aws_s3_bucket_object_lock_configuration.AwsS3BucketObjectLockConfiguration"
    ]
    """<p> Specifies which rule Amazon S3 applies by default to every new object placed in the bucket. </p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the bucket. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketDetails) -> dict:
    out: dict = {}
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "owner_name" in value:
        out["OwnerName"] = value["owner_name"]
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "created_at" in value:
        out["CreatedAt"] = value["created_at"]
    if "server_side_encryption_configuration" in value:
        import aws_sdk_securityhub.types.aws_s3_bucket_server_side_encryption_configuration

        out["ServerSideEncryptionConfiguration"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_server_side_encryption_configuration.serialize_json(
                value["server_side_encryption_configuration"]
            )
        )
    if "bucket_lifecycle_configuration" in value:
        import aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_details

        out["BucketLifecycleConfiguration"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_details.serialize_json(
                value["bucket_lifecycle_configuration"]
            )
        )
    if "public_access_block_configuration" in value:
        import aws_sdk_securityhub.types.aws_s3_account_public_access_block_details

        out["PublicAccessBlockConfiguration"] = (
            aws_sdk_securityhub.types.aws_s3_account_public_access_block_details.serialize_json(
                value["public_access_block_configuration"]
            )
        )
    if "access_control_list" in value:
        out["AccessControlList"] = value["access_control_list"]
    if "bucket_logging_configuration" in value:
        import aws_sdk_securityhub.types.aws_s3_bucket_logging_configuration

        out["BucketLoggingConfiguration"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_logging_configuration.serialize_json(
                value["bucket_logging_configuration"]
            )
        )
    if "bucket_website_configuration" in value:
        import aws_sdk_securityhub.types.aws_s3_bucket_website_configuration

        out["BucketWebsiteConfiguration"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_website_configuration.serialize_json(
                value["bucket_website_configuration"]
            )
        )
    if "bucket_notification_configuration" in value:
        import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration

        out["BucketNotificationConfiguration"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration.serialize_json(
                value["bucket_notification_configuration"]
            )
        )
    if "bucket_versioning_configuration" in value:
        import aws_sdk_securityhub.types.aws_s3_bucket_bucket_versioning_configuration

        out["BucketVersioningConfiguration"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_bucket_versioning_configuration.serialize_json(
                value["bucket_versioning_configuration"]
            )
        )
    if "object_lock_configuration" in value:
        import aws_sdk_securityhub.types.aws_s3_bucket_object_lock_configuration

        out["ObjectLockConfiguration"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_object_lock_configuration.serialize_json(
                value["object_lock_configuration"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AwsS3BucketDetails:
    out: AwsS3BucketDetails = {}  # type: ignore[typeddict-item]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "OwnerName" in data:
        out["owner_name"] = data["OwnerName"]
    if "OwnerAccountId" in data:
        out["owner_account_id"] = data["OwnerAccountId"]
    if "CreatedAt" in data:
        out["created_at"] = data["CreatedAt"]
    if "ServerSideEncryptionConfiguration" in data:
        import aws_sdk_securityhub.types.aws_s3_bucket_server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_server_side_encryption_configuration.deserialize_json(
                data["ServerSideEncryptionConfiguration"]
            )
        )
    if "BucketLifecycleConfiguration" in data:
        import aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_details

        out["bucket_lifecycle_configuration"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_details.deserialize_json(
                data["BucketLifecycleConfiguration"]
            )
        )
    if "PublicAccessBlockConfiguration" in data:
        import aws_sdk_securityhub.types.aws_s3_account_public_access_block_details

        out["public_access_block_configuration"] = (
            aws_sdk_securityhub.types.aws_s3_account_public_access_block_details.deserialize_json(
                data["PublicAccessBlockConfiguration"]
            )
        )
    if "AccessControlList" in data:
        out["access_control_list"] = data["AccessControlList"]
    if "BucketLoggingConfiguration" in data:
        import aws_sdk_securityhub.types.aws_s3_bucket_logging_configuration

        out["bucket_logging_configuration"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_logging_configuration.deserialize_json(
                data["BucketLoggingConfiguration"]
            )
        )
    if "BucketWebsiteConfiguration" in data:
        import aws_sdk_securityhub.types.aws_s3_bucket_website_configuration

        out["bucket_website_configuration"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_website_configuration.deserialize_json(
                data["BucketWebsiteConfiguration"]
            )
        )
    if "BucketNotificationConfiguration" in data:
        import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration

        out["bucket_notification_configuration"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration.deserialize_json(
                data["BucketNotificationConfiguration"]
            )
        )
    if "BucketVersioningConfiguration" in data:
        import aws_sdk_securityhub.types.aws_s3_bucket_bucket_versioning_configuration

        out["bucket_versioning_configuration"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_bucket_versioning_configuration.deserialize_json(
                data["BucketVersioningConfiguration"]
            )
        )
    if "ObjectLockConfiguration" in data:
        import aws_sdk_securityhub.types.aws_s3_bucket_object_lock_configuration

        out["object_lock_configuration"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_object_lock_configuration.deserialize_json(
                data["ObjectLockConfiguration"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    return out
