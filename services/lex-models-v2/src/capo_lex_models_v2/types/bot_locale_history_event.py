"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotLocaleHistoryEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_locale_history_event_description
    import capo_lex_models_v2.types.timestamp


class BotLocaleHistoryEvent(TypedDict, closed=True):
    event: "capo_lex_models_v2.types.bot_locale_history_event_description.BotLocaleHistoryEventDescription"
    """<p>A description of the event that occurred.</p>"""
    event_date: "capo_lex_models_v2.types.timestamp.Timestamp"
    """<p>A timestamp of the date and time that the event occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotLocaleHistoryEvent) -> dict:
    out: dict = {}
    out["event"] = value["event"]
    import capo_lex_models_v2.types.timestamp

    out["eventDate"] = capo_lex_models_v2.types.timestamp.serialize_json(
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
        import capo_lex_models_v2.types.timestamp

        out["event_date"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["eventDate"]
        )
    else:
        raise DeserializationError("BotLocaleHistoryEvent.event_date required")
    return out
