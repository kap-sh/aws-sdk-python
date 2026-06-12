"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListStackRefactorsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.max_results
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.stack_refactor_execution_status_filter


class ListStackRefactorsInput(TypedDict):
    execution_status_filter: NotRequired[
        "aws_sdk_cloudformation.types.stack_refactor_execution_status_filter.StackRefactorExecutionStatusFilter"
    ]
    """<p>Execution status to use as a filter. Specify one or more execution status codes to list only stack refactors with the specified execution status codes.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_results: NotRequired["aws_sdk_cloudformation.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListStackRefactorsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "execution_status_filter" in value:
        import aws_sdk_cloudformation.types.stack_refactor_execution_status_filter

        aws_sdk_cloudformation.types.stack_refactor_execution_status_filter.serialize_query(
            value["execution_status_filter"], pairs, f"{prefix}.ExecutionStatusFilter"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))


def deserialize_query(el: Element) -> ListStackRefactorsInput:
    out: ListStackRefactorsInput = {}  # type: ignore[typeddict-item]
    child_execution_status_filter = el.find("ExecutionStatusFilter")
    if child_execution_status_filter is not None:
        import aws_sdk_cloudformation.types.stack_refactor_execution_status_filter

        out["execution_status_filter"] = (
            aws_sdk_cloudformation.types.stack_refactor_execution_status_filter.deserialize_query(
                child_execution_status_filter
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
