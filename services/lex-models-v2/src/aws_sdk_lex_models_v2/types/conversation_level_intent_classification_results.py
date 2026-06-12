"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationLevelIntentClassificationResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.conversation_level_intent_classification_result_item

ConversationLevelIntentClassificationResults: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.conversation_level_intent_classification_result_item.ConversationLevelIntentClassificationResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLevelIntentClassificationResults) -> list:
    import aws_sdk_lex_models_v2.types.conversation_level_intent_classification_result_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.conversation_level_intent_classification_result_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConversationLevelIntentClassificationResults:
    import aws_sdk_lex_models_v2.types.conversation_level_intent_classification_result_item

    out: ConversationLevelIntentClassificationResults = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.conversation_level_intent_classification_result_item.deserialize_json(
                item
            )
        )
    return out
