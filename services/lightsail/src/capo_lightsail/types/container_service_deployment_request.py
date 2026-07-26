"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.container_map
    import capo_lightsail.types.endpoint_request


class ContainerServiceDeploymentRequest(TypedDict, closed=True):
    containers: NotRequired["capo_lightsail.types.container_map.ContainerMap"]
    """<p>An object that describes the configuration for the containers of the deployment.</p>"""
    public_endpoint: NotRequired[
        "capo_lightsail.types.endpoint_request.EndpointRequest"
    ]
    """<p>An object that describes the endpoint of the deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServiceDeploymentRequest) -> dict:
    out: dict = {}
    if "containers" in value:
        import capo_lightsail.types.container_map

        out["containers"] = capo_lightsail.types.container_map.serialize_aws_json_1_1(
            value["containers"]
        )
    if "public_endpoint" in value:
        import capo_lightsail.types.endpoint_request

        out["publicEndpoint"] = (
            capo_lightsail.types.endpoint_request.serialize_aws_json_1_1(
                value["public_endpoint"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerServiceDeploymentRequest:
    out: ContainerServiceDeploymentRequest = {}  # type: ignore[typeddict-item]
    if "containers" in data:
        import capo_lightsail.types.container_map

        out["containers"] = capo_lightsail.types.container_map.deserialize_aws_json_1_1(
            data["containers"]
        )
    if "publicEndpoint" in data:
        import capo_lightsail.types.endpoint_request

        out["public_endpoint"] = (
            capo_lightsail.types.endpoint_request.deserialize_aws_json_1_1(
                data["publicEndpoint"]
            )
        )
    return out
