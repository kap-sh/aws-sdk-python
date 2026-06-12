"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListStackSetOperationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.stack_set_operation_summaries


class ListStackSetOperationsOutput(TypedDict):
    summaries: NotRequired[
        "aws_sdk_cloudformation.types.stack_set_operation_summaries.StackSetOperationSummaries"
    ]
    """<p>A list of <code>StackSetOperationSummary</code> structures that contain summary information about operations for the specified StackSet.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>If the request doesn't return all results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call <code>ListOperationResults</code> again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, <code>NextToken</code> is set to <code>null</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListStackSetOperationsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "summaries" in value:
        import aws_sdk_cloudformation.types.stack_set_operation_summaries

        aws_sdk_cloudformation.types.stack_set_operation_summaries.serialize_query(
            value["summaries"], pairs, f"{prefix}.Summaries"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListStackSetOperationsOutput:
    out: ListStackSetOperationsOutput = {}  # type: ignore[typeddict-item]
    child_summaries = el.find("Summaries")
    if child_summaries is not None:
        import aws_sdk_cloudformation.types.stack_set_operation_summaries

        out["summaries"] = (
            aws_sdk_cloudformation.types.stack_set_operation_summaries.deserialize_query(
                child_summaries
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
