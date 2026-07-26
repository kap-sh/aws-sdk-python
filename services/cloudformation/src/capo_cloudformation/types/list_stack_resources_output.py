"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListStackResourcesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.next_token
    import capo_cloudformation.types.stack_resource_summaries


class ListStackResourcesOutput(TypedDict, closed=True):
    stack_resource_summaries: NotRequired[
        "capo_cloudformation.types.stack_resource_summaries.StackResourceSummaries"
    ]
    """<p>A list of <code>StackResourceSummary</code> structures.</p>"""
    next_token: NotRequired["capo_cloudformation.types.next_token.NextToken"]
    """<p>If the output exceeds 1 MB, a string that identifies the next page of stack resources. If no additional page exists, this value is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListStackResourcesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_resource_summaries" in value:
        import capo_cloudformation.types.stack_resource_summaries

        capo_cloudformation.types.stack_resource_summaries.serialize_query(
            value["stack_resource_summaries"], pairs, f"{prefix}.StackResourceSummaries"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListStackResourcesOutput:
    out: ListStackResourcesOutput = {}  # type: ignore[typeddict-item]
    child_stack_resource_summaries = el.find("StackResourceSummaries")
    if child_stack_resource_summaries is not None:
        import capo_cloudformation.types.stack_resource_summaries

        out["stack_resource_summaries"] = (
            capo_cloudformation.types.stack_resource_summaries.deserialize_query(
                child_stack_resource_summaries
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
