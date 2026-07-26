"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListTestExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.max_results
    import capo_lex_models_v2.types.next_token
    import capo_lex_models_v2.types.test_execution_sort_by


class ListTestExecutionsRequest(TypedDict, closed=True):
    sort_by: NotRequired[
        "capo_lex_models_v2.types.test_execution_sort_by.TestExecutionSortBy"
    ]
    """<p>The sort order of the test set executions.</p>"""
    max_results: NotRequired["capo_lex_models_v2.types.max_results.MaxResults"]
    """<p>The maximum number of test executions to return in each page. If there are fewer results than the max page size, only the actual number of results are returned.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from the ListTestExecutions operation contains more results than specified in the maxResults parameter, a token is returned in the response. Use that token in the nextToken parameter to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTestExecutionsRequest) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import capo_lex_models_v2.types.test_execution_sort_by

        out["sortBy"] = capo_lex_models_v2.types.test_execution_sort_by.serialize_json(
            value["sort_by"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTestExecutionsRequest:
    out: ListTestExecutionsRequest = {}  # type: ignore[typeddict-item]
    if "sortBy" in data:
        import capo_lex_models_v2.types.test_execution_sort_by

        out["sort_by"] = (
            capo_lex_models_v2.types.test_execution_sort_by.deserialize_json(
                data["sortBy"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
