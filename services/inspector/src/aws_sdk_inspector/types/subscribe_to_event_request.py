"""Generated from Smithy shape ``com.amazonaws.inspector#SubscribeToEventRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.arn
    import aws_sdk_inspector.types.inspector_event


class SubscribeToEventRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_inspector.types.arn.Arn"
    """<p>The ARN of the assessment template that is used during the event for which you want to receive SNS notifications.</p>"""
    event: "aws_sdk_inspector.types.inspector_event.InspectorEvent"
    """<p>The event for which you want to receive SNS notifications.</p>"""
    topic_arn: "aws_sdk_inspector.types.arn.Arn"
    """<p>The ARN of the SNS topic to which the SNS notifications are sent.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscribeToEventRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_inspector.types.inspector_event

    out["event"] = aws_sdk_inspector.types.inspector_event.serialize_aws_json_1_1(
        value["event"]
    )
    out["topicArn"] = value["topic_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SubscribeToEventRequest:
    out: SubscribeToEventRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("SubscribeToEventRequest.resource_arn required")
    if "event" in data:
        import aws_sdk_inspector.types.inspector_event

        out["event"] = aws_sdk_inspector.types.inspector_event.deserialize_aws_json_1_1(
            data["event"]
        )
    else:
        raise DeserializationError("SubscribeToEventRequest.event required")
    if "topicArn" in data:
        out["topic_arn"] = data["topicArn"]
    else:
        raise DeserializationError("SubscribeToEventRequest.topic_arn required")
    return out
