"""Generated from Smithy shape ``com.amazonaws.connectparticipant#MessageProcessingMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectparticipant.types.message_processing_status


class MessageProcessingMetadata(TypedDict, closed=True):
    message_processing_status: NotRequired[
        "capo_connectparticipant.types.message_processing_status.MessageProcessingStatus"
    ]
    """<p>The status of Message Processing for the message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageProcessingMetadata) -> dict:
    out: dict = {}
    if "message_processing_status" in value:
        import capo_connectparticipant.types.message_processing_status

        out["MessageProcessingStatus"] = (
            capo_connectparticipant.types.message_processing_status.serialize_json(
                value["message_processing_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> MessageProcessingMetadata:
    out: MessageProcessingMetadata = {}  # type: ignore[typeddict-item]
    if "MessageProcessingStatus" in data:
        import capo_connectparticipant.types.message_processing_status

        out["message_processing_status"] = (
            capo_connectparticipant.types.message_processing_status.deserialize_json(
                data["MessageProcessingStatus"]
            )
        )
    return out
