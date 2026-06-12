"""Generated from Smithy shape ``com.amazonaws.connect#SendChatIntegrationEventRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.chat_event
    import aws_sdk_connect.types.destination_id
    import aws_sdk_connect.types.new_session_details
    import aws_sdk_connect.types.source_id
    import aws_sdk_connect.types.subtype


class SendChatIntegrationEventRequest(TypedDict):
    source_id: "aws_sdk_connect.types.source_id.SourceId"
    """<p>External identifier of chat customer participant, used in part to uniquely identify a chat. For SMS, this is the E164 phone number of the chat customer participant.</p>"""
    destination_id: "aws_sdk_connect.types.destination_id.DestinationId"
    """<p>Chat system identifier, used in part to uniquely identify chat. This is associated with the Connect Customer instance and flow to be used to start chats. For Server Migration Service, this is the phone number destination of inbound Server Migration Service messages represented by an Amazon Web Services End User Messaging phone number ARN.</p>"""
    subtype: NotRequired["aws_sdk_connect.types.subtype.Subtype"]
    """<p>Classification of a channel. This is used in part to uniquely identify chat. </p> <p>Valid value: <code>[\"connect:sms\", connect:\"WhatsApp\"]</code> </p>"""
    event: "aws_sdk_connect.types.chat_event.ChatEvent"
    """<p>Chat integration event payload</p>"""
    new_session_details: NotRequired[
        "aws_sdk_connect.types.new_session_details.NewSessionDetails"
    ]
    """<p>Contact properties to apply when starting a new chat. If the integration event is handled with an existing chat, this is ignored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendChatIntegrationEventRequest) -> dict:
    out: dict = {}
    out["SourceId"] = value["source_id"]
    out["DestinationId"] = value["destination_id"]
    if "subtype" in value:
        out["Subtype"] = value["subtype"]
    import aws_sdk_connect.types.chat_event

    out["Event"] = aws_sdk_connect.types.chat_event.serialize_json(value["event"])
    if "new_session_details" in value:
        import aws_sdk_connect.types.new_session_details

        out["NewSessionDetails"] = (
            aws_sdk_connect.types.new_session_details.serialize_json(
                value["new_session_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> SendChatIntegrationEventRequest:
    out: SendChatIntegrationEventRequest = {}  # type: ignore[typeddict-item]
    if "SourceId" in data:
        out["source_id"] = data["SourceId"]
    else:
        raise DeserializationError("SendChatIntegrationEventRequest.source_id required")
    if "DestinationId" in data:
        out["destination_id"] = data["DestinationId"]
    else:
        raise DeserializationError(
            "SendChatIntegrationEventRequest.destination_id required"
        )
    if "Subtype" in data:
        out["subtype"] = data["Subtype"]
    if "Event" in data:
        import aws_sdk_connect.types.chat_event

        out["event"] = aws_sdk_connect.types.chat_event.deserialize_json(data["Event"])
    else:
        raise DeserializationError("SendChatIntegrationEventRequest.event required")
    if "NewSessionDetails" in data:
        import aws_sdk_connect.types.new_session_details

        out["new_session_details"] = (
            aws_sdk_connect.types.new_session_details.deserialize_json(
                data["NewSessionDetails"]
            )
        )
    return out
