"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.logical_resource_id
    import capo_cloudformation.types.stack_name


class ResourceLocation(TypedDict, closed=True):
    stack_name: NotRequired["capo_cloudformation.types.stack_name.StackName"]
    """<p>The name associated with the stack.</p>"""
    logical_resource_id: NotRequired[
        "capo_cloudformation.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>The logical name of the resource specified in the template.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceLocation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_name" in value:
        pairs.append((f"{prefix}.StackName", str(value["stack_name"])))
    if "logical_resource_id" in value:
        pairs.append((f"{prefix}.LogicalResourceId", str(value["logical_resource_id"])))


def deserialize_query(el: Element) -> ResourceLocation:
    out: ResourceLocation = {}  # type: ignore[typeddict-item]
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_logical_resource_id = el.find("LogicalResourceId")
    if child_logical_resource_id is not None:
        out["logical_resource_id"] = str(child_logical_resource_id.text or "")
    return out
