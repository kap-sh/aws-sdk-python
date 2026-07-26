"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBotResourceGenerationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.generation_sort_by
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.max_results
    import capo_lex_models_v2.types.next_token


class ListBotResourceGenerationsRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot whose generation requests you want to view.</p>"""
    bot_version: "capo_lex_models_v2.types.bot_version.BotVersion"
    """<p>The version of the bot whose generation requests you want to view.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The locale of the bot whose generation requests you want to view.</p>"""
    sort_by: NotRequired["capo_lex_models_v2.types.generation_sort_by.GenerationSortBy"]
    """<p>An object containing information about the attribute and the method by which to sort the results</p>"""
    max_results: NotRequired["capo_lex_models_v2.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the number specified in the <code>maxResults</code>, the response returns a token in the <code>nextToken</code> field. Use this token when making a request to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotResourceGenerationsRequest) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import capo_lex_models_v2.types.generation_sort_by

        out["sortBy"] = capo_lex_models_v2.types.generation_sort_by.serialize_json(
            value["sort_by"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBotResourceGenerationsRequest:
    out: ListBotResourceGenerationsRequest = {}  # type: ignore[typeddict-item]
    if "sortBy" in data:
        import capo_lex_models_v2.types.generation_sort_by

        out["sort_by"] = capo_lex_models_v2.types.generation_sort_by.deserialize_json(
            data["sortBy"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
