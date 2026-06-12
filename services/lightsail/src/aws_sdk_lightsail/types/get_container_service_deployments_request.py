"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContainerServiceDeploymentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_service_name


class GetContainerServiceDeploymentsRequest(TypedDict):
    service_name: "aws_sdk_lightsail.types.container_service_name.ContainerServiceName"
    """<p>The name of the container service for which to return deployments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContainerServiceDeploymentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContainerServiceDeploymentsRequest:
    out: GetContainerServiceDeploymentsRequest = {}  # type: ignore[typeddict-item]
    return out
