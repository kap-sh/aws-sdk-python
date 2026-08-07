"""Generated from Smithy shape ``com.amazonaws.cloudformation#Change``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.change_type
    import capo_cloudformation.types.hook_invocation_count
    import capo_cloudformation.types.resource_change


class Change(TypedDict, closed=True):
    type: NotRequired["capo_cloudformation.types.change_type.ChangeType"]
    """<p>The type of entity that CloudFormation changes.</p> <ul> <li> <p> <code>Resource</code> This change is for a resource.</p> </li> </ul>"""
    hook_invocation_count: NotRequired[
        "capo_cloudformation.types.hook_invocation_count.HookInvocationCount"
    ]
    """<p>Is either <code>null</code>, if no Hooks invoke for the resource, or contains the number of Hooks that will invoke for the resource.</p>"""
    resource_change: NotRequired[
        "capo_cloudformation.types.resource_change.ResourceChange"
    ]
    """<p>A <code>ResourceChange</code> structure that describes the resource and action that CloudFormation will perform.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Change, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "type" in value:
        import capo_cloudformation.types.change_type

        capo_cloudformation.types.change_type.serialize_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "hook_invocation_count" in value:
        pairs.append(
            (f"{key_prefix}HookInvocationCount", str(value["hook_invocation_count"]))
        )
    if "resource_change" in value:
        import capo_cloudformation.types.resource_change

        capo_cloudformation.types.resource_change.serialize_query(
            value["resource_change"], pairs, f"{key_prefix}ResourceChange"
        )


def deserialize_query(el: Element) -> Change:
    out: Change = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import capo_cloudformation.types.change_type

        out["type"] = capo_cloudformation.types.change_type.deserialize_query(
            child_type
        )
    child_hook_invocation_count = el.find("HookInvocationCount")
    if child_hook_invocation_count is not None:
        out["hook_invocation_count"] = int(child_hook_invocation_count.text or "")
    child_resource_change = el.find("ResourceChange")
    if child_resource_change is not None:
        import capo_cloudformation.types.resource_change

        out["resource_change"] = (
            capo_cloudformation.types.resource_change.deserialize_query(
                child_resource_change
            )
        )
    return out
