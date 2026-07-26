"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#PlainTextMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.plain_text_message_value


class PlainTextMessage(TypedDict, closed=True):
    value: "capo_lex_models_v2.types.plain_text_message_value.PlainTextMessageValue"
    """<p>The message to send to the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PlainTextMessage) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> PlainTextMessage:
    out: PlainTextMessage = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("PlainTextMessage.value required")
    return out
