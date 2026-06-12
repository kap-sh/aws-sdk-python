"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotLocaleHistoryEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_locale_history_event_description
    import aws_sdk_lex_models_v2.types.timestamp


class BotLocaleHistoryEvent(TypedDict):
    event: "aws_sdk_lex_models_v2.types.bot_locale_history_event_description.BotLocaleHistoryEventDescription"
    """<p>A description of the event that occurred.</p>"""
    event_date: "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    """<p>A timestamp of the date and time that the event occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotLocaleHistoryEvent) -> dict:
    out: dict = {}
    out["event"] = value["event"]
    import aws_sdk_lex_models_v2.types.timestamp

    out["eventDate"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
        value["event_date"]
    )
    return out


def deserialize_json(data: dict) -> BotLocaleHistoryEvent:
    out: BotLocaleHistoryEvent = {}  # type: ignore[typeddict-item]
    if "event" in data:
        out["event"] = data["event"]
    else:
        raise DeserializationError("BotLocaleHistoryEvent.event required")
    if "eventDate" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["event_date"] = aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
            data["eventDate"]
        )
    else:
        raise DeserializationError("BotLocaleHistoryEvent.event_date required")
    return out
