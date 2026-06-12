"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListTestSetsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.max_results
    import aws_sdk_lex_models_v2.types.next_token
    import aws_sdk_lex_models_v2.types.test_set_sort_by


class ListTestSetsRequest(TypedDict):
    sort_by: NotRequired["aws_sdk_lex_models_v2.types.test_set_sort_by.TestSetSortBy"]
    """<p>The sort order for the list of test sets.</p>"""
    max_results: NotRequired["aws_sdk_lex_models_v2.types.max_results.MaxResults"]
    """<p>The maximum number of test sets to return in each page. If there are fewer results than the max page size, only the actual number of results are returned.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from the ListTestSets operation contains more results than specified in the maxResults parameter, a token is returned in the response. Use that token in the nextToken parameter to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTestSetsRequest) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import aws_sdk_lex_models_v2.types.test_set_sort_by

        out["sortBy"] = aws_sdk_lex_models_v2.types.test_set_sort_by.serialize_json(
            value["sort_by"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTestSetsRequest:
    out: ListTestSetsRequest = {}  # type: ignore[typeddict-item]
    if "sortBy" in data:
        import aws_sdk_lex_models_v2.types.test_set_sort_by

        out["sort_by"] = aws_sdk_lex_models_v2.types.test_set_sort_by.deserialize_json(
            data["sortBy"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
