"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_qconnect.types.message_data
    import aws_sdk_qconnect.types.participant
    import aws_sdk_qconnect.types.uuid


class MessageOutput(TypedDict, closed=True):
    value: "aws_sdk_qconnect.types.message_data.MessageData"
    """<p>The value of a message data.</p>"""
    message_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of a message.</p>"""
    participant: "aws_sdk_qconnect.types.participant.Participant"
    """<p>The participant of a message.</p>"""
    timestamp: "datetime.datetime"
    """<p>The timestamp of a message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageOutput) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.message_data

    out["value"] = aws_sdk_qconnect.types.message_data.serialize_json(value["value"])
    out["messageId"] = value["message_id"]
    out["participant"] = value["participant"]
    import aws_sdk_qconnect.types._prelude.timestamp

    out["timestamp"] = aws_sdk_qconnect.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    return out


def deserialize_json(data: dict) -> MessageOutput:
    out: MessageOutput = {}  # type: ignore[typeddict-item]
    if "value" in data:
        import aws_sdk_qconnect.types.message_data

        out["value"] = aws_sdk_qconnect.types.message_data.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("MessageOutput.value required")
    if "messageId" in data:
        out["message_id"] = data["messageId"]
    else:
        raise DeserializationError("MessageOutput.message_id required")
    if "participant" in data:
        out["participant"] = data["participant"]
    else:
        raise DeserializationError("MessageOutput.participant required")
    if "timestamp" in data:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["timestamp"] = aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
            data["timestamp"]
        )
    else:
        raise DeserializationError("MessageOutput.timestamp required")
    return out
