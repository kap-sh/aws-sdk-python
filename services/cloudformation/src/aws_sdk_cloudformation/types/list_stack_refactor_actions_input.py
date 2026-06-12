"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListStackRefactorActionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.max_results
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.stack_refactor_id


class ListStackRefactorActionsInput(TypedDict):
    stack_refactor_id: NotRequired[
        "aws_sdk_cloudformation.types.stack_refactor_id.StackRefactorId"
    ]
    """<p>The ID associated with the stack refactor created from the <a>CreateStackRefactor</a> action.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_results: NotRequired["aws_sdk_cloudformation.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListStackRefactorActionsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_refactor_id" in value:
        pairs.append((f"{prefix}.StackRefactorId", str(value["stack_refactor_id"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))


def deserialize_query(el: Element) -> ListStackRefactorActionsInput:
    out: ListStackRefactorActionsInput = {}  # type: ignore[typeddict-item]
    child_stack_refactor_id = el.find("StackRefactorId")
    if child_stack_refactor_id is not None:
        out["stack_refactor_id"] = str(child_stack_refactor_id.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
