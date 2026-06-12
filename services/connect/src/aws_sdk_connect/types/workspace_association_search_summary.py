"""Generated from Smithy shape ``com.amazonaws.connect#WorkspaceAssociationSearchSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.workspace_associated_resource_id
    import aws_sdk_connect.types.workspace_associated_resource_name
    import aws_sdk_connect.types.workspace_associated_resource_type
    import aws_sdk_connect.types.workspace_id


class WorkspaceAssociationSearchSummary(TypedDict):
    workspace_id: NotRequired["aws_sdk_connect.types.workspace_id.WorkspaceId"]
    """<p>The identifier of the workspace.</p>"""
    workspace_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the workspace.</p>"""
    resource_id: NotRequired[
        "aws_sdk_connect.types.workspace_associated_resource_id.WorkspaceAssociatedResourceId"
    ]
    """<p>The identifier of the associated resource (user or routing profile).</p>"""
    resource_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the associated resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_connect.types.workspace_associated_resource_type.WorkspaceAssociatedResourceType"
    ]
    """<p>The type of resource associated with the workspace. Valid values are: <code>USER</code> and <code>ROUTING_PROFILE</code>.</p>"""
    resource_name: NotRequired[
        "aws_sdk_connect.types.workspace_associated_resource_name.WorkspaceAssociatedResourceName"
    ]
    """<p>The name of the associated resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceAssociationSearchSummary) -> dict:
    out: dict = {}
    if "workspace_id" in value:
        out["WorkspaceId"] = value["workspace_id"]
    if "workspace_arn" in value:
        out["WorkspaceArn"] = value["workspace_arn"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> WorkspaceAssociationSearchSummary:
    out: WorkspaceAssociationSearchSummary = {}  # type: ignore[typeddict-item]
    if "WorkspaceId" in data:
        out["workspace_id"] = data["WorkspaceId"]
    if "WorkspaceArn" in data:
        out["workspace_arn"] = data["WorkspaceArn"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    return out
