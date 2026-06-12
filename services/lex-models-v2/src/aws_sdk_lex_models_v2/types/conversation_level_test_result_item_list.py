"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationLevelTestResultItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.conversation_level_test_result_item

ConversationLevelTestResultItemList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.conversation_level_test_result_item.ConversationLevelTestResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLevelTestResultItemList) -> list:
    import aws_sdk_lex_models_v2.types.conversation_level_test_result_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.conversation_level_test_result_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConversationLevelTestResultItemList:
    import aws_sdk_lex_models_v2.types.conversation_level_test_result_item

    out: ConversationLevelTestResultItemList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.conversation_level_test_result_item.deserialize_json(
                item
            )
        )
    return out
