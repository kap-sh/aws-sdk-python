"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationLevelSlotResolutionResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.test_result_match_status
    import capo_lex_models_v2.types.test_result_slot_name


class ConversationLevelSlotResolutionResultItem(TypedDict, closed=True):
    intent_name: "capo_lex_models_v2.types.name.Name"
    """<p>The intents used in the slots list for the slot resolution details.</p>"""
    slot_name: "capo_lex_models_v2.types.test_result_slot_name.TestResultSlotName"
    """<p>The slot name in the slots list for the slot resolution details.</p>"""
    match_result: (
        "capo_lex_models_v2.types.test_result_match_status.TestResultMatchStatus"
    )
    """<p>The number of matching slots used in the slots listings for the slot resolution evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLevelSlotResolutionResultItem) -> dict:
    out: dict = {}
    out["intentName"] = value["intent_name"]
    out["slotName"] = value["slot_name"]
    import capo_lex_models_v2.types.test_result_match_status

    out["matchResult"] = (
        capo_lex_models_v2.types.test_result_match_status.serialize_json(
            value["match_result"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConversationLevelSlotResolutionResultItem:
    out: ConversationLevelSlotResolutionResultItem = {}  # type: ignore[typeddict-item]
    if "intentName" in data:
        out["intent_name"] = data["intentName"]
    else:
        raise DeserializationError(
            "ConversationLevelSlotResolutionResultItem.intent_name required"
        )
    if "slotName" in data:
        out["slot_name"] = data["slotName"]
    else:
        raise DeserializationError(
            "ConversationLevelSlotResolutionResultItem.slot_name required"
        )
    if "matchResult" in data:
        import capo_lex_models_v2.types.test_result_match_status

        out["match_result"] = (
            capo_lex_models_v2.types.test_result_match_status.deserialize_json(
                data["matchResult"]
            )
        )
    else:
        raise DeserializationError(
            "ConversationLevelSlotResolutionResultItem.match_result required"
        )
    return out
