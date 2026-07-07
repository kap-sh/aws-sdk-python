"""Generated from Smithy shape ``com.amazonaws.proton#ListEnvironmentOutputsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.deployment_id
    import aws_sdk_proton.types.empty_next_token
    import aws_sdk_proton.types.resource_name


class ListEnvironmentOutputsInput(TypedDict, closed=True):
    environment_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The environment name.</p>"""
    next_token: NotRequired["aws_sdk_proton.types.empty_next_token.EmptyNextToken"]
    """<p>A token that indicates the location of the next environment output in the array of environment outputs, after the list of environment outputs that was previously requested.</p>"""
    deployment_id: NotRequired["aws_sdk_proton.types.deployment_id.DeploymentId"]
    """<p>The ID of the deployment whose outputs you want.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnvironmentOutputsInput) -> dict:
    out: dict = {}
    out["environmentName"] = value["environment_name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnvironmentOutputsInput:
    out: ListEnvironmentOutputsInput = {}  # type: ignore[typeddict-item]
    if "environmentName" in data:
        out["environment_name"] = data["environmentName"]
    else:
        raise DeserializationError(
            "ListEnvironmentOutputsInput.environment_name required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    return out
