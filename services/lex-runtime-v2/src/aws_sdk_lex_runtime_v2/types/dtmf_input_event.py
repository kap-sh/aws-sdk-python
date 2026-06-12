"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#DTMFInputEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_runtime_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.dtmf_regex
    import aws_sdk_lex_runtime_v2.types.epoch_millis
    import aws_sdk_lex_runtime_v2.types.event_id


class DTMFInputEvent(TypedDict):
    input_character: "aws_sdk_lex_runtime_v2.types.dtmf_regex.DTMFRegex"
    """<p>The DTMF character that the user pressed. The allowed characters are A - D, 0 - 9, # and *.</p>"""
    event_id: NotRequired["aws_sdk_lex_runtime_v2.types.event_id.EventId"]
    """<p>A unique identifier that your application assigns to the event. You can use this to identify events in logs.</p>"""
    client_timestamp_millis: "aws_sdk_lex_runtime_v2.types.epoch_millis.EpochMillis"
    """<p>A timestamp set by the client of the date and time that the event was sent to Amazon Lex V2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DTMFInputEvent) -> dict:
    out: dict = {}
    out["inputCharacter"] = value["input_character"]
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    out["clientTimestampMillis"] = value.get("client_timestamp_millis", 0)
    return out


def deserialize_json(data: dict) -> DTMFInputEvent:
    out: DTMFInputEvent = {}  # type: ignore[typeddict-item]
    if "inputCharacter" in data:
        out["input_character"] = data["inputCharacter"]
    else:
        raise DeserializationError("DTMFInputEvent.input_character required")
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    if "clientTimestampMillis" in data:
        out["client_timestamp_millis"] = data["clientTimestampMillis"]
    else:
        out["client_timestamp_millis"] = 0
    return out
