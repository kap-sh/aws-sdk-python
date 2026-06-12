"""Generated from Smithy shape ``com.amazonaws.ivschat#SendEventRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivschat.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivschat.types.event_attributes
    import aws_sdk_ivschat.types.event_name
    import aws_sdk_ivschat.types.room_identifier


class SendEventRequest(TypedDict):
    room_identifier: "aws_sdk_ivschat.types.room_identifier.RoomIdentifier"
    """<p>Identifier of the room to which the event will be sent. Currently this must be an ARN.</p>"""
    event_name: "aws_sdk_ivschat.types.event_name.EventName"
    """<p>Application-defined name of the event to send to clients.</p>"""
    attributes: NotRequired["aws_sdk_ivschat.types.event_attributes.EventAttributes"]
    """<p>Application-defined metadata to attach to the event sent to clients. The maximum length of the metadata is 1 KB total.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendEventRequest) -> dict:
    out: dict = {}
    out["roomIdentifier"] = value["room_identifier"]
    out["eventName"] = value["event_name"]
    if "attributes" in value:
        import aws_sdk_ivschat.types.event_attributes

        out["attributes"] = aws_sdk_ivschat.types.event_attributes.serialize_json(
            value["attributes"]
        )
    return out


def deserialize_json(data: dict) -> SendEventRequest:
    out: SendEventRequest = {}  # type: ignore[typeddict-item]
    if "roomIdentifier" in data:
        out["room_identifier"] = data["roomIdentifier"]
    else:
        raise DeserializationError("SendEventRequest.room_identifier required")
    if "eventName" in data:
        out["event_name"] = data["eventName"]
    else:
        raise DeserializationError("SendEventRequest.event_name required")
    if "attributes" in data:
        import aws_sdk_ivschat.types.event_attributes

        out["attributes"] = aws_sdk_ivschat.types.event_attributes.deserialize_json(
            data["attributes"]
        )
    return out
