"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketNotificationConfigurationS3KeyFilterRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter_rule_name
    import aws_sdk_securityhub.types.non_empty_string


class AwsS3BucketNotificationConfigurationS3KeyFilterRule(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter_rule_name.AwsS3BucketNotificationConfigurationS3KeyFilterRuleName"
    ]
    """<p>Indicates whether the filter is based on the prefix or suffix of the Amazon S3 key.</p>"""
    value: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The filter value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketNotificationConfigurationS3KeyFilterRule) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter_rule_name

        out["Name"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter_rule_name.serialize_json(
                value["name"]
            )
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AwsS3BucketNotificationConfigurationS3KeyFilterRule:
    out: AwsS3BucketNotificationConfigurationS3KeyFilterRule = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter_rule_name

        out["name"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_s3_key_filter_rule_name.deserialize_json(
                data["Name"]
            )
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
