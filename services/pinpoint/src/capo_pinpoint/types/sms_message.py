"""Generated from Smithy shape ``com.amazonaws.pinpoint#SMSMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.map_of_list_of__string
    import capo_pinpoint.types.message_type


class SMSMessage(TypedDict, closed=True):
    body: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The body of the SMS message.</p>"""
    keyword: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The SMS program name that you provided to AWS Support when you requested your dedicated number.</p>"""
    media_url: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>This field is reserved for future use.</p>"""
    message_type: NotRequired["capo_pinpoint.types.message_type.MessageType"]
    """<p>The SMS message type. Valid values are TRANSACTIONAL (for messages that are critical or time-sensitive, such as a one-time passwords) and PROMOTIONAL (for messsages that aren't critical or time-sensitive, such as marketing messages).</p>"""
    origination_number: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The number to send the SMS message from. This value should be one of the dedicated long or short codes that's assigned to your AWS account. If you don't specify a long or short code, Amazon Pinpoint assigns a random long code to the SMS message and sends the message from that code.</p>"""
    sender_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The sender ID to display as the sender of the message on a recipient's device. Support for sender IDs varies by country or region.</p>"""
    substitutions: NotRequired[
        "capo_pinpoint.types.map_of_list_of__string.MapOfListOf__string"
    ]
    """<p>The message variables to use in the SMS message. You can override the default variables with individual address variables.</p>"""
    entity_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The entity ID or Principal Entity (PE) id received from the regulatory body for sending SMS in your country.</p>"""
    template_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The template ID received from the regulatory body for sending SMS in your country.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SMSMessage) -> dict:
    out: dict = {}
    if "body" in value:
        out["Body"] = value["body"]
    if "keyword" in value:
        out["Keyword"] = value["keyword"]
    if "media_url" in value:
        out["MediaUrl"] = value["media_url"]
    if "message_type" in value:
        import capo_pinpoint.types.message_type

        out["MessageType"] = capo_pinpoint.types.message_type.serialize_json(
            value["message_type"]
        )
    if "origination_number" in value:
        out["OriginationNumber"] = value["origination_number"]
    if "sender_id" in value:
        out["SenderId"] = value["sender_id"]
    if "substitutions" in value:
        import capo_pinpoint.types.map_of_list_of__string

        out["Substitutions"] = (
            capo_pinpoint.types.map_of_list_of__string.serialize_json(
                value["substitutions"]
            )
        )
    if "entity_id" in value:
        out["EntityId"] = value["entity_id"]
    if "template_id" in value:
        out["TemplateId"] = value["template_id"]
    return out


def deserialize_json(data: dict) -> SMSMessage:
    out: SMSMessage = {}  # type: ignore[typeddict-item]
    if "Body" in data:
        out["body"] = data["Body"]
    if "Keyword" in data:
        out["keyword"] = data["Keyword"]
    if "MediaUrl" in data:
        out["media_url"] = data["MediaUrl"]
    if "MessageType" in data:
        import capo_pinpoint.types.message_type

        out["message_type"] = capo_pinpoint.types.message_type.deserialize_json(
            data["MessageType"]
        )
    if "OriginationNumber" in data:
        out["origination_number"] = data["OriginationNumber"]
    if "SenderId" in data:
        out["sender_id"] = data["SenderId"]
    if "Substitutions" in data:
        import capo_pinpoint.types.map_of_list_of__string

        out["substitutions"] = (
            capo_pinpoint.types.map_of_list_of__string.deserialize_json(
                data["Substitutions"]
            )
        )
    if "EntityId" in data:
        out["entity_id"] = data["EntityId"]
    if "TemplateId" in data:
        out["template_id"] = data["TemplateId"]
    return out
