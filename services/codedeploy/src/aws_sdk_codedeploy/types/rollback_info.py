"""Generated from Smithy shape ``com.amazonaws.codedeploy#RollbackInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_id
    import aws_sdk_codedeploy.types.description


class RollbackInfo(TypedDict):
    rollback_deployment_id: NotRequired[
        "aws_sdk_codedeploy.types.deployment_id.DeploymentId"
    ]
    """<p>The ID of the deployment rollback.</p>"""
    rollback_triggering_deployment_id: NotRequired[
        "aws_sdk_codedeploy.types.deployment_id.DeploymentId"
    ]
    """<p>The deployment ID of the deployment that was underway and triggered a rollback deployment because it failed or was stopped.</p>"""
    rollback_message: NotRequired["aws_sdk_codedeploy.types.description.Description"]
    """<p>Information that describes the status of a deployment rollback (for example, whether the deployment can't be rolled back, is in progress, failed, or succeeded). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RollbackInfo) -> dict:
    out: dict = {}
    if "rollback_deployment_id" in value:
        out["rollbackDeploymentId"] = value["rollback_deployment_id"]
    if "rollback_triggering_deployment_id" in value:
        out["rollbackTriggeringDeploymentId"] = value[
            "rollback_triggering_deployment_id"
        ]
    if "rollback_message" in value:
        out["rollbackMessage"] = value["rollback_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RollbackInfo:
    out: RollbackInfo = {}  # type: ignore[typeddict-item]
    if "rollbackDeploymentId" in data:
        out["rollback_deployment_id"] = data["rollbackDeploymentId"]
    if "rollbackTriggeringDeploymentId" in data:
        out["rollback_triggering_deployment_id"] = data[
            "rollbackTriggeringDeploymentId"
        ]
    if "rollbackMessage" in data:
        out["rollback_message"] = data["rollbackMessage"]
    return out
