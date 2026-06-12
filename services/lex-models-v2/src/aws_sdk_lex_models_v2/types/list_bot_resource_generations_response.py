"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBotResourceGenerationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.generation_summary_list
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.next_token


class ListBotResourceGenerationsResponse(TypedDict):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot for which the generation requests were made.</p>"""
    bot_version: NotRequired["aws_sdk_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The version of the bot for which the generation requests were made.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The locale of the bot for which the generation requests were made.</p>"""
    generation_summaries: NotRequired[
        "aws_sdk_lex_models_v2.types.generation_summary_list.GenerationSummaryList"
    ]
    """<p>A list of objects, each containing information about a generation request for the bot locale.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the number specified in the <code>maxResults</code>, the response returns a token in the <code>nextToken</code> field. Use this token when making a request to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotResourceGenerationsResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "generation_summaries" in value:
        import aws_sdk_lex_models_v2.types.generation_summary_list

        out["generationSummaries"] = (
            aws_sdk_lex_models_v2.types.generation_summary_list.serialize_json(
                value["generation_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBotResourceGenerationsResponse:
    out: ListBotResourceGenerationsResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "generationSummaries" in data:
        import aws_sdk_lex_models_v2.types.generation_summary_list

        out["generation_summaries"] = (
            aws_sdk_lex_models_v2.types.generation_summary_list.deserialize_json(
                data["generationSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
