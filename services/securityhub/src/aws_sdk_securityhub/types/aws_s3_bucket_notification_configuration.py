"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketNotificationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_details


class AwsS3BucketNotificationConfiguration(TypedDict):
    configurations: NotRequired[
        "aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_details.AwsS3BucketNotificationConfigurationDetails"
    ]
    """<p>Configurations for S3 bucket notifications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketNotificationConfiguration) -> dict:
    out: dict = {}
    if "configurations" in value:
        import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_details

        out["Configurations"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_details.serialize_json(
                value["configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsS3BucketNotificationConfiguration:
    out: AwsS3BucketNotificationConfiguration = {}  # type: ignore[typeddict-item]
    if "Configurations" in data:
        import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_details

        out["configurations"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_details.deserialize_json(
                data["Configurations"]
            )
        )
    return out
