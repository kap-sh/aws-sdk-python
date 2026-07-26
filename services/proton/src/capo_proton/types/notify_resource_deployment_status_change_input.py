"""Generated from Smithy shape ``com.amazonaws.proton#NotifyResourceDeploymentStatusChangeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.arn
    import capo_proton.types.deployment_id
    import capo_proton.types.outputs_list
    import capo_proton.types.resource_deployment_status
    import capo_proton.types.status_message


class NotifyResourceDeploymentStatusChangeInput(TypedDict, closed=True):
    resource_arn: "capo_proton.types.arn.Arn"
    """<p>The provisioned resource Amazon Resource Name (ARN).</p>"""
    status: NotRequired[
        "capo_proton.types.resource_deployment_status.ResourceDeploymentStatus"
    ]
    """<p>The status of your provisioned resource.</p>"""
    outputs: NotRequired["capo_proton.types.outputs_list.OutputsList"]
    """<p>The provisioned resource state change detail data that's returned by Proton.</p>"""
    deployment_id: NotRequired["capo_proton.types.deployment_id.DeploymentId"]
    """<p>The deployment ID for your provisioned resource.</p>"""
    status_message: NotRequired["capo_proton.types.status_message.StatusMessage"]
    """<p>The deployment status message for your provisioned resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotifyResourceDeploymentStatusChangeInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "outputs" in value:
        import capo_proton.types.outputs_list

        out["outputs"] = capo_proton.types.outputs_list.serialize_aws_json_1_0(
            value["outputs"]
        )
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> NotifyResourceDeploymentStatusChangeInput:
    out: NotifyResourceDeploymentStatusChangeInput = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError(
            "NotifyResourceDeploymentStatusChangeInput.resource_arn required"
        )
    if "status" in data:
        out["status"] = data["status"]
    if "outputs" in data:
        import capo_proton.types.outputs_list

        out["outputs"] = capo_proton.types.outputs_list.deserialize_aws_json_1_0(
            data["outputs"]
        )
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    return out
