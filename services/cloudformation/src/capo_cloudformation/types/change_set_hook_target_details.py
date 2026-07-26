"""Generated from Smithy shape ``com.amazonaws.cloudformation#ChangeSetHookTargetDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.change_set_hook_resource_target_details
    import capo_cloudformation.types.hook_target_type


class ChangeSetHookTargetDetails(TypedDict, closed=True):
    target_type: NotRequired[
        "capo_cloudformation.types.hook_target_type.HookTargetType"
    ]
    """<p>The Hook target type.</p>"""
    resource_target_details: NotRequired[
        "capo_cloudformation.types.change_set_hook_resource_target_details.ChangeSetHookResourceTargetDetails"
    ]
    """<p>Required if <code>TargetType</code> is <code>RESOURCE</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ChangeSetHookTargetDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "target_type" in value:
        import capo_cloudformation.types.hook_target_type

        capo_cloudformation.types.hook_target_type.serialize_query(
            value["target_type"], pairs, f"{prefix}.TargetType"
        )
    if "resource_target_details" in value:
        import capo_cloudformation.types.change_set_hook_resource_target_details

        capo_cloudformation.types.change_set_hook_resource_target_details.serialize_query(
            value["resource_target_details"], pairs, f"{prefix}.ResourceTargetDetails"
        )


def deserialize_query(el: Element) -> ChangeSetHookTargetDetails:
    out: ChangeSetHookTargetDetails = {}  # type: ignore[typeddict-item]
    child_target_type = el.find("TargetType")
    if child_target_type is not None:
        import capo_cloudformation.types.hook_target_type

        out["target_type"] = (
            capo_cloudformation.types.hook_target_type.deserialize_query(
                child_target_type
            )
        )
    child_resource_target_details = el.find("ResourceTargetDetails")
    if child_resource_target_details is not None:
        import capo_cloudformation.types.change_set_hook_resource_target_details

        out["resource_target_details"] = (
            capo_cloudformation.types.change_set_hook_resource_target_details.deserialize_query(
                child_resource_target_details
            )
        )
    return out
