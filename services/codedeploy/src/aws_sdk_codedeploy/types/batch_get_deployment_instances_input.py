"""Generated from Smithy shape ``com.amazonaws.codedeploy#BatchGetDeploymentInstancesInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_id
    import aws_sdk_codedeploy.types.instances_list


class BatchGetDeploymentInstancesInput(TypedDict):
    deployment_id: "aws_sdk_codedeploy.types.deployment_id.DeploymentId"
    """<p> The unique ID of a deployment. </p>"""
    instance_ids: "aws_sdk_codedeploy.types.instances_list.InstancesList"
    """<p>The unique IDs of instances used in the deployment. The maximum number of instance IDs you can specify is 25.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDeploymentInstancesInput) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    import aws_sdk_codedeploy.types.instances_list

    out["instanceIds"] = aws_sdk_codedeploy.types.instances_list.serialize_aws_json_1_1(
        value["instance_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDeploymentInstancesInput:
    out: BatchGetDeploymentInstancesInput = {}  # type: ignore[typeddict-item]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    else:
        raise DeserializationError(
            "BatchGetDeploymentInstancesInput.deployment_id required"
        )
    if "instanceIds" in data:
        import aws_sdk_codedeploy.types.instances_list

        out["instance_ids"] = (
            aws_sdk_codedeploy.types.instances_list.deserialize_aws_json_1_1(
                data["instanceIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetDeploymentInstancesInput.instance_ids required"
        )
    return out
