"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketNotificationConfigurationS3KeyFilterRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter_rule

AwsS3BucketNotificationConfigurationS3KeyFilterRules: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter_rule.AwsS3BucketNotificationConfigurationS3KeyFilterRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketNotificationConfigurationS3KeyFilterRules) -> list:
    import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter_rule.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsS3BucketNotificationConfigurationS3KeyFilterRules:
    import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter_rule

    out: AwsS3BucketNotificationConfigurationS3KeyFilterRules = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter_rule.deserialize_json(
                item
            )
        )
    return out
