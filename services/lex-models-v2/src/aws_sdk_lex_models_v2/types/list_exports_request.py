"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListExportsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.export_filters
    import aws_sdk_lex_models_v2.types.export_sort_by
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.max_results
    import aws_sdk_lex_models_v2.types.next_token


class ListExportsRequest(TypedDict, closed=True):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier that Amazon Lex assigned to the bot.</p>"""
    bot_version: NotRequired["aws_sdk_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The version of the bot to list exports for. </p>"""
    sort_by: NotRequired["aws_sdk_lex_models_v2.types.export_sort_by.ExportSortBy"]
    """<p>Determines the field that the list of exports is sorted by. You can sort by the <code>LastUpdatedDateTime</code> field in ascending or descending order.</p>"""
    filters: NotRequired["aws_sdk_lex_models_v2.types.export_filters.ExportFilters"]
    """<p>Provides the specification of a filter used to limit the exports in the response to only those that match the filter specification. You can only specify one filter and one string to filter on.</p>"""
    max_results: NotRequired["aws_sdk_lex_models_v2.types.max_results.MaxResults"]
    """<p>The maximum number of exports to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from the <code>ListExports</code> operation contains more results that specified in the <code>maxResults</code> parameter, a token is returned in the response. </p> <p>Use the returned token in the <code>nextToken</code> parameter of a <code>ListExports</code> request to return the next page of results. For a complete set of results, call the <code>ListExports</code> operation until the <code>nextToken</code> returned in the response is null.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>Specifies the resources that should be exported. If you don't specify a resource type in the <code>filters</code> parameter, both bot locales and custom vocabularies are exported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExportsRequest) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "sort_by" in value:
        import aws_sdk_lex_models_v2.types.export_sort_by

        out["sortBy"] = aws_sdk_lex_models_v2.types.export_sort_by.serialize_json(
            value["sort_by"]
        )
    if "filters" in value:
        import aws_sdk_lex_models_v2.types.export_filters

        out["filters"] = aws_sdk_lex_models_v2.types.export_filters.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    return out


def deserialize_json(data: dict) -> ListExportsRequest:
    out: ListExportsRequest = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "sortBy" in data:
        import aws_sdk_lex_models_v2.types.export_sort_by

        out["sort_by"] = aws_sdk_lex_models_v2.types.export_sort_by.deserialize_json(
            data["sortBy"]
        )
    if "filters" in data:
        import aws_sdk_lex_models_v2.types.export_filters

        out["filters"] = aws_sdk_lex_models_v2.types.export_filters.deserialize_json(
            data["filters"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    return out
