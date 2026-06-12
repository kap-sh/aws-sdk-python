"""Generated from Smithy shape ``com.amazonaws.mediaconvert#S3DestinationSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.s3_destination_access_control
    import aws_sdk_mediaconvert.types.s3_encryption_settings
    import aws_sdk_mediaconvert.types.s3_storage_class


class S3DestinationSettings(TypedDict):
    access_control: NotRequired[
        "aws_sdk_mediaconvert.types.s3_destination_access_control.S3DestinationAccessControl"
    ]
    """Optional. Have MediaConvert automatically apply Amazon S3 access control for the outputs in this output group. When you don't use this setting, S3 automatically applies the default access control list PRIVATE."""
    encryption: NotRequired[
        "aws_sdk_mediaconvert.types.s3_encryption_settings.S3EncryptionSettings"
    ]
    """Settings for how your job outputs are encrypted as they are uploaded to Amazon S3."""
    storage_class: NotRequired[
        "aws_sdk_mediaconvert.types.s3_storage_class.S3StorageClass"
    ]
    """Specify the S3 storage class to use for this output. To use your destination's default storage class: Keep the default value, Not set. For more information about S3 storage classes, see https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html"""


# --- restJson1 ser/de ---
def serialize_json(value: S3DestinationSettings) -> dict:
    out: dict = {}
    if "access_control" in value:
        import aws_sdk_mediaconvert.types.s3_destination_access_control

        out["accessControl"] = (
            aws_sdk_mediaconvert.types.s3_destination_access_control.serialize_json(
                value["access_control"]
            )
        )
    if "encryption" in value:
        import aws_sdk_mediaconvert.types.s3_encryption_settings

        out["encryption"] = (
            aws_sdk_mediaconvert.types.s3_encryption_settings.serialize_json(
                value["encryption"]
            )
        )
    if "storage_class" in value:
        import aws_sdk_mediaconvert.types.s3_storage_class

        out["storageClass"] = (
            aws_sdk_mediaconvert.types.s3_storage_class.serialize_json(
                value["storage_class"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3DestinationSettings:
    out: S3DestinationSettings = {}  # type: ignore[typeddict-item]
    if "accessControl" in data:
        import aws_sdk_mediaconvert.types.s3_destination_access_control

        out["access_control"] = (
            aws_sdk_mediaconvert.types.s3_destination_access_control.deserialize_json(
                data["accessControl"]
            )
        )
    if "encryption" in data:
        import aws_sdk_mediaconvert.types.s3_encryption_settings

        out["encryption"] = (
            aws_sdk_mediaconvert.types.s3_encryption_settings.deserialize_json(
                data["encryption"]
            )
        )
    if "storageClass" in data:
        import aws_sdk_mediaconvert.types.s3_storage_class

        out["storage_class"] = (
            aws_sdk_mediaconvert.types.s3_storage_class.deserialize_json(
                data["storageClass"]
            )
        )
    return out
