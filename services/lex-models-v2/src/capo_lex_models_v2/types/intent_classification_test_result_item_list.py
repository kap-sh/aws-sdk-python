"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentClassificationTestResultItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.intent_classification_test_result_item

IntentClassificationTestResultItemList: TypeAlias = list[
    "capo_lex_models_v2.types.intent_classification_test_result_item.IntentClassificationTestResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntentClassificationTestResultItemList) -> list:
    import capo_lex_models_v2.types.intent_classification_test_result_item

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.intent_classification_test_result_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IntentClassificationTestResultItemList:
    import capo_lex_models_v2.types.intent_classification_test_result_item

    out: IntentClassificationTestResultItemList = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.intent_classification_test_result_item.deserialize_json(
                item
            )
        )
    return out
