"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketNotificationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_s3_bucket_notification_configuration_details


class AwsS3BucketNotificationConfiguration(TypedDict, closed=True):
    configurations: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_notification_configuration_details.AwsS3BucketNotificationConfigurationDetails"
    ]
    """<p>Configurations for S3 bucket notifications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketNotificationConfiguration) -> dict:
    out: dict = {}
    if "configurations" in value:
        import capo_securityhub.types.aws_s3_bucket_notification_configuration_details

        out["Configurations"] = (
            capo_securityhub.types.aws_s3_bucket_notification_configuration_details.serialize_json(
                value["configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsS3BucketNotificationConfiguration:
    out: AwsS3BucketNotificationConfiguration = {}  # type: ignore[typeddict-item]
    if "Configurations" in data:
        import capo_securityhub.types.aws_s3_bucket_notification_configuration_details

        out["configurations"] = (
            capo_securityhub.types.aws_s3_bucket_notification_configuration_details.deserialize_json(
                data["Configurations"]
            )
        )
    return out
