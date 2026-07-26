"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeStackResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.stack_resource_detail


class DescribeStackResourceOutput(TypedDict, closed=True):
    stack_resource_detail: NotRequired[
        "capo_cloudformation.types.stack_resource_detail.StackResourceDetail"
    ]
    """<p>A <code>StackResourceDetail</code> structure that contains the description of the specified resource in the specified stack.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeStackResourceOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_resource_detail" in value:
        import capo_cloudformation.types.stack_resource_detail

        capo_cloudformation.types.stack_resource_detail.serialize_query(
            value["stack_resource_detail"], pairs, f"{prefix}.StackResourceDetail"
        )


def deserialize_query(el: Element) -> DescribeStackResourceOutput:
    out: DescribeStackResourceOutput = {}  # type: ignore[typeddict-item]
    child_stack_resource_detail = el.find("StackResourceDetail")
    if child_stack_resource_detail is not None:
        import capo_cloudformation.types.stack_resource_detail

        out["stack_resource_detail"] = (
            capo_cloudformation.types.stack_resource_detail.deserialize_query(
                child_stack_resource_detail
            )
        )
    return out
