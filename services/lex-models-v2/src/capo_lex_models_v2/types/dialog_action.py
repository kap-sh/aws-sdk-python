"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DialogAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boxed_boolean
    import capo_lex_models_v2.types.dialog_action_type
    import capo_lex_models_v2.types.name


class DialogAction(TypedDict, closed=True):
    type: "capo_lex_models_v2.types.dialog_action_type.DialogActionType"
    """<p>The action that the bot should execute. </p>"""
    slot_to_elicit: NotRequired["capo_lex_models_v2.types.name.Name"]
    """<p>If the dialog action is <code>ElicitSlot</code>, defines the slot to elicit from the user.</p>"""
    suppress_next_message: NotRequired[
        "capo_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>When true the next message for the intent is not used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DialogAction) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.dialog_action_type

    out["type"] = capo_lex_models_v2.types.dialog_action_type.serialize_json(
        value["type"]
    )
    if "slot_to_elicit" in value:
        out["slotToElicit"] = value["slot_to_elicit"]
    if "suppress_next_message" in value:
        out["suppressNextMessage"] = value["suppress_next_message"]
    return out


def deserialize_json(data: dict) -> DialogAction:
    out: DialogAction = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_lex_models_v2.types.dialog_action_type

        out["type"] = capo_lex_models_v2.types.dialog_action_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("DialogAction.type required")
    if "slotToElicit" in data:
        out["slot_to_elicit"] = data["slotToElicit"]
    if "suppressNextMessage" in data:
        out["suppress_next_message"] = data["suppressNextMessage"]
    return out
