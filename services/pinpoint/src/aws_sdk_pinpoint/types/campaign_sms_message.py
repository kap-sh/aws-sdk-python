"""Generated from Smithy shape ``com.amazonaws.pinpoint#CampaignSmsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.message_type


class CampaignSmsMessage(TypedDict):
    body: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The body of the SMS message.</p>"""
    message_type: NotRequired["aws_sdk_pinpoint.types.message_type.MessageType"]
    """<p>The SMS message type. Valid values are TRANSACTIONAL (for messages that are critical or time-sensitive, such as a one-time passwords) and PROMOTIONAL (for messsages that aren't critical or time-sensitive, such as marketing messages).</p>"""
    origination_number: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The long code to send the SMS message from. This value should be one of the dedicated long codes that's assigned to your AWS account. Although it isn't required, we recommend that you specify the long code using an E.164 format to ensure prompt and accurate delivery of the message. For example, +12065550100.</p>"""
    sender_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The sender ID to display on recipients' devices when they receive the SMS message.</p>"""
    entity_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The entity ID or Principal Entity (PE) id received from the regulatory body for sending SMS in your country.</p>"""
    template_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The template ID received from the regulatory body for sending SMS in your country.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CampaignSmsMessage) -> dict:
    out: dict = {}
    if "body" in value:
        out["Body"] = value["body"]
    if "message_type" in value:
        import aws_sdk_pinpoint.types.message_type

        out["MessageType"] = aws_sdk_pinpoint.types.message_type.serialize_json(
            value["message_type"]
        )
    if "origination_number" in value:
        out["OriginationNumber"] = value["origination_number"]
    if "sender_id" in value:
        out["SenderId"] = value["sender_id"]
    if "entity_id" in value:
        out["EntityId"] = value["entity_id"]
    if "template_id" in value:
        out["TemplateId"] = value["template_id"]
    return out


def deserialize_json(data: dict) -> CampaignSmsMessage:
    out: CampaignSmsMessage = {}  # type: ignore[typeddict-item]
    if "Body" in data:
        out["body"] = data["Body"]
    if "MessageType" in data:
        import aws_sdk_pinpoint.types.message_type

        out["message_type"] = aws_sdk_pinpoint.types.message_type.deserialize_json(
            data["MessageType"]
        )
    if "OriginationNumber" in data:
        out["origination_number"] = data["OriginationNumber"]
    if "SenderId" in data:
        out["sender_id"] = data["SenderId"]
    if "EntityId" in data:
        out["entity_id"] = data["EntityId"]
    if "TemplateId" in data:
        out["template_id"] = data["TemplateId"]
    return out
