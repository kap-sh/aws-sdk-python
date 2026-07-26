"""Generated from Smithy shape ``com.amazonaws.connectparticipant#SendMessageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectparticipant.types.chat_item_id
    import capo_connectparticipant.types.instant
    import capo_connectparticipant.types.message_processing_metadata


class SendMessageResponse(TypedDict, closed=True):
    id: NotRequired["capo_connectparticipant.types.chat_item_id.ChatItemId"]
    """<p>The ID of the message.</p>"""
    absolute_time: NotRequired["capo_connectparticipant.types.instant.Instant"]
    """<p>The time when the message was sent.</p> <p>It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.</p>"""
    message_metadata: NotRequired[
        "capo_connectparticipant.types.message_processing_metadata.MessageProcessingMetadata"
    ]
    """<p>Contains metadata for the message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "absolute_time" in value:
        out["AbsoluteTime"] = value["absolute_time"]
    if "message_metadata" in value:
        import capo_connectparticipant.types.message_processing_metadata

        out["MessageMetadata"] = (
            capo_connectparticipant.types.message_processing_metadata.serialize_json(
                value["message_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> SendMessageResponse:
    out: SendMessageResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "AbsoluteTime" in data:
        out["absolute_time"] = data["AbsoluteTime"]
    if "MessageMetadata" in data:
        import capo_connectparticipant.types.message_processing_metadata

        out["message_metadata"] = (
            capo_connectparticipant.types.message_processing_metadata.deserialize_json(
                data["MessageMetadata"]
            )
        )
    return out
