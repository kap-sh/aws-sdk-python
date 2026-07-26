"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetBuiltinIntentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.builtin_intent_signature
    import capo_lex_model_building_service.types.builtin_intent_slot_list
    import capo_lex_model_building_service.types.locale_list


class GetBuiltinIntentResponse(TypedDict, closed=True):
    signature: NotRequired[
        "capo_lex_model_building_service.types.builtin_intent_signature.BuiltinIntentSignature"
    ]
    """<p>The unique identifier for a built-in intent.</p>"""
    supported_locales: NotRequired[
        "capo_lex_model_building_service.types.locale_list.LocaleList"
    ]
    """<p>A list of locales that the intent supports.</p>"""
    slots: NotRequired[
        "capo_lex_model_building_service.types.builtin_intent_slot_list.BuiltinIntentSlotList"
    ]
    """<p>An array of <code>BuiltinIntentSlot</code> objects, one entry for each slot type in the intent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBuiltinIntentResponse) -> dict:
    out: dict = {}
    if "signature" in value:
        out["signature"] = value["signature"]
    if "supported_locales" in value:
        import capo_lex_model_building_service.types.locale_list

        out["supportedLocales"] = (
            capo_lex_model_building_service.types.locale_list.serialize_json(
                value["supported_locales"]
            )
        )
    if "slots" in value:
        import capo_lex_model_building_service.types.builtin_intent_slot_list

        out["slots"] = (
            capo_lex_model_building_service.types.builtin_intent_slot_list.serialize_json(
                value["slots"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetBuiltinIntentResponse:
    out: GetBuiltinIntentResponse = {}  # type: ignore[typeddict-item]
    if "signature" in data:
        out["signature"] = data["signature"]
    if "supportedLocales" in data:
        import capo_lex_model_building_service.types.locale_list

        out["supported_locales"] = (
            capo_lex_model_building_service.types.locale_list.deserialize_json(
                data["supportedLocales"]
            )
        )
    if "slots" in data:
        import capo_lex_model_building_service.types.builtin_intent_slot_list

        out["slots"] = (
            capo_lex_model_building_service.types.builtin_intent_slot_list.deserialize_json(
                data["slots"]
            )
        )
    return out
