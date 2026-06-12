"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBotAliasesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_alias_summary_list
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.next_token


class ListBotAliasesResponse(TypedDict):
    bot_alias_summaries: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_alias_summary_list.BotAliasSummaryList"
    ]
    """<p>Summary information for the bot aliases that meet the filter criteria specified in the request. The length of the list is specified in the <code>maxResults</code> parameter of the request. If there are more aliases available, the <code>nextToken</code> field contains a token to get the next page of results.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>A token that indicates whether there are more results to return in a response to the <code>ListBotAliases</code> operation. If the <code>nextToken</code> field is present, you send the contents as the <code>nextToken</code> parameter of a <code>ListBotAliases</code> operation request to get the next page of results.</p>"""
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot associated with the aliases.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotAliasesResponse) -> dict:
    out: dict = {}
    if "bot_alias_summaries" in value:
        import aws_sdk_lex_models_v2.types.bot_alias_summary_list

        out["botAliasSummaries"] = (
            aws_sdk_lex_models_v2.types.bot_alias_summary_list.serialize_json(
                value["bot_alias_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    return out


def deserialize_json(data: dict) -> ListBotAliasesResponse:
    out: ListBotAliasesResponse = {}  # type: ignore[typeddict-item]
    if "botAliasSummaries" in data:
        import aws_sdk_lex_models_v2.types.bot_alias_summary_list

        out["bot_alias_summaries"] = (
            aws_sdk_lex_models_v2.types.bot_alias_summary_list.deserialize_json(
                data["botAliasSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    return out
