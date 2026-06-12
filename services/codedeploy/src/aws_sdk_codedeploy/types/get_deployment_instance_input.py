"""Generated from Smithy shape ``com.amazonaws.codedeploy#GetDeploymentInstanceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_id
    import aws_sdk_codedeploy.types.instance_id


class GetDeploymentInstanceInput(TypedDict):
    deployment_id: "aws_sdk_codedeploy.types.deployment_id.DeploymentId"
    """<p> The unique ID of a deployment. </p>"""
    instance_id: "aws_sdk_codedeploy.types.instance_id.InstanceId"
    """<p> The unique ID of an instance in the deployment group. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeploymentInstanceInput) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    out["instanceId"] = value["instance_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeploymentInstanceInput:
    out: GetDeploymentInstanceInput = {}  # type: ignore[typeddict-item]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    else:
        raise DeserializationError("GetDeploymentInstanceInput.deployment_id required")
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    else:
        raise DeserializationError("GetDeploymentInstanceInput.instance_id required")
    return out
