"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationLevelTestResults``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.conversation_level_test_result_item_list


class ConversationLevelTestResults(TypedDict, closed=True):
    items: "aws_sdk_lex_models_v2.types.conversation_level_test_result_item_list.ConversationLevelTestResultItemList"
    """<p>The item list in the test set results data at the conversation level.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLevelTestResults) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.conversation_level_test_result_item_list

    out["items"] = (
        aws_sdk_lex_models_v2.types.conversation_level_test_result_item_list.serialize_json(
            value["items"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConversationLevelTestResults:
    out: ConversationLevelTestResults = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_lex_models_v2.types.conversation_level_test_result_item_list

        out["items"] = (
            aws_sdk_lex_models_v2.types.conversation_level_test_result_item_list.deserialize_json(
                data["items"]
            )
        )
    else:
        raise DeserializationError("ConversationLevelTestResults.items required")
    return out
