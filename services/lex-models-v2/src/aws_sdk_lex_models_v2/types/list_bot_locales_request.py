"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBotLocalesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_locale_filters
    import aws_sdk_lex_models_v2.types.bot_locale_sort_by
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.max_results
    import aws_sdk_lex_models_v2.types.next_token


class ListBotLocalesRequest(TypedDict, closed=True):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot to list locales for.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.bot_version.BotVersion"
    """<p>The version of the bot to list locales for.</p>"""
    sort_by: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_locale_sort_by.BotLocaleSortBy"
    ]
    """<p>Specifies sorting parameters for the list of locales. You can sort by locale name in ascending or descending order.</p>"""
    filters: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_locale_filters.BotLocaleFilters"
    ]
    """<p>Provides the specification for a filter used to limit the response to only those locales that match the filter specification. You can only specify one filter and one value to filter on.</p>"""
    max_results: NotRequired["aws_sdk_lex_models_v2.types.max_results.MaxResults"]
    """<p>The maximum number of aliases to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from the <code>ListBotLocales</code> operation contains more results than specified in the <code>maxResults</code> parameter, a token is returned in the response. Use that token as the <code>nextToken</code> parameter to return the next page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotLocalesRequest) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import aws_sdk_lex_models_v2.types.bot_locale_sort_by

        out["sortBy"] = aws_sdk_lex_models_v2.types.bot_locale_sort_by.serialize_json(
            value["sort_by"]
        )
    if "filters" in value:
        import aws_sdk_lex_models_v2.types.bot_locale_filters

        out["filters"] = aws_sdk_lex_models_v2.types.bot_locale_filters.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBotLocalesRequest:
    out: ListBotLocalesRequest = {}  # type: ignore[typeddict-item]
    if "sortBy" in data:
        import aws_sdk_lex_models_v2.types.bot_locale_sort_by

        out["sort_by"] = (
            aws_sdk_lex_models_v2.types.bot_locale_sort_by.deserialize_json(
                data["sortBy"]
            )
        )
    if "filters" in data:
        import aws_sdk_lex_models_v2.types.bot_locale_filters

        out["filters"] = (
            aws_sdk_lex_models_v2.types.bot_locale_filters.deserialize_json(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
