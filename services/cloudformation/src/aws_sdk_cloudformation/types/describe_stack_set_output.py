"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeStackSetOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_set


class DescribeStackSetOutput(TypedDict):
    stack_set: NotRequired["aws_sdk_cloudformation.types.stack_set.StackSet"]
    """<p>The specified StackSet.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeStackSetOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_set" in value:
        import aws_sdk_cloudformation.types.stack_set

        aws_sdk_cloudformation.types.stack_set.serialize_query(
            value["stack_set"], pairs, f"{prefix}.StackSet"
        )


def deserialize_query(el: Element) -> DescribeStackSetOutput:
    out: DescribeStackSetOutput = {}  # type: ignore[typeddict-item]
    child_stack_set = el.find("StackSet")
    if child_stack_set is not None:
        import aws_sdk_cloudformation.types.stack_set

        out["stack_set"] = aws_sdk_cloudformation.types.stack_set.deserialize_query(
            child_stack_set
        )
    return out
