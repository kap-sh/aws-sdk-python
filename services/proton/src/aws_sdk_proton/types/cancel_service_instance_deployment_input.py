"""Generated from Smithy shape ``com.amazonaws.proton#CancelServiceInstanceDeploymentInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.resource_name


class CancelServiceInstanceDeploymentInput(TypedDict):
    service_instance_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service instance with the deployment to cancel.</p>"""
    service_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service with the service instance deployment to cancel.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelServiceInstanceDeploymentInput) -> dict:
    out: dict = {}
    out["serviceInstanceName"] = value["service_instance_name"]
    out["serviceName"] = value["service_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelServiceInstanceDeploymentInput:
    out: CancelServiceInstanceDeploymentInput = {}  # type: ignore[typeddict-item]
    if "serviceInstanceName" in data:
        out["service_instance_name"] = data["serviceInstanceName"]
    else:
        raise DeserializationError(
            "CancelServiceInstanceDeploymentInput.service_instance_name required"
        )
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError(
            "CancelServiceInstanceDeploymentInput.service_name required"
        )
    return out
