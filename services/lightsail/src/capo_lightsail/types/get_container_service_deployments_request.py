"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContainerServiceDeploymentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.container_service_name


class GetContainerServiceDeploymentsRequest(TypedDict, closed=True):
    service_name: "capo_lightsail.types.container_service_name.ContainerServiceName"
    """<p>The name of the container service for which to return deployments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContainerServiceDeploymentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContainerServiceDeploymentsRequest:
    out: GetContainerServiceDeploymentsRequest = {}  # type: ignore[typeddict-item]
    return out
