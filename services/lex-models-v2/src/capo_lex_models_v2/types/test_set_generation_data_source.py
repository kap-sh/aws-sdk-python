"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetGenerationDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.conversation_logs_data_source


class TestSetGenerationDataSource(TypedDict, closed=True):
    conversation_logs_data_source: NotRequired[
        "capo_lex_models_v2.types.conversation_logs_data_source.ConversationLogsDataSource"
    ]
    """<p>Contains information about the bot from which the conversation logs are sourced.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSetGenerationDataSource) -> dict:
    out: dict = {}
    if "conversation_logs_data_source" in value:
        import capo_lex_models_v2.types.conversation_logs_data_source

        out["conversationLogsDataSource"] = (
            capo_lex_models_v2.types.conversation_logs_data_source.serialize_json(
                value["conversation_logs_data_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestSetGenerationDataSource:
    out: TestSetGenerationDataSource = {}  # type: ignore[typeddict-item]
    if "conversationLogsDataSource" in data:
        import capo_lex_models_v2.types.conversation_logs_data_source

        out["conversation_logs_data_source"] = (
            capo_lex_models_v2.types.conversation_logs_data_source.deserialize_json(
                data["conversationLogsDataSource"]
            )
        )
    return out
