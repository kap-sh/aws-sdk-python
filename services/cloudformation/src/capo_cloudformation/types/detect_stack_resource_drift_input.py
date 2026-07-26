"""Generated from Smithy shape ``com.amazonaws.cloudformation#DetectStackResourceDriftInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.logical_resource_id
    import capo_cloudformation.types.stack_name_or_id


class DetectStackResourceDriftInput(TypedDict, closed=True):
    stack_name: NotRequired["capo_cloudformation.types.stack_name_or_id.StackNameOrId"]
    """<p>The name of the stack to which the resource belongs.</p>"""
    logical_resource_id: NotRequired[
        "capo_cloudformation.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>The logical name of the resource for which to return drift information.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DetectStackResourceDriftInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_name" in value:
        pairs.append((f"{prefix}.StackName", str(value["stack_name"])))
    if "logical_resource_id" in value:
        pairs.append((f"{prefix}.LogicalResourceId", str(value["logical_resource_id"])))


def deserialize_query(el: Element) -> DetectStackResourceDriftInput:
    out: DetectStackResourceDriftInput = {}  # type: ignore[typeddict-item]
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_logical_resource_id = el.find("LogicalResourceId")
    if child_logical_resource_id is not None:
        out["logical_resource_id"] = str(child_logical_resource_id.text or "")
    return out
