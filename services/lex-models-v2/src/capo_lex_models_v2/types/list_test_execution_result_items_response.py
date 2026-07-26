"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListTestExecutionResultItemsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.next_token
    import capo_lex_models_v2.types.test_execution_result_items


class ListTestExecutionResultItemsResponse(TypedDict, closed=True):
    test_execution_results: NotRequired[
        "capo_lex_models_v2.types.test_execution_result_items.TestExecutionResultItems"
    ]
    """<p>The list of results from the test execution.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>A token that indicates whether there are more results to return in a response to the <code>ListTestExecutionResultItems</code> operation. If the <code>nextToken</code> field is present, you send the contents as the <code>nextToken</code> parameter of a <code>ListTestExecutionResultItems</code> operation request to get the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTestExecutionResultItemsResponse) -> dict:
    out: dict = {}
    if "test_execution_results" in value:
        import capo_lex_models_v2.types.test_execution_result_items

        out["testExecutionResults"] = (
            capo_lex_models_v2.types.test_execution_result_items.serialize_json(
                value["test_execution_results"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTestExecutionResultItemsResponse:
    out: ListTestExecutionResultItemsResponse = {}  # type: ignore[typeddict-item]
    if "testExecutionResults" in data:
        import capo_lex_models_v2.types.test_execution_result_items

        out["test_execution_results"] = (
            capo_lex_models_v2.types.test_execution_result_items.deserialize_json(
                data["testExecutionResults"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
