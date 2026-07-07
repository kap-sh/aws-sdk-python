"""Generated from Smithy shape ``com.amazonaws.qconnect#SelfServiceConversationHistory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_qconnect.types.sensitive_string


class SelfServiceConversationHistory(TypedDict, closed=True):
    turn_number: "int"
    """<p>The number of turn of the conversation history data.</p>"""
    input_transcript: NotRequired[
        "aws_sdk_qconnect.types.sensitive_string.SensitiveString"
    ]
    """<p>The input transcript of the conversation history data.</p>"""
    bot_response: NotRequired["aws_sdk_qconnect.types.sensitive_string.SensitiveString"]
    """<p>The bot response of the conversation history data.</p>"""
    timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of the conversation history entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelfServiceConversationHistory) -> dict:
    out: dict = {}
    out["turnNumber"] = value.get("turn_number", 0)
    if "input_transcript" in value:
        out["inputTranscript"] = value["input_transcript"]
    if "bot_response" in value:
        out["botResponse"] = value["bot_response"]
    if "timestamp" in value:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["timestamp"] = aws_sdk_qconnect.types._prelude.timestamp.serialize_json(
            value["timestamp"]
        )
    return out


def deserialize_json(data: dict) -> SelfServiceConversationHistory:
    out: SelfServiceConversationHistory = {}  # type: ignore[typeddict-item]
    if "turnNumber" in data:
        out["turn_number"] = data["turnNumber"]
    else:
        out["turn_number"] = 0
    if "inputTranscript" in data:
        out["input_transcript"] = data["inputTranscript"]
    if "botResponse" in data:
        out["bot_response"] = data["botResponse"]
    if "timestamp" in data:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["timestamp"] = aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
            data["timestamp"]
        )
    return out
