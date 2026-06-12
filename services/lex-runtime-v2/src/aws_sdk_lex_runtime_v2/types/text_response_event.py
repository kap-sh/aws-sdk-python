"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#TextResponseEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.event_id
    import aws_sdk_lex_runtime_v2.types.messages


class TextResponseEvent(TypedDict):
    messages: NotRequired["aws_sdk_lex_runtime_v2.types.messages.Messages"]
    """<p>A list of messages to send to the user. Messages are ordered based on the order that you returned the messages from your Lambda function or the order that the messages are defined in the bot.</p>"""
    event_id: NotRequired["aws_sdk_lex_runtime_v2.types.event_id.EventId"]
    """<p>A unique identifier of the event sent by Amazon Lex V2. The identifier is in the form <code>RESPONSE-N</code>, where N is a number starting with one and incremented for each event sent by Amazon Lex V2 in the current session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextResponseEvent) -> dict:
    out: dict = {}
    if "messages" in value:
        import aws_sdk_lex_runtime_v2.types.messages

        out["messages"] = aws_sdk_lex_runtime_v2.types.messages.serialize_json(
            value["messages"]
        )
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    return out


def deserialize_json(data: dict) -> TextResponseEvent:
    out: TextResponseEvent = {}  # type: ignore[typeddict-item]
    if "messages" in data:
        import aws_sdk_lex_runtime_v2.types.messages

        out["messages"] = aws_sdk_lex_runtime_v2.types.messages.deserialize_json(
            data["messages"]
        )
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    return out
