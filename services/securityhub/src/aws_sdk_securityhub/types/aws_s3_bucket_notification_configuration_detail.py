"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketNotificationConfigurationDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_events
    import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_filter
    import aws_sdk_securityhub.types.non_empty_string


class AwsS3BucketNotificationConfigurationDetail(TypedDict, closed=True):
    events: NotRequired[
        "aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_events.AwsS3BucketNotificationConfigurationEvents"
    ]
    """<p>The list of events that trigger a notification.</p>"""
    filter: NotRequired[
        "aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_filter.AwsS3BucketNotificationConfigurationFilter"
    ]
    """<p>The filters that determine which S3 buckets generate notifications.</p>"""
    destination: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the Lambda function, Amazon SQS queue, or Amazon SNS topic that generates the notification.</p>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates the type of notification. Notifications can be generated using Lambda functions, Amazon SQS queues, or Amazon SNS topics, with corresponding valid values as follows:</p> <ul> <li> <p> <code>LambdaConfiguration</code> </p> </li> <li> <p> <code>QueueConfiguration</code> </p> </li> <li> <p> <code>TopicConfiguration</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketNotificationConfigurationDetail) -> dict:
    out: dict = {}
    if "events" in value:
        import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_events

        out["Events"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_events.serialize_json(
                value["events"]
            )
        )
    if "filter" in value:
        import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_filter

        out["Filter"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_filter.serialize_json(
                value["filter"]
            )
        )
    if "destination" in value:
        out["Destination"] = value["destination"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsS3BucketNotificationConfigurationDetail:
    out: AwsS3BucketNotificationConfigurationDetail = {}  # type: ignore[typeddict-item]
    if "Events" in data:
        import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_events

        out["events"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_events.deserialize_json(
                data["Events"]
            )
        )
    if "Filter" in data:
        import aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_filter

        out["filter"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_notification_configuration_filter.deserialize_json(
                data["Filter"]
            )
        )
    if "Destination" in data:
        out["destination"] = data["Destination"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
