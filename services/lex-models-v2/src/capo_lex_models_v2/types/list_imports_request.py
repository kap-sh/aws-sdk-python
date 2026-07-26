"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListImportsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.import_filters
    import capo_lex_models_v2.types.import_sort_by
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.max_results
    import capo_lex_models_v2.types.next_token


class ListImportsRequest(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier that Amazon Lex assigned to the bot.</p>"""
    bot_version: NotRequired[
        "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The version of the bot to list imports for.</p>"""
    sort_by: NotRequired["capo_lex_models_v2.types.import_sort_by.ImportSortBy"]
    """<p>Determines the field that the list of imports is sorted by. You can sort by the <code>LastUpdatedDateTime</code> field in ascending or descending order.</p>"""
    filters: NotRequired["capo_lex_models_v2.types.import_filters.ImportFilters"]
    """<p>Provides the specification of a filter used to limit the bots in the response to only those that match the filter specification. You can only specify one filter and one string to filter on.</p>"""
    max_results: NotRequired["capo_lex_models_v2.types.max_results.MaxResults"]
    """<p>The maximum number of imports to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from the <code>ListImports</code> operation contains more results than specified in the <code>maxResults</code> parameter, a token is returned in the response.</p> <p>Use the returned token in the <code>nextToken</code> parameter of a <code>ListImports</code> request to return the next page of results. For a complete set of results, call the <code>ListImports</code> operation until the <code>nextToken</code> returned in the response is null.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>Specifies the locale that should be present in the list. If you don't specify a resource type in the <code>filters</code> parameter, the list contains both bot locales and custom vocabularies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImportsRequest) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "sort_by" in value:
        import capo_lex_models_v2.types.import_sort_by

        out["sortBy"] = capo_lex_models_v2.types.import_sort_by.serialize_json(
            value["sort_by"]
        )
    if "filters" in value:
        import capo_lex_models_v2.types.import_filters

        out["filters"] = capo_lex_models_v2.types.import_filters.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    return out


def deserialize_json(data: dict) -> ListImportsRequest:
    out: ListImportsRequest = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "sortBy" in data:
        import capo_lex_models_v2.types.import_sort_by

        out["sort_by"] = capo_lex_models_v2.types.import_sort_by.deserialize_json(
            data["sortBy"]
        )
    if "filters" in data:
        import capo_lex_models_v2.types.import_filters

        out["filters"] = capo_lex_models_v2.types.import_filters.deserialize_json(
            data["filters"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    return out
