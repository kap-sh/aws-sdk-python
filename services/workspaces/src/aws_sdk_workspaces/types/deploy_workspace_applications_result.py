"""Generated from Smithy shape ``com.amazonaws.workspaces#DeployWorkspaceApplicationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.work_space_application_deployment


class DeployWorkspaceApplicationsResult(TypedDict):
    deployment: NotRequired[
        "aws_sdk_workspaces.types.work_space_application_deployment.WorkSpaceApplicationDeployment"
    ]
    """<p>The list of deployed associations and information about them.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeployWorkspaceApplicationsResult) -> dict:
    out: dict = {}
    if "deployment" in value:
        import aws_sdk_workspaces.types.work_space_application_deployment

        out["Deployment"] = (
            aws_sdk_workspaces.types.work_space_application_deployment.serialize_aws_json_1_1(
                value["deployment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeployWorkspaceApplicationsResult:
    out: DeployWorkspaceApplicationsResult = {}  # type: ignore[typeddict-item]
    if "Deployment" in data:
        import aws_sdk_workspaces.types.work_space_application_deployment

        out["deployment"] = (
            aws_sdk_workspaces.types.work_space_application_deployment.deserialize_aws_json_1_1(
                data["Deployment"]
            )
        )
    return out
