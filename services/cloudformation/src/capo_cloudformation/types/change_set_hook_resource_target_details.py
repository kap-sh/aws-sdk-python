"""Generated from Smithy shape ``com.amazonaws.cloudformation#ChangeSetHookResourceTargetDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.change_action
    import capo_cloudformation.types.hook_target_type_name
    import capo_cloudformation.types.logical_resource_id


class ChangeSetHookResourceTargetDetails(TypedDict, closed=True):
    logical_resource_id: NotRequired[
        "capo_cloudformation.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>The resource's logical ID, which is defined in the stack's template.</p>"""
    resource_type: NotRequired[
        "capo_cloudformation.types.hook_target_type_name.HookTargetTypeName"
    ]
    """<p>The type of CloudFormation resource, such as <code>AWS::S3::Bucket</code>.</p>"""
    resource_action: NotRequired["capo_cloudformation.types.change_action.ChangeAction"]
    """<p>Specifies the action of the resource.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ChangeSetHookResourceTargetDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "logical_resource_id" in value:
        pairs.append(
            (f"{key_prefix}LogicalResourceId", str(value["logical_resource_id"]))
        )
    if "resource_type" in value:
        pairs.append((f"{key_prefix}ResourceType", str(value["resource_type"])))
    if "resource_action" in value:
        import capo_cloudformation.types.change_action

        capo_cloudformation.types.change_action.serialize_query(
            value["resource_action"], pairs, f"{key_prefix}ResourceAction"
        )


def deserialize_query(el: Element) -> ChangeSetHookResourceTargetDetails:
    out: ChangeSetHookResourceTargetDetails = {}  # type: ignore[typeddict-item]
    child_logical_resource_id = el.find("LogicalResourceId")
    if child_logical_resource_id is not None:
        out["logical_resource_id"] = str(child_logical_resource_id.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        out["resource_type"] = str(child_resource_type.text or "")
    child_resource_action = el.find("ResourceAction")
    if child_resource_action is not None:
        import capo_cloudformation.types.change_action

        out["resource_action"] = (
            capo_cloudformation.types.change_action.deserialize_query(
                child_resource_action
            )
        )
    return out
