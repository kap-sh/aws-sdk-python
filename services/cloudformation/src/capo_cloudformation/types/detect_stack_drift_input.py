"""Generated from Smithy shape ``com.amazonaws.cloudformation#DetectStackDriftInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.logical_resource_ids
    import capo_cloudformation.types.stack_name_or_id


class DetectStackDriftInput(TypedDict, closed=True):
    stack_name: NotRequired["capo_cloudformation.types.stack_name_or_id.StackNameOrId"]
    """<p>The name of the stack for which you want to detect drift.</p>"""
    logical_resource_ids: NotRequired[
        "capo_cloudformation.types.logical_resource_ids.LogicalResourceIds"
    ]
    """<p>The logical names of any resources you want to use as filters.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DetectStackDriftInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_name" in value:
        pairs.append((f"{prefix}.StackName", str(value["stack_name"])))
    if "logical_resource_ids" in value:
        import capo_cloudformation.types.logical_resource_ids

        capo_cloudformation.types.logical_resource_ids.serialize_query(
            value["logical_resource_ids"], pairs, f"{prefix}.LogicalResourceIds"
        )


def deserialize_query(el: Element) -> DetectStackDriftInput:
    out: DetectStackDriftInput = {}  # type: ignore[typeddict-item]
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_logical_resource_ids = el.find("LogicalResourceIds")
    if child_logical_resource_ids is not None:
        import capo_cloudformation.types.logical_resource_ids

        out["logical_resource_ids"] = (
            capo_cloudformation.types.logical_resource_ids.deserialize_query(
                child_logical_resource_ids
            )
        )
    return out
