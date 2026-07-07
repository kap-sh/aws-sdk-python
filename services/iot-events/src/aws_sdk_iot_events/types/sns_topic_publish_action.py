"""Generated from Smithy shape ``com.amazonaws.iotevents#SNSTopicPublishAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.amazon_resource_name
    import aws_sdk_iot_events.types.payload


class SNSTopicPublishAction(TypedDict, closed=True):
    target_arn: "aws_sdk_iot_events.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the Amazon SNS target where the message is sent.</p>"""
    payload: NotRequired["aws_sdk_iot_events.types.payload.Payload"]
    """<p>You can configure the action payload when you send a message as an Amazon SNS push notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SNSTopicPublishAction) -> dict:
    out: dict = {}
    out["targetArn"] = value["target_arn"]
    if "payload" in value:
        import aws_sdk_iot_events.types.payload

        out["payload"] = aws_sdk_iot_events.types.payload.serialize_json(
            value["payload"]
        )
    return out


def deserialize_json(data: dict) -> SNSTopicPublishAction:
    out: SNSTopicPublishAction = {}  # type: ignore[typeddict-item]
    if "targetArn" in data:
        out["target_arn"] = data["targetArn"]
    else:
        raise DeserializationError("SNSTopicPublishAction.target_arn required")
    if "payload" in data:
        import aws_sdk_iot_events.types.payload

        out["payload"] = aws_sdk_iot_events.types.payload.deserialize_json(
            data["payload"]
        )
    return out
