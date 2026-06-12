"""Generated from Smithy shape ``com.amazonaws.cloudformation#ChangeSetHookResourceTargetDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.change_action
    import aws_sdk_cloudformation.types.hook_target_type_name
    import aws_sdk_cloudformation.types.logical_resource_id


class ChangeSetHookResourceTargetDetails(TypedDict):
    logical_resource_id: NotRequired[
        "aws_sdk_cloudformation.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>The resource's logical ID, which is defined in the stack's template.</p>"""
    resource_type: NotRequired[
        "aws_sdk_cloudformation.types.hook_target_type_name.HookTargetTypeName"
    ]
    """<p>The type of CloudFormation resource, such as <code>AWS::S3::Bucket</code>.</p>"""
    resource_action: NotRequired[
        "aws_sdk_cloudformation.types.change_action.ChangeAction"
    ]
    """<p>Specifies the action of the resource.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ChangeSetHookResourceTargetDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "logical_resource_id" in value:
        pairs.append((f"{prefix}.LogicalResourceId", str(value["logical_resource_id"])))
    if "resource_type" in value:
        pairs.append((f"{prefix}.ResourceType", str(value["resource_type"])))
    if "resource_action" in value:
        import aws_sdk_cloudformation.types.change_action

        aws_sdk_cloudformation.types.change_action.serialize_query(
            value["resource_action"], pairs, f"{prefix}.ResourceAction"
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
        import aws_sdk_cloudformation.types.change_action

        out["resource_action"] = (
            aws_sdk_cloudformation.types.change_action.deserialize_query(
                child_resource_action
            )
        )
    return out
