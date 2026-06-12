"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBotsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_filters
    import aws_sdk_lex_models_v2.types.bot_sort_by
    import aws_sdk_lex_models_v2.types.max_results
    import aws_sdk_lex_models_v2.types.next_token


class ListBotsRequest(TypedDict):
    sort_by: NotRequired["aws_sdk_lex_models_v2.types.bot_sort_by.BotSortBy"]
    """<p>Specifies sorting parameters for the list of bots. You can specify that the list be sorted by bot name in ascending or descending order.</p>"""
    filters: NotRequired["aws_sdk_lex_models_v2.types.bot_filters.BotFilters"]
    """<p>Provides the specification of a filter used to limit the bots in the response to only those that match the filter specification. You can only specify one filter and one string to filter on.</p>"""
    max_results: NotRequired["aws_sdk_lex_models_v2.types.max_results.MaxResults"]
    """<p>The maximum number of bots to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from the <code>ListBots</code> operation contains more results than specified in the <code>maxResults</code> parameter, a token is returned in the response. </p> <p>Use the returned token in the <code>nextToken</code> parameter of a <code>ListBots</code> request to return the next page of results. For a complete set of results, call the <code>ListBots</code> operation until the <code>nextToken</code> returned in the response is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotsRequest) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import aws_sdk_lex_models_v2.types.bot_sort_by

        out["sortBy"] = aws_sdk_lex_models_v2.types.bot_sort_by.serialize_json(
            value["sort_by"]
        )
    if "filters" in value:
        import aws_sdk_lex_models_v2.types.bot_filters

        out["filters"] = aws_sdk_lex_models_v2.types.bot_filters.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBotsRequest:
    out: ListBotsRequest = {}  # type: ignore[typeddict-item]
    if "sortBy" in data:
        import aws_sdk_lex_models_v2.types.bot_sort_by

        out["sort_by"] = aws_sdk_lex_models_v2.types.bot_sort_by.deserialize_json(
            data["sortBy"]
        )
    if "filters" in data:
        import aws_sdk_lex_models_v2.types.bot_filters

        out["filters"] = aws_sdk_lex_models_v2.types.bot_filters.deserialize_json(
            data["filters"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
