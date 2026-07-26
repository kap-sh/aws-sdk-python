"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBotAliasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_alias_summary_list
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.next_token


class ListBotAliasesResponse(TypedDict, closed=True):
    bot_alias_summaries: NotRequired[
        "capo_lex_models_v2.types.bot_alias_summary_list.BotAliasSummaryList"
    ]
    """<p>Summary information for the bot aliases that meet the filter criteria specified in the request. The length of the list is specified in the <code>maxResults</code> parameter of the request. If there are more aliases available, the <code>nextToken</code> field contains a token to get the next page of results.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>A token that indicates whether there are more results to return in a response to the <code>ListBotAliases</code> operation. If the <code>nextToken</code> field is present, you send the contents as the <code>nextToken</code> parameter of a <code>ListBotAliases</code> operation request to get the next page of results.</p>"""
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot associated with the aliases.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotAliasesResponse) -> dict:
    out: dict = {}
    if "bot_alias_summaries" in value:
        import capo_lex_models_v2.types.bot_alias_summary_list

        out["botAliasSummaries"] = (
            capo_lex_models_v2.types.bot_alias_summary_list.serialize_json(
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
        import capo_lex_models_v2.types.bot_alias_summary_list

        out["bot_alias_summaries"] = (
            capo_lex_models_v2.types.bot_alias_summary_list.deserialize_json(
                data["botAliasSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    return out
