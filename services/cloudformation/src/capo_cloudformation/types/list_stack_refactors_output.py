"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListStackRefactorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.next_token
    import capo_cloudformation.types.stack_refactor_summaries


class ListStackRefactorsOutput(TypedDict, closed=True):
    stack_refactor_summaries: NotRequired[
        "capo_cloudformation.types.stack_refactor_summaries.StackRefactorSummaries"
    ]
    """<p>Provides a summary of a stack refactor, including the following:</p> <ul> <li> <p> <code>StackRefactorId</code> </p> </li> <li> <p> <code>Status</code> </p> </li> <li> <p> <code>StatusReason</code> </p> </li> <li> <p> <code>ExecutionStatus</code> </p> </li> <li> <p> <code>ExecutionStatusReason</code> </p> </li> <li> <p> <code>Description</code> </p> </li> </ul>"""
    next_token: NotRequired["capo_cloudformation.types.next_token.NextToken"]
    """<p>If the request doesn't return all the remaining results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If the request returns all results, <code>NextToken</code> is set to <code>null</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListStackRefactorsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_refactor_summaries" in value:
        import capo_cloudformation.types.stack_refactor_summaries

        capo_cloudformation.types.stack_refactor_summaries.serialize_query(
            value["stack_refactor_summaries"], pairs, f"{prefix}.StackRefactorSummaries"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListStackRefactorsOutput:
    out: ListStackRefactorsOutput = {}  # type: ignore[typeddict-item]
    child_stack_refactor_summaries = el.find("StackRefactorSummaries")
    if child_stack_refactor_summaries is not None:
        import capo_cloudformation.types.stack_refactor_summaries

        out["stack_refactor_summaries"] = (
            capo_cloudformation.types.stack_refactor_summaries.deserialize_query(
                child_stack_refactor_summaries
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
