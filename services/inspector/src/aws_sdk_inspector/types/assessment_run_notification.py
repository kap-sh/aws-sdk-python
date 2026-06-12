"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentRunNotification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.arn
    import aws_sdk_inspector.types.assessment_run_notification_sns_status_code
    import aws_sdk_inspector.types.bool
    import aws_sdk_inspector.types.inspector_event
    import aws_sdk_inspector.types.message
    import aws_sdk_inspector.types.timestamp


class AssessmentRunNotification(TypedDict):
    date: "aws_sdk_inspector.types.timestamp.Timestamp"
    """<p>The date of the notification.</p>"""
    event: "aws_sdk_inspector.types.inspector_event.InspectorEvent"
    """<p>The event for which a notification is sent.</p>"""
    message: NotRequired["aws_sdk_inspector.types.message.Message"]
    """<p>The message included in the notification.</p>"""
    error: "aws_sdk_inspector.types.bool.Bool"
    """<p>The Boolean value that specifies whether the notification represents an error.</p>"""
    sns_topic_arn: NotRequired["aws_sdk_inspector.types.arn.Arn"]
    """<p>The SNS topic to which the SNS notification is sent.</p>"""
    sns_publish_status_code: NotRequired[
        "aws_sdk_inspector.types.assessment_run_notification_sns_status_code.AssessmentRunNotificationSnsStatusCode"
    ]
    """<p>The status code of the SNS notification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentRunNotification) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.timestamp

    out["date"] = aws_sdk_inspector.types.timestamp.serialize_aws_json_1_1(
        value["date"]
    )
    import aws_sdk_inspector.types.inspector_event

    out["event"] = aws_sdk_inspector.types.inspector_event.serialize_aws_json_1_1(
        value["event"]
    )
    if "message" in value:
        out["message"] = value["message"]
    out["error"] = value["error"]
    if "sns_topic_arn" in value:
        out["snsTopicArn"] = value["sns_topic_arn"]
    if "sns_publish_status_code" in value:
        import aws_sdk_inspector.types.assessment_run_notification_sns_status_code

        out["snsPublishStatusCode"] = (
            aws_sdk_inspector.types.assessment_run_notification_sns_status_code.serialize_aws_json_1_1(
                value["sns_publish_status_code"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssessmentRunNotification:
    out: AssessmentRunNotification = {}  # type: ignore[typeddict-item]
    if "date" in data:
        import aws_sdk_inspector.types.timestamp

        out["date"] = aws_sdk_inspector.types.timestamp.deserialize_aws_json_1_1(
            data["date"]
        )
    else:
        raise DeserializationError("AssessmentRunNotification.date required")
    if "event" in data:
        import aws_sdk_inspector.types.inspector_event

        out["event"] = aws_sdk_inspector.types.inspector_event.deserialize_aws_json_1_1(
            data["event"]
        )
    else:
        raise DeserializationError("AssessmentRunNotification.event required")
    if "message" in data:
        out["message"] = data["message"]
    if "error" in data:
        out["error"] = data["error"]
    else:
        raise DeserializationError("AssessmentRunNotification.error required")
    if "snsTopicArn" in data:
        out["sns_topic_arn"] = data["snsTopicArn"]
    if "snsPublishStatusCode" in data:
        import aws_sdk_inspector.types.assessment_run_notification_sns_status_code

        out["sns_publish_status_code"] = (
            aws_sdk_inspector.types.assessment_run_notification_sns_status_code.deserialize_aws_json_1_1(
                data["snsPublishStatusCode"]
            )
        )
    return out
