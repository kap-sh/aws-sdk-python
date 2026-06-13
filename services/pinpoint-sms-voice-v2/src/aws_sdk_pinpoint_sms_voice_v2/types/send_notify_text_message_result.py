"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SendNotifyTextMessageResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_template_id


class SendNotifyTextMessageResult(TypedDict):
    message_id: NotRequired["str"]
    """<p>The unique identifier for the message.</p>"""
    template_id: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.notify_template_id.NotifyTemplateId"
    ]
    """<p>The unique identifier of the template used for the message.</p>"""
    resolved_message_body: NotRequired["str"]
    """<p>The message body after template variable substitution has been applied.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendNotifyTextMessageResult) -> dict:
    out: dict = {}
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    if "template_id" in value:
        out["TemplateId"] = value["template_id"]
    if "resolved_message_body" in value:
        out["ResolvedMessageBody"] = value["resolved_message_body"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SendNotifyTextMessageResult:
    out: SendNotifyTextMessageResult = {}  # type: ignore[typeddict-item]
    if "MessageId" in data:
        out["message_id"] = data["MessageId"]
    if "TemplateId" in data:
        out["template_id"] = data["TemplateId"]
    if "ResolvedMessageBody" in data:
        out["resolved_message_body"] = data["ResolvedMessageBody"]
    return out
