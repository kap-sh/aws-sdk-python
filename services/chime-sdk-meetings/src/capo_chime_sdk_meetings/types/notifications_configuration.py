"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#NotificationsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.arn


class NotificationsConfiguration(TypedDict, closed=True):
    lambda_function_arn: NotRequired["capo_chime_sdk_meetings.types.arn.Arn"]
    """<p>The ARN of the Amazon Web Services Lambda function in the notifications configuration.</p>"""
    sns_topic_arn: NotRequired["capo_chime_sdk_meetings.types.arn.Arn"]
    """<p>The ARN of the SNS topic.</p>"""
    sqs_queue_arn: NotRequired["capo_chime_sdk_meetings.types.arn.Arn"]
    """<p>The ARN of the SQS queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationsConfiguration) -> dict:
    out: dict = {}
    if "lambda_function_arn" in value:
        out["LambdaFunctionArn"] = value["lambda_function_arn"]
    if "sns_topic_arn" in value:
        out["SnsTopicArn"] = value["sns_topic_arn"]
    if "sqs_queue_arn" in value:
        out["SqsQueueArn"] = value["sqs_queue_arn"]
    return out


def deserialize_json(data: dict) -> NotificationsConfiguration:
    out: NotificationsConfiguration = {}  # type: ignore[typeddict-item]
    if "LambdaFunctionArn" in data:
        out["lambda_function_arn"] = data["LambdaFunctionArn"]
    if "SnsTopicArn" in data:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    if "SqsQueueArn" in data:
        out["sqs_queue_arn"] = data["SqsQueueArn"]
    return out
