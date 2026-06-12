"""Generated from Smithy shape ``com.amazonaws.connectparticipant#MessageMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.chat_item_id
    import aws_sdk_connectparticipant.types.message_processing_status
    import aws_sdk_connectparticipant.types.receipts


class MessageMetadata(TypedDict):
    message_id: NotRequired["aws_sdk_connectparticipant.types.chat_item_id.ChatItemId"]
    """<p>The identifier of the message that contains the metadata information. </p>"""
    receipts: NotRequired["aws_sdk_connectparticipant.types.receipts.Receipts"]
    """<p>The list of receipt information for a message for different recipients.</p>"""
    message_processing_status: NotRequired[
        "aws_sdk_connectparticipant.types.message_processing_status.MessageProcessingStatus"
    ]
    """<p>The status of Message Processing for the message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageMetadata) -> dict:
    out: dict = {}
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    if "receipts" in value:
        import aws_sdk_connectparticipant.types.receipts

        out["Receipts"] = aws_sdk_connectparticipant.types.receipts.serialize_json(
            value["receipts"]
        )
    if "message_processing_status" in value:
        import aws_sdk_connectparticipant.types.message_processing_status

        out["MessageProcessingStatus"] = (
            aws_sdk_connectparticipant.types.message_processing_status.serialize_json(
                value["message_processing_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> MessageMetadata:
    out: MessageMetadata = {}  # type: ignore[typeddict-item]
    if "MessageId" in data:
        out["message_id"] = data["MessageId"]
    if "Receipts" in data:
        import aws_sdk_connectparticipant.types.receipts

        out["receipts"] = aws_sdk_connectparticipant.types.receipts.deserialize_json(
            data["Receipts"]
        )
    if "MessageProcessingStatus" in data:
        import aws_sdk_connectparticipant.types.message_processing_status

        out["message_processing_status"] = (
            aws_sdk_connectparticipant.types.message_processing_status.deserialize_json(
                data["MessageProcessingStatus"]
            )
        )
    return out
