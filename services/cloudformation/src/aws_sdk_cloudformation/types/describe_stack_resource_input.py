"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeStackResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.logical_resource_id
    import aws_sdk_cloudformation.types.stack_name


class DescribeStackResourceInput(TypedDict):
    stack_name: NotRequired["aws_sdk_cloudformation.types.stack_name.StackName"]
    """<p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul>"""
    logical_resource_id: NotRequired[
        "aws_sdk_cloudformation.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>The logical name of the resource as specified in the template.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeStackResourceInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_name" in value:
        pairs.append((f"{prefix}.StackName", str(value["stack_name"])))
    if "logical_resource_id" in value:
        pairs.append((f"{prefix}.LogicalResourceId", str(value["logical_resource_id"])))


def deserialize_query(el: Element) -> DescribeStackResourceInput:
    out: DescribeStackResourceInput = {}  # type: ignore[typeddict-item]
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_logical_resource_id = el.find("LogicalResourceId")
    if child_logical_resource_id is not None:
        out["logical_resource_id"] = str(child_logical_resource_id.text or "")
    return out
