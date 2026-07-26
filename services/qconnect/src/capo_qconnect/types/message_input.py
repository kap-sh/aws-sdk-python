"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.message_data


class MessageInput(TypedDict, closed=True):
    value: "capo_qconnect.types.message_data.MessageData"
    """<p>The message input value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageInput) -> dict:
    out: dict = {}
    import capo_qconnect.types.message_data

    out["value"] = capo_qconnect.types.message_data.serialize_json(value["value"])
    return out


def deserialize_json(data: dict) -> MessageInput:
    out: MessageInput = {}  # type: ignore[typeddict-item]
    if "value" in data:
        import capo_qconnect.types.message_data

        out["value"] = capo_qconnect.types.message_data.deserialize_json(data["value"])
    else:
        raise DeserializationError("MessageInput.value required")
    return out
