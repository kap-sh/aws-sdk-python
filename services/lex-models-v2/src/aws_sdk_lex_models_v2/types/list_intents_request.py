"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListIntentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.intent_filters
    import aws_sdk_lex_models_v2.types.intent_sort_by
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.max_results
    import aws_sdk_lex_models_v2.types.next_token


class ListIntentsRequest(TypedDict):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot that contains the intent.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.bot_version.BotVersion"
    """<p>The version of the bot that contains the intent.</p>"""
    locale_id: "aws_sdk_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the language and locale of the intents to list. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.</p>"""
    sort_by: NotRequired["aws_sdk_lex_models_v2.types.intent_sort_by.IntentSortBy"]
    """<p>Determines the sort order for the response from the <code>ListIntents</code> operation. You can choose to sort by the intent name or last updated date in either ascending or descending order.</p>"""
    filters: NotRequired["aws_sdk_lex_models_v2.types.intent_filters.IntentFilters"]
    """<p>Provides the specification of a filter used to limit the intents in the response to only those that match the filter specification. You can only specify one filter and only one string to filter on.</p>"""
    max_results: NotRequired["aws_sdk_lex_models_v2.types.max_results.MaxResults"]
    """<p>The maximum number of intents to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from the <code>ListIntents</code> operation contains more results than specified in the <code>maxResults</code> parameter, a token is returned in the response.</p> <p>Use the returned token in the <code>nextToken</code> parameter of a <code>ListIntents</code> request to return the next page of results. For a complete set of results, call the <code>ListIntents</code> operation until the <code>nextToken</code> returned in the response is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIntentsRequest) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import aws_sdk_lex_models_v2.types.intent_sort_by

        out["sortBy"] = aws_sdk_lex_models_v2.types.intent_sort_by.serialize_json(
            value["sort_by"]
        )
    if "filters" in value:
        import aws_sdk_lex_models_v2.types.intent_filters

        out["filters"] = aws_sdk_lex_models_v2.types.intent_filters.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIntentsRequest:
    out: ListIntentsRequest = {}  # type: ignore[typeddict-item]
    if "sortBy" in data:
        import aws_sdk_lex_models_v2.types.intent_sort_by

        out["sort_by"] = aws_sdk_lex_models_v2.types.intent_sort_by.deserialize_json(
            data["sortBy"]
        )
    if "filters" in data:
        import aws_sdk_lex_models_v2.types.intent_filters

        out["filters"] = aws_sdk_lex_models_v2.types.intent_filters.deserialize_json(
            data["filters"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
