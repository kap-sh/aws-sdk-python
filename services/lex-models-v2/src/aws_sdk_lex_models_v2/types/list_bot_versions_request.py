"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBotVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version_sort_by
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.max_results
    import aws_sdk_lex_models_v2.types.next_token


class ListBotVersionsRequest(TypedDict, closed=True):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot to list versions for.</p>"""
    sort_by: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_version_sort_by.BotVersionSortBy"
    ]
    """<p>Specifies sorting parameters for the list of versions. You can specify that the list be sorted by version name in either ascending or descending order.</p>"""
    max_results: NotRequired["aws_sdk_lex_models_v2.types.max_results.MaxResults"]
    """<p>The maximum number of versions to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response to the <code>ListBotVersion</code> operation contains more results than specified in the <code>maxResults</code> parameter, a token is returned in the response. Use that token in the <code>nextToken</code> parameter to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotVersionsRequest) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import aws_sdk_lex_models_v2.types.bot_version_sort_by

        out["sortBy"] = aws_sdk_lex_models_v2.types.bot_version_sort_by.serialize_json(
            value["sort_by"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBotVersionsRequest:
    out: ListBotVersionsRequest = {}  # type: ignore[typeddict-item]
    if "sortBy" in data:
        import aws_sdk_lex_models_v2.types.bot_version_sort_by

        out["sort_by"] = (
            aws_sdk_lex_models_v2.types.bot_version_sort_by.deserialize_json(
                data["sortBy"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
