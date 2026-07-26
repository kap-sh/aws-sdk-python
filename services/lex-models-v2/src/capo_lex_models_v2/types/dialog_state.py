"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DialogState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.dialog_action
    import capo_lex_models_v2.types.intent_override
    import capo_lex_models_v2.types.string_map


class DialogState(TypedDict, closed=True):
    dialog_action: NotRequired["capo_lex_models_v2.types.dialog_action.DialogAction"]
    intent: NotRequired["capo_lex_models_v2.types.intent_override.IntentOverride"]
    session_attributes: NotRequired["capo_lex_models_v2.types.string_map.StringMap"]
    """<p>Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex and a client application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DialogState) -> dict:
    out: dict = {}
    if "dialog_action" in value:
        import capo_lex_models_v2.types.dialog_action

        out["dialogAction"] = capo_lex_models_v2.types.dialog_action.serialize_json(
            value["dialog_action"]
        )
    if "intent" in value:
        import capo_lex_models_v2.types.intent_override

        out["intent"] = capo_lex_models_v2.types.intent_override.serialize_json(
            value["intent"]
        )
    if "session_attributes" in value:
        import capo_lex_models_v2.types.string_map

        out["sessionAttributes"] = capo_lex_models_v2.types.string_map.serialize_json(
            value["session_attributes"]
        )
    return out


def deserialize_json(data: dict) -> DialogState:
    out: DialogState = {}  # type: ignore[typeddict-item]
    if "dialogAction" in data:
        import capo_lex_models_v2.types.dialog_action

        out["dialog_action"] = capo_lex_models_v2.types.dialog_action.deserialize_json(
            data["dialogAction"]
        )
    if "intent" in data:
        import capo_lex_models_v2.types.intent_override

        out["intent"] = capo_lex_models_v2.types.intent_override.deserialize_json(
            data["intent"]
        )
    if "sessionAttributes" in data:
        import capo_lex_models_v2.types.string_map

        out["session_attributes"] = (
            capo_lex_models_v2.types.string_map.deserialize_json(
                data["sessionAttributes"]
            )
        )
    return out
