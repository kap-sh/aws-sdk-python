"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.work_space_associated_resource_type_list
    import aws_sdk_workspaces.types.workspace_id


class DescribeWorkspaceAssociationsRequest(TypedDict):
    workspace_id: "aws_sdk_workspaces.types.workspace_id.WorkspaceId"
    """<p>The identifier of the WorkSpace.</p>"""
    associated_resource_types: "aws_sdk_workspaces.types.work_space_associated_resource_type_list.WorkSpaceAssociatedResourceTypeList"
    """<p>The resource types of the associated resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceAssociationsRequest) -> dict:
    out: dict = {}
    out["WorkspaceId"] = value["workspace_id"]
    import aws_sdk_workspaces.types.work_space_associated_resource_type_list

    out["AssociatedResourceTypes"] = (
        aws_sdk_workspaces.types.work_space_associated_resource_type_list.serialize_aws_json_1_1(
            value["associated_resource_types"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspaceAssociationsRequest:
    out: DescribeWorkspaceAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "WorkspaceId" in data:
        out["workspace_id"] = data["WorkspaceId"]
    else:
        raise DeserializationError(
            "DescribeWorkspaceAssociationsRequest.workspace_id required"
        )
    if "AssociatedResourceTypes" in data:
        import aws_sdk_workspaces.types.work_space_associated_resource_type_list

        out["associated_resource_types"] = (
            aws_sdk_workspaces.types.work_space_associated_resource_type_list.deserialize_aws_json_1_1(
                data["AssociatedResourceTypes"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeWorkspaceAssociationsRequest.associated_resource_types required"
        )
    return out
