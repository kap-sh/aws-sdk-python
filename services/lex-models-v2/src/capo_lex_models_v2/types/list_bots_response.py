"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBotsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_summary_list
    import capo_lex_models_v2.types.next_token


class ListBotsResponse(TypedDict, closed=True):
    bot_summaries: NotRequired[
        "capo_lex_models_v2.types.bot_summary_list.BotSummaryList"
    ]
    """<p>Summary information for the bots that meet the filter criteria specified in the request. The length of the list is specified in the <code>maxResults</code> parameter of the request. If there are more bots available, the <code>nextToken</code> field contains a token to the next page of results.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>A token that indicates whether there are more results to return in a response to the <code>ListBots</code> operation. If the <code>nextToken</code> field is present, you send the contents as the <code>nextToken</code> parameter of a <code>ListBots</code> operation request to get the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotsResponse) -> dict:
    out: dict = {}
    if "bot_summaries" in value:
        import capo_lex_models_v2.types.bot_summary_list

        out["botSummaries"] = capo_lex_models_v2.types.bot_summary_list.serialize_json(
            value["bot_summaries"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBotsResponse:
    out: ListBotsResponse = {}  # type: ignore[typeddict-item]
    if "botSummaries" in data:
        import capo_lex_models_v2.types.bot_summary_list

        out["bot_summaries"] = (
            capo_lex_models_v2.types.bot_summary_list.deserialize_json(
                data["botSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
