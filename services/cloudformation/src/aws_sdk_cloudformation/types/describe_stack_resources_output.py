"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeStackResourcesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_resources


class DescribeStackResourcesOutput(TypedDict):
    stack_resources: NotRequired[
        "aws_sdk_cloudformation.types.stack_resources.StackResources"
    ]
    """<p>A list of <code>StackResource</code> structures.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeStackResourcesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_resources" in value:
        import aws_sdk_cloudformation.types.stack_resources

        aws_sdk_cloudformation.types.stack_resources.serialize_query(
            value["stack_resources"], pairs, f"{prefix}.StackResources"
        )


def deserialize_query(el: Element) -> DescribeStackResourcesOutput:
    out: DescribeStackResourcesOutput = {}  # type: ignore[typeddict-item]
    child_stack_resources = el.find("StackResources")
    if child_stack_resources is not None:
        import aws_sdk_cloudformation.types.stack_resources

        out["stack_resources"] = (
            aws_sdk_cloudformation.types.stack_resources.deserialize_query(
                child_stack_resources
            )
        )
    return out
