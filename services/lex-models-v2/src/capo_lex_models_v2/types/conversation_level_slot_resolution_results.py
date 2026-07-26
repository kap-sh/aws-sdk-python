"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationLevelSlotResolutionResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.conversation_level_slot_resolution_result_item

ConversationLevelSlotResolutionResults: TypeAlias = list[
    "capo_lex_models_v2.types.conversation_level_slot_resolution_result_item.ConversationLevelSlotResolutionResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLevelSlotResolutionResults) -> list:
    import capo_lex_models_v2.types.conversation_level_slot_resolution_result_item

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.conversation_level_slot_resolution_result_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConversationLevelSlotResolutionResults:
    import capo_lex_models_v2.types.conversation_level_slot_resolution_result_item

    out: ConversationLevelSlotResolutionResults = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.conversation_level_slot_resolution_result_item.deserialize_json(
                item
            )
        )
    return out
