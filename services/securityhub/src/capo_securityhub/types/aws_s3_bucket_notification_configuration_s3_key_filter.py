"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketNotificationConfigurationS3KeyFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter_rules


class AwsS3BucketNotificationConfigurationS3KeyFilter(TypedDict, closed=True):
    filter_rules: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter_rules.AwsS3BucketNotificationConfigurationS3KeyFilterRules"
    ]
    """<p>The filter rules for the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketNotificationConfigurationS3KeyFilter) -> dict:
    out: dict = {}
    if "filter_rules" in value:
        import capo_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter_rules

        out["FilterRules"] = (
            capo_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter_rules.serialize_json(
                value["filter_rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsS3BucketNotificationConfigurationS3KeyFilter:
    out: AwsS3BucketNotificationConfigurationS3KeyFilter = {}  # type: ignore[typeddict-item]
    if "FilterRules" in data:
        import capo_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter_rules

        out["filter_rules"] = (
            capo_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter_rules.deserialize_json(
                data["FilterRules"]
            )
        )
    return out
