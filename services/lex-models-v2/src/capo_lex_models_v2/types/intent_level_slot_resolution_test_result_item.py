"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentLevelSlotResolutionTestResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boolean
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.slot_resolution_test_result_items


class IntentLevelSlotResolutionTestResultItem(TypedDict, closed=True):
    intent_name: "capo_lex_models_v2.types.name.Name"
    """<p>The name of the intent that was recognized.</p>"""
    multi_turn_conversation: "capo_lex_models_v2.types.boolean.Boolean"
    """<p>Indicates whether the conversation involves multiple turns or not.</p>"""
    slot_resolution_results: "capo_lex_models_v2.types.slot_resolution_test_result_items.SlotResolutionTestResultItems"
    """<p>The results for the slot resolution in the test execution result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentLevelSlotResolutionTestResultItem) -> dict:
    out: dict = {}
    out["intentName"] = value["intent_name"]
    out["multiTurnConversation"] = value.get("multi_turn_conversation", False)
    import capo_lex_models_v2.types.slot_resolution_test_result_items

    out["slotResolutionResults"] = (
        capo_lex_models_v2.types.slot_resolution_test_result_items.serialize_json(
            value["slot_resolution_results"]
        )
    )
    return out


def deserialize_json(data: dict) -> IntentLevelSlotResolutionTestResultItem:
    out: IntentLevelSlotResolutionTestResultItem = {}  # type: ignore[typeddict-item]
    if "intentName" in data:
        out["intent_name"] = data["intentName"]
    else:
        raise DeserializationError(
            "IntentLevelSlotResolutionTestResultItem.intent_name required"
        )
    if "multiTurnConversation" in data:
        out["multi_turn_conversation"] = data["multiTurnConversation"]
    else:
        out["multi_turn_conversation"] = False
    if "slotResolutionResults" in data:
        import capo_lex_models_v2.types.slot_resolution_test_result_items

        out["slot_resolution_results"] = (
            capo_lex_models_v2.types.slot_resolution_test_result_items.deserialize_json(
                data["slotResolutionResults"]
            )
        )
    else:
        raise DeserializationError(
            "IntentLevelSlotResolutionTestResultItem.slot_resolution_results required"
        )
    return out
