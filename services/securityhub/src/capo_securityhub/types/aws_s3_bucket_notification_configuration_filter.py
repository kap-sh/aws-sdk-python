"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketNotificationConfigurationFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter


class AwsS3BucketNotificationConfigurationFilter(TypedDict, closed=True):
    s3_key_filter: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter.AwsS3BucketNotificationConfigurationS3KeyFilter"
    ]
    """<p>Details for an Amazon S3 filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketNotificationConfigurationFilter) -> dict:
    out: dict = {}
    if "s3_key_filter" in value:
        import capo_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter

        out["S3KeyFilter"] = (
            capo_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter.serialize_json(
                value["s3_key_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsS3BucketNotificationConfigurationFilter:
    out: AwsS3BucketNotificationConfigurationFilter = {}  # type: ignore[typeddict-item]
    if "S3KeyFilter" in data:
        import capo_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter

        out["s3_key_filter"] = (
            capo_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter.deserialize_json(
                data["S3KeyFilter"]
            )
        )
    return out
