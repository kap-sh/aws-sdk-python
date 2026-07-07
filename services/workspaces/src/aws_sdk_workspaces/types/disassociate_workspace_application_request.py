"""Generated from Smithy shape ``com.amazonaws.workspaces#DisassociateWorkspaceApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.work_space_application_id
    import aws_sdk_workspaces.types.workspace_id


class DisassociateWorkspaceApplicationRequest(TypedDict, closed=True):
    workspace_id: "aws_sdk_workspaces.types.workspace_id.WorkspaceId"
    """<p>The identifier of the WorkSpace.</p>"""
    application_id: (
        "aws_sdk_workspaces.types.work_space_application_id.WorkSpaceApplicationId"
    )
    """<p>The identifier of the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateWorkspaceApplicationRequest) -> dict:
    out: dict = {}
    out["WorkspaceId"] = value["workspace_id"]
    out["ApplicationId"] = value["application_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateWorkspaceApplicationRequest:
    out: DisassociateWorkspaceApplicationRequest = {}  # type: ignore[typeddict-item]
    if "WorkspaceId" in data:
        out["workspace_id"] = data["WorkspaceId"]
    else:
        raise DeserializationError(
            "DisassociateWorkspaceApplicationRequest.workspace_id required"
        )
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    else:
        raise DeserializationError(
            "DisassociateWorkspaceApplicationRequest.application_id required"
        )
    return out
