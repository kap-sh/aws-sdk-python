"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentLevelSlotResolutionTestResultItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.intent_level_slot_resolution_test_result_item

IntentLevelSlotResolutionTestResultItemList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.intent_level_slot_resolution_test_result_item.IntentLevelSlotResolutionTestResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntentLevelSlotResolutionTestResultItemList) -> list:
    import aws_sdk_lex_models_v2.types.intent_level_slot_resolution_test_result_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.intent_level_slot_resolution_test_result_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IntentLevelSlotResolutionTestResultItemList:
    import aws_sdk_lex_models_v2.types.intent_level_slot_resolution_test_result_item

    out: IntentLevelSlotResolutionTestResultItemList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.intent_level_slot_resolution_test_result_item.deserialize_json(
                item
            )
        )
    return out
