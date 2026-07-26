"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.container_service_health_check_config
    import capo_lightsail.types.integer
    import capo_lightsail.types.string


class ContainerServiceEndpoint(TypedDict, closed=True):
    container_name: NotRequired["capo_lightsail.types.string.string"]
    """<p>The name of the container entry of the deployment that the endpoint configuration applies to.</p>"""
    container_port: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The port of the specified container to which traffic is forwarded to.</p>"""
    health_check: NotRequired[
        "capo_lightsail.types.container_service_health_check_config.ContainerServiceHealthCheckConfig"
    ]
    """<p>An object that describes the health check configuration of the container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServiceEndpoint) -> dict:
    out: dict = {}
    if "container_name" in value:
        out["containerName"] = value["container_name"]
    if "container_port" in value:
        out["containerPort"] = value["container_port"]
    if "health_check" in value:
        import capo_lightsail.types.container_service_health_check_config

        out["healthCheck"] = (
            capo_lightsail.types.container_service_health_check_config.serialize_aws_json_1_1(
                value["health_check"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerServiceEndpoint:
    out: ContainerServiceEndpoint = {}  # type: ignore[typeddict-item]
    if "containerName" in data:
        out["container_name"] = data["containerName"]
    if "containerPort" in data:
        out["container_port"] = data["containerPort"]
    if "healthCheck" in data:
        import capo_lightsail.types.container_service_health_check_config

        out["health_check"] = (
            capo_lightsail.types.container_service_health_check_config.deserialize_aws_json_1_1(
                data["healthCheck"]
            )
        )
    return out
