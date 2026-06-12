"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#TranscriptEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.event_id
    import aws_sdk_lex_runtime_v2.types.string


class TranscriptEvent(TypedDict):
    transcript: NotRequired["aws_sdk_lex_runtime_v2.types.string.String"]
    """<p>The transcript of the voice audio from the user.</p>"""
    event_id: NotRequired["aws_sdk_lex_runtime_v2.types.event_id.EventId"]
    """<p>A unique identifier of the event sent by Amazon Lex V2. The identifier is in the form <code>RESPONSE-N</code>, where N is a number starting with one and incremented for each event sent by Amazon Lex V2 in the current session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TranscriptEvent) -> dict:
    out: dict = {}
    if "transcript" in value:
        out["transcript"] = value["transcript"]
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    return out


def deserialize_json(data: dict) -> TranscriptEvent:
    out: TranscriptEvent = {}  # type: ignore[typeddict-item]
    if "transcript" in data:
        out["transcript"] = data["transcript"]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    return out
