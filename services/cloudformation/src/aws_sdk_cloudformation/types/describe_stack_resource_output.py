"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeStackResourceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_resource_detail


class DescribeStackResourceOutput(TypedDict):
    stack_resource_detail: NotRequired[
        "aws_sdk_cloudformation.types.stack_resource_detail.StackResourceDetail"
    ]
    """<p>A <code>StackResourceDetail</code> structure that contains the description of the specified resource in the specified stack.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeStackResourceOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_resource_detail" in value:
        import aws_sdk_cloudformation.types.stack_resource_detail

        aws_sdk_cloudformation.types.stack_resource_detail.serialize_query(
            value["stack_resource_detail"], pairs, f"{prefix}.StackResourceDetail"
        )


def deserialize_query(el: Element) -> DescribeStackResourceOutput:
    out: DescribeStackResourceOutput = {}  # type: ignore[typeddict-item]
    child_stack_resource_detail = el.find("StackResourceDetail")
    if child_stack_resource_detail is not None:
        import aws_sdk_cloudformation.types.stack_resource_detail

        out["stack_resource_detail"] = (
            aws_sdk_cloudformation.types.stack_resource_detail.deserialize_query(
                child_stack_resource_detail
            )
        )
    return out
