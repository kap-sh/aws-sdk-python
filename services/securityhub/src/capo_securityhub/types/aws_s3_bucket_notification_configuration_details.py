"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketNotificationConfigurationDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_s3_bucket_notification_configuration_detail

AwsS3BucketNotificationConfigurationDetails: TypeAlias = list[
    "capo_securityhub.types.aws_s3_bucket_notification_configuration_detail.AwsS3BucketNotificationConfigurationDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketNotificationConfigurationDetails) -> list:
    import capo_securityhub.types.aws_s3_bucket_notification_configuration_detail

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_s3_bucket_notification_configuration_detail.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsS3BucketNotificationConfigurationDetails:
    import capo_securityhub.types.aws_s3_bucket_notification_configuration_detail

    out: AwsS3BucketNotificationConfigurationDetails = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_s3_bucket_notification_configuration_detail.deserialize_json(
                item
            )
        )
    return out
