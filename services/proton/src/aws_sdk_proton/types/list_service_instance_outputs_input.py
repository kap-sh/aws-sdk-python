"""Generated from Smithy shape ``com.amazonaws.proton#ListServiceInstanceOutputsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.deployment_id
    import aws_sdk_proton.types.empty_next_token
    import aws_sdk_proton.types.resource_name


class ListServiceInstanceOutputsInput(TypedDict):
    service_instance_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service instance whose outputs you want.</p>"""
    service_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service that <code>serviceInstanceName</code> is associated to.</p>"""
    next_token: NotRequired["aws_sdk_proton.types.empty_next_token.EmptyNextToken"]
    """<p>A token that indicates the location of the next output in the array of outputs, after the list of outputs that was previously requested.</p>"""
    deployment_id: NotRequired["aws_sdk_proton.types.deployment_id.DeploymentId"]
    """<p>The ID of the deployment whose outputs you want.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServiceInstanceOutputsInput) -> dict:
    out: dict = {}
    out["serviceInstanceName"] = value["service_instance_name"]
    out["serviceName"] = value["service_name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListServiceInstanceOutputsInput:
    out: ListServiceInstanceOutputsInput = {}  # type: ignore[typeddict-item]
    if "serviceInstanceName" in data:
        out["service_instance_name"] = data["serviceInstanceName"]
    else:
        raise DeserializationError(
            "ListServiceInstanceOutputsInput.service_instance_name required"
        )
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError(
            "ListServiceInstanceOutputsInput.service_name required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    return out
