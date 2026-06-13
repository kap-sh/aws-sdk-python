"""Generated from Smithy shape ``com.amazonaws.proton#CancelServicePipelineDeploymentInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.resource_name


class CancelServicePipelineDeploymentInput(TypedDict):
    service_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service with the service pipeline deployment to cancel.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelServicePipelineDeploymentInput) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelServicePipelineDeploymentInput:
    out: CancelServicePipelineDeploymentInput = {}  # type: ignore[typeddict-item]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError(
            "CancelServicePipelineDeploymentInput.service_name required"
        )
    return out
