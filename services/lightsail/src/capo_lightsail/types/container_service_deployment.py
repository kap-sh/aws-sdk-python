"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceDeployment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.container_map
    import capo_lightsail.types.container_service_deployment_state
    import capo_lightsail.types.container_service_endpoint
    import capo_lightsail.types.integer
    import capo_lightsail.types.iso_date


class ContainerServiceDeployment(TypedDict, closed=True):
    version: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The version number of the deployment.</p>"""
    state: NotRequired[
        "capo_lightsail.types.container_service_deployment_state.ContainerServiceDeploymentState"
    ]
    """<p>The state of the deployment.</p> <p>A deployment can be in one of the following states:</p> <ul> <li> <p> <code>ACTIVATING</code> - The deployment is being created.</p> </li> <li> <p> <code>ACTIVE</code> - The deployment was successfully created, and it's currently running on the container service. The container service can have only one deployment in an active state at a time.</p> </li> <li> <p> <code>INACTIVE</code> - The deployment was previously successfully created, but it is not currently running on the container service.</p> </li> <li> <p> <code>FAILED</code> - The deployment failed. Use the <code>GetContainerLog</code> action to view the log events for the containers in the deployment to try to determine the reason for the failure.</p> </li> </ul>"""
    containers: NotRequired["capo_lightsail.types.container_map.ContainerMap"]
    """<p>An object that describes the configuration for the containers of the deployment.</p>"""
    public_endpoint: NotRequired[
        "capo_lightsail.types.container_service_endpoint.ContainerServiceEndpoint"
    ]
    """<p>An object that describes the endpoint of the deployment.</p>"""
    created_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the deployment was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServiceDeployment) -> dict:
    out: dict = {}
    if "version" in value:
        out["version"] = value["version"]
    if "state" in value:
        import capo_lightsail.types.container_service_deployment_state

        out["state"] = (
            capo_lightsail.types.container_service_deployment_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "containers" in value:
        import capo_lightsail.types.container_map

        out["containers"] = capo_lightsail.types.container_map.serialize_aws_json_1_1(
            value["containers"]
        )
    if "public_endpoint" in value:
        import capo_lightsail.types.container_service_endpoint

        out["publicEndpoint"] = (
            capo_lightsail.types.container_service_endpoint.serialize_aws_json_1_1(
                value["public_endpoint"]
            )
        )
    if "created_at" in value:
        import capo_lightsail.types.iso_date

        out["createdAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerServiceDeployment:
    out: ContainerServiceDeployment = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    if "state" in data:
        import capo_lightsail.types.container_service_deployment_state

        out["state"] = (
            capo_lightsail.types.container_service_deployment_state.deserialize_aws_json_1_1(
                data["state"]
            )
        )
    if "containers" in data:
        import capo_lightsail.types.container_map

        out["containers"] = capo_lightsail.types.container_map.deserialize_aws_json_1_1(
            data["containers"]
        )
    if "publicEndpoint" in data:
        import capo_lightsail.types.container_service_endpoint

        out["public_endpoint"] = (
            capo_lightsail.types.container_service_endpoint.deserialize_aws_json_1_1(
                data["publicEndpoint"]
            )
        )
    if "createdAt" in data:
        import capo_lightsail.types.iso_date

        out["created_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    return out
