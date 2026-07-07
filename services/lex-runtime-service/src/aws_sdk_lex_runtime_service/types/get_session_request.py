"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#GetSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_service.types.bot_alias
    import aws_sdk_lex_runtime_service.types.bot_name
    import aws_sdk_lex_runtime_service.types.intent_summary_checkpoint_label
    import aws_sdk_lex_runtime_service.types.user_id


class GetSessionRequest(TypedDict, closed=True):
    bot_name: "aws_sdk_lex_runtime_service.types.bot_name.BotName"
    """<p>The name of the bot that contains the session data.</p>"""
    bot_alias: "aws_sdk_lex_runtime_service.types.bot_alias.BotAlias"
    """<p>The alias in use for the bot that contains the session data.</p>"""
    user_id: "aws_sdk_lex_runtime_service.types.user_id.UserId"
    """<p>The ID of the client application user. Amazon Lex uses this to identify a user's conversation with your bot. </p>"""
    checkpoint_label_filter: NotRequired[
        "aws_sdk_lex_runtime_service.types.intent_summary_checkpoint_label.IntentSummaryCheckpointLabel"
    ]
    """<p>A string used to filter the intents returned in the <code>recentIntentSummaryView</code> structure. </p> <p>When you specify a filter, only intents with their <code>checkpointLabel</code> field set to that string are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSessionRequest:
    out: GetSessionRequest = {}  # type: ignore[typeddict-item]
    return out
