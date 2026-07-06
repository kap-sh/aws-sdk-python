"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListTestExecutionResultItemsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.max_results
    import aws_sdk_lex_models_v2.types.next_token
    import aws_sdk_lex_models_v2.types.test_execution_result_filter_by


class ListTestExecutionResultItemsRequest(TypedDict, closed=True):
    test_execution_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the test execution to list the result items.</p>"""
    result_filter_by: "aws_sdk_lex_models_v2.types.test_execution_result_filter_by.TestExecutionResultFilterBy"
    """<p>The filter for the list of results from the test set execution.</p>"""
    max_results: NotRequired["aws_sdk_lex_models_v2.types.max_results.MaxResults"]
    """<p>The maximum number of test execution result items to return in each page. If there are fewer results than the max page size, only the actual number of results are returned.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from the <code>ListTestExecutionResultItems</code> operation contains more results than specified in the <code>maxResults</code> parameter, a token is returned in the response. Use that token in the <code>nextToken</code> parameter to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTestExecutionResultItemsRequest) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.test_execution_result_filter_by

    out["resultFilterBy"] = (
        aws_sdk_lex_models_v2.types.test_execution_result_filter_by.serialize_json(
            value["result_filter_by"]
        )
    )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTestExecutionResultItemsRequest:
    out: ListTestExecutionResultItemsRequest = {}  # type: ignore[typeddict-item]
    if "resultFilterBy" in data:
        import aws_sdk_lex_models_v2.types.test_execution_result_filter_by

        out["result_filter_by"] = (
            aws_sdk_lex_models_v2.types.test_execution_result_filter_by.deserialize_json(
                data["resultFilterBy"]
            )
        )
    else:
        raise DeserializationError(
            "ListTestExecutionResultItemsRequest.result_filter_by required"
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
