"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListStackInstancesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.next_token
    import capo_cloudformation.types.stack_instance_summaries


class ListStackInstancesOutput(TypedDict, closed=True):
    summaries: NotRequired[
        "capo_cloudformation.types.stack_instance_summaries.StackInstanceSummaries"
    ]
    """<p>A list of <code>StackInstanceSummary</code> structures that contain information about the specified stack instances.</p>"""
    next_token: NotRequired["capo_cloudformation.types.next_token.NextToken"]
    """<p>If the request doesn't return all the remaining results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call <code>ListStackInstances</code> again and assign that token to the request object's <code>NextToken</code> parameter. If the request returns all results, <code>NextToken</code> is set to <code>null</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListStackInstancesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "summaries" in value:
        import capo_cloudformation.types.stack_instance_summaries

        capo_cloudformation.types.stack_instance_summaries.serialize_query(
            value["summaries"], pairs, f"{prefix}.Summaries"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListStackInstancesOutput:
    out: ListStackInstancesOutput = {}  # type: ignore[typeddict-item]
    child_summaries = el.find("Summaries")
    if child_summaries is not None:
        import capo_cloudformation.types.stack_instance_summaries

        out["summaries"] = (
            capo_cloudformation.types.stack_instance_summaries.deserialize_query(
                child_summaries
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
