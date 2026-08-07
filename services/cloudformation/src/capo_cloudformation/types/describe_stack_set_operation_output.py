"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeStackSetOperationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.stack_set_operation


class DescribeStackSetOperationOutput(TypedDict, closed=True):
    stack_set_operation: NotRequired[
        "capo_cloudformation.types.stack_set_operation.StackSetOperation"
    ]
    """<p>The specified StackSet operation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeStackSetOperationOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_set_operation" in value:
        import capo_cloudformation.types.stack_set_operation

        capo_cloudformation.types.stack_set_operation.serialize_query(
            value["stack_set_operation"], pairs, f"{key_prefix}StackSetOperation"
        )


def deserialize_query(el: Element) -> DescribeStackSetOperationOutput:
    out: DescribeStackSetOperationOutput = {}  # type: ignore[typeddict-item]
    child_stack_set_operation = el.find("StackSetOperation")
    if child_stack_set_operation is not None:
        import capo_cloudformation.types.stack_set_operation

        out["stack_set_operation"] = (
            capo_cloudformation.types.stack_set_operation.deserialize_query(
                child_stack_set_operation
            )
        )
    return out
