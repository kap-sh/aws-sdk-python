"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceEndpoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_service_health_check_config
    import aws_sdk_lightsail.types.integer
    import aws_sdk_lightsail.types.string


class ContainerServiceEndpoint(TypedDict):
    container_name: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The name of the container entry of the deployment that the endpoint configuration applies to.</p>"""
    container_port: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The port of the specified container to which traffic is forwarded to.</p>"""
    health_check: NotRequired[
        "aws_sdk_lightsail.types.container_service_health_check_config.ContainerServiceHealthCheckConfig"
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
        import aws_sdk_lightsail.types.container_service_health_check_config

        out["healthCheck"] = (
            aws_sdk_lightsail.types.container_service_health_check_config.serialize_aws_json_1_1(
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
        import aws_sdk_lightsail.types.container_service_health_check_config

        out["health_check"] = (
            aws_sdk_lightsail.types.container_service_health_check_config.deserialize_aws_json_1_1(
                data["healthCheck"]
            )
        )
    return out
