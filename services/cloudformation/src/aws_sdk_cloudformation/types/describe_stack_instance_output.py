"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeStackInstanceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_instance


class DescribeStackInstanceOutput(TypedDict, closed=True):
    stack_instance: NotRequired[
        "aws_sdk_cloudformation.types.stack_instance.StackInstance"
    ]
    """<p>The stack instance that matches the specified request parameters.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeStackInstanceOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_instance" in value:
        import aws_sdk_cloudformation.types.stack_instance

        aws_sdk_cloudformation.types.stack_instance.serialize_query(
            value["stack_instance"], pairs, f"{prefix}.StackInstance"
        )


def deserialize_query(el: Element) -> DescribeStackInstanceOutput:
    out: DescribeStackInstanceOutput = {}  # type: ignore[typeddict-item]
    child_stack_instance = el.find("StackInstance")
    if child_stack_instance is not None:
        import aws_sdk_cloudformation.types.stack_instance

        out["stack_instance"] = (
            aws_sdk_cloudformation.types.stack_instance.deserialize_query(
                child_stack_instance
            )
        )
    return out
