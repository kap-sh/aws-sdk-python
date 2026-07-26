"""Generated from Smithy shape ``com.amazonaws.chatbot#GetCustomActionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.custom_action


class GetCustomActionResult(TypedDict, closed=True):
    custom_action: NotRequired["capo_chatbot.types.custom_action.CustomAction"]
    """<p>Returns the custom action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCustomActionResult) -> dict:
    out: dict = {}
    if "custom_action" in value:
        import capo_chatbot.types.custom_action

        out["CustomAction"] = capo_chatbot.types.custom_action.serialize_json(
            value["custom_action"]
        )
    return out


def deserialize_json(data: dict) -> GetCustomActionResult:
    out: GetCustomActionResult = {}  # type: ignore[typeddict-item]
    if "CustomAction" in data:
        import capo_chatbot.types.custom_action

        out["custom_action"] = capo_chatbot.types.custom_action.deserialize_json(
            data["CustomAction"]
        )
    return out
