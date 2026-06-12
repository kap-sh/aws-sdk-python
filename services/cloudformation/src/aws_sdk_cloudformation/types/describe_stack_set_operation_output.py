"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeStackSetOperationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_set_operation


class DescribeStackSetOperationOutput(TypedDict):
    stack_set_operation: NotRequired[
        "aws_sdk_cloudformation.types.stack_set_operation.StackSetOperation"
    ]
    """<p>The specified StackSet operation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeStackSetOperationOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_set_operation" in value:
        import aws_sdk_cloudformation.types.stack_set_operation

        aws_sdk_cloudformation.types.stack_set_operation.serialize_query(
            value["stack_set_operation"], pairs, f"{prefix}.StackSetOperation"
        )


def deserialize_query(el: Element) -> DescribeStackSetOperationOutput:
    out: DescribeStackSetOperationOutput = {}  # type: ignore[typeddict-item]
    child_stack_set_operation = el.find("StackSetOperation")
    if child_stack_set_operation is not None:
        import aws_sdk_cloudformation.types.stack_set_operation

        out["stack_set_operation"] = (
            aws_sdk_cloudformation.types.stack_set_operation.deserialize_query(
                child_stack_set_operation
            )
        )
    return out
