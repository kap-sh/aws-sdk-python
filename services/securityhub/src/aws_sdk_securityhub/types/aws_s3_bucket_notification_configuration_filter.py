"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketNotificationConfigurationFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter


class AwsS3BucketNotificationConfigurationFilter(TypedDict):
    s3_key_filter: NotRequired[
        "aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter.AwsS3BucketNotificationConfigurationS3KeyFilter"
    ]
    """<p>Details for an Amazon S3 filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketNotificationConfigurationFilter) -> dict:
    out: dict = {}
    if "s3_key_filter" in value:
        import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter

        out["S3KeyFilter"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter.serialize_json(
                value["s3_key_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsS3BucketNotificationConfigurationFilter:
    out: AwsS3BucketNotificationConfigurationFilter = {}  # type: ignore[typeddict-item]
    if "S3KeyFilter" in data:
        import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter

        out["s3_key_filter"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter.deserialize_json(
                data["S3KeyFilter"]
            )
        )
    return out
