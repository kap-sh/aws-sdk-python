"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListStacksOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.stack_summaries


class ListStacksOutput(TypedDict):
    stack_summaries: NotRequired[
        "aws_sdk_cloudformation.types.stack_summaries.StackSummaries"
    ]
    """<p>A list of <code>StackSummary</code> structures that contains information about the specified stacks.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>If the output exceeds 1 MB in size, a string that identifies the next page of stacks. If no additional page exists, this value is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListStacksOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_summaries" in value:
        import aws_sdk_cloudformation.types.stack_summaries

        aws_sdk_cloudformation.types.stack_summaries.serialize_query(
            value["stack_summaries"], pairs, f"{prefix}.StackSummaries"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListStacksOutput:
    out: ListStacksOutput = {}  # type: ignore[typeddict-item]
    child_stack_summaries = el.find("StackSummaries")
    if child_stack_summaries is not None:
        import aws_sdk_cloudformation.types.stack_summaries

        out["stack_summaries"] = (
            aws_sdk_cloudformation.types.stack_summaries.deserialize_query(
                child_stack_summaries
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
