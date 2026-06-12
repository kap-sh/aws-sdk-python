"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBotVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version_summary_list
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.next_token


class ListBotVersionsResponse(TypedDict):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot to list versions for.</p>"""
    bot_version_summaries: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_version_summary_list.BotVersionSummaryList"
    ]
    """<p>Summary information for the bot versions that meet the filter criteria specified in the request. The length of the list is specified in the <code>maxResults</code> parameter of the request. If there are more versions available, the <code>nextToken</code> field contains a token to get the next page of results.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>A token that indicates whether there are more results to return in a response to the <code>ListBotVersions</code> operation. If the <code>nextToken</code> field is present, you send the contents as the <code>nextToken</code> parameter of a <code>ListBotAliases</code> operation request to get the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotVersionsResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version_summaries" in value:
        import aws_sdk_lex_models_v2.types.bot_version_summary_list

        out["botVersionSummaries"] = (
            aws_sdk_lex_models_v2.types.bot_version_summary_list.serialize_json(
                value["bot_version_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBotVersionsResponse:
    out: ListBotVersionsResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersionSummaries" in data:
        import aws_sdk_lex_models_v2.types.bot_version_summary_list

        out["bot_version_summaries"] = (
            aws_sdk_lex_models_v2.types.bot_version_summary_list.deserialize_json(
                data["botVersionSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
