"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListStackSetsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.stack_set_summaries


class ListStackSetsOutput(TypedDict):
    summaries: NotRequired[
        "aws_sdk_cloudformation.types.stack_set_summaries.StackSetSummaries"
    ]
    """<p>A list of <code>StackSetSummary</code> structures that contain information about the user's StackSets.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>If the request doesn't return all of the remaining results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call <code>ListStackInstances</code> again and assign that token to the request object's <code>NextToken</code> parameter. If the request returns all results, <code>NextToken</code> is set to <code>null</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListStackSetsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "summaries" in value:
        import aws_sdk_cloudformation.types.stack_set_summaries

        aws_sdk_cloudformation.types.stack_set_summaries.serialize_query(
            value["summaries"], pairs, f"{prefix}.Summaries"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListStackSetsOutput:
    out: ListStackSetsOutput = {}  # type: ignore[typeddict-item]
    child_summaries = el.find("Summaries")
    if child_summaries is not None:
        import aws_sdk_cloudformation.types.stack_set_summaries

        out["summaries"] = (
            aws_sdk_cloudformation.types.stack_set_summaries.deserialize_query(
                child_summaries
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
