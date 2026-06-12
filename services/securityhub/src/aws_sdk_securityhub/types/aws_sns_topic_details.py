"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsSnsTopicDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_sns_topic_subscription_list
    import aws_sdk_securityhub.types.non_empty_string


class AwsSnsTopicDetails(TypedDict):
    kms_master_key_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of an Amazon Web Services managed key for Amazon SNS or a customer managed key.</p>"""
    subscription: NotRequired[
        "aws_sdk_securityhub.types.aws_sns_topic_subscription_list.AwsSnsTopicSubscriptionList"
    ]
    """<p>Subscription is an embedded property that describes the subscription endpoints of an Amazon SNS topic.</p>"""
    topic_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the Amazon SNS topic.</p>"""
    owner: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The subscription's owner.</p>"""
    sqs_success_feedback_role_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint. </p>"""
    sqs_failure_feedback_role_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint. </p>"""
    application_success_feedback_role_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates failed message delivery status for an Amazon SNS topic that is subscribed to a platform application endpoint. </p>"""
    firehose_success_feedback_role_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Amazon Kinesis Data Firehose endpoint. </p>"""
    firehose_failure_feedback_role_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Amazon Kinesis Data Firehose endpoint. </p>"""
    http_success_feedback_role_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an HTTP endpoint. </p>"""
    http_failure_feedback_role_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an HTTP endpoint. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsSnsTopicDetails) -> dict:
    out: dict = {}
    if "kms_master_key_id" in value:
        out["KmsMasterKeyId"] = value["kms_master_key_id"]
    if "subscription" in value:
        import aws_sdk_securityhub.types.aws_sns_topic_subscription_list

        out["Subscription"] = (
            aws_sdk_securityhub.types.aws_sns_topic_subscription_list.serialize_json(
                value["subscription"]
            )
        )
    if "topic_name" in value:
        out["TopicName"] = value["topic_name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "sqs_success_feedback_role_arn" in value:
        out["SqsSuccessFeedbackRoleArn"] = value["sqs_success_feedback_role_arn"]
    if "sqs_failure_feedback_role_arn" in value:
        out["SqsFailureFeedbackRoleArn"] = value["sqs_failure_feedback_role_arn"]
    if "application_success_feedback_role_arn" in value:
        out["ApplicationSuccessFeedbackRoleArn"] = value[
            "application_success_feedback_role_arn"
        ]
    if "firehose_success_feedback_role_arn" in value:
        out["FirehoseSuccessFeedbackRoleArn"] = value[
            "firehose_success_feedback_role_arn"
        ]
    if "firehose_failure_feedback_role_arn" in value:
        out["FirehoseFailureFeedbackRoleArn"] = value[
            "firehose_failure_feedback_role_arn"
        ]
    if "http_success_feedback_role_arn" in value:
        out["HttpSuccessFeedbackRoleArn"] = value["http_success_feedback_role_arn"]
    if "http_failure_feedback_role_arn" in value:
        out["HttpFailureFeedbackRoleArn"] = value["http_failure_feedback_role_arn"]
    return out


def deserialize_json(data: dict) -> AwsSnsTopicDetails:
    out: AwsSnsTopicDetails = {}  # type: ignore[typeddict-item]
    if "KmsMasterKeyId" in data:
        out["kms_master_key_id"] = data["KmsMasterKeyId"]
    if "Subscription" in data:
        import aws_sdk_securityhub.types.aws_sns_topic_subscription_list

        out["subscription"] = (
            aws_sdk_securityhub.types.aws_sns_topic_subscription_list.deserialize_json(
                data["Subscription"]
            )
        )
    if "TopicName" in data:
        out["topic_name"] = data["TopicName"]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "SqsSuccessFeedbackRoleArn" in data:
        out["sqs_success_feedback_role_arn"] = data["SqsSuccessFeedbackRoleArn"]
    if "SqsFailureFeedbackRoleArn" in data:
        out["sqs_failure_feedback_role_arn"] = data["SqsFailureFeedbackRoleArn"]
    if "ApplicationSuccessFeedbackRoleArn" in data:
        out["application_success_feedback_role_arn"] = data[
            "ApplicationSuccessFeedbackRoleArn"
        ]
    if "FirehoseSuccessFeedbackRoleArn" in data:
        out["firehose_success_feedback_role_arn"] = data[
            "FirehoseSuccessFeedbackRoleArn"
        ]
    if "FirehoseFailureFeedbackRoleArn" in data:
        out["firehose_failure_feedback_role_arn"] = data[
            "FirehoseFailureFeedbackRoleArn"
        ]
    if "HttpSuccessFeedbackRoleArn" in data:
        out["http_success_feedback_role_arn"] = data["HttpSuccessFeedbackRoleArn"]
    if "HttpFailureFeedbackRoleArn" in data:
        out["http_failure_feedback_role_arn"] = data["HttpFailureFeedbackRoleArn"]
    return out
