"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListStacksInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.stack_status_filter


class ListStacksInput(TypedDict):
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    stack_status_filter: NotRequired[
        "aws_sdk_cloudformation.types.stack_status_filter.StackStatusFilter"
    ]
    """<p>Stack status to use as a filter. Specify one or more stack status codes to list only stacks with the specified status codes. For a complete list of stack status codes, see the <code>StackStatus</code> parameter of the <a>Stack</a> data type.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListStacksInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "stack_status_filter" in value:
        import aws_sdk_cloudformation.types.stack_status_filter

        aws_sdk_cloudformation.types.stack_status_filter.serialize_query(
            value["stack_status_filter"], pairs, f"{prefix}.StackStatusFilter"
        )


def deserialize_query(el: Element) -> ListStacksInput:
    out: ListStacksInput = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_stack_status_filter = el.find("StackStatusFilter")
    if child_stack_status_filter is not None:
        import aws_sdk_cloudformation.types.stack_status_filter

        out["stack_status_filter"] = (
            aws_sdk_cloudformation.types.stack_status_filter.deserialize_query(
                child_stack_status_filter
            )
        )
    return out
