"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBotLocalesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_locale_summary_list
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.next_token


class ListBotLocalesResponse(TypedDict, closed=True):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot to list locales for.</p>"""
    bot_version: NotRequired["aws_sdk_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The version of the bot.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>A token that indicates whether there are more results to return in a response to the <code>ListBotLocales</code> operation. If the <code>nextToken</code> field is present, you send the contents as the <code>nextToken</code> parameter of a <code>ListBotLocales</code> operation request to get the next page of results.</p>"""
    bot_locale_summaries: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_locale_summary_list.BotLocaleSummaryList"
    ]
    """<p>Summary information for the locales that meet the filter criteria specified in the request. The length of the list is specified in the <code>maxResults</code> parameter of the request. If there are more locales available, the <code>nextToken</code> field contains a token to get the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotLocalesResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "bot_locale_summaries" in value:
        import aws_sdk_lex_models_v2.types.bot_locale_summary_list

        out["botLocaleSummaries"] = (
            aws_sdk_lex_models_v2.types.bot_locale_summary_list.serialize_json(
                value["bot_locale_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListBotLocalesResponse:
    out: ListBotLocalesResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "botLocaleSummaries" in data:
        import aws_sdk_lex_models_v2.types.bot_locale_summary_list

        out["bot_locale_summaries"] = (
            aws_sdk_lex_models_v2.types.bot_locale_summary_list.deserialize_json(
                data["botLocaleSummaries"]
            )
        )
    return out
