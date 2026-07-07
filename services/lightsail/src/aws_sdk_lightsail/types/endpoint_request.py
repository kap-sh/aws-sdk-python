"""Generated from Smithy shape ``com.amazonaws.lightsail#EndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_service_health_check_config
    import aws_sdk_lightsail.types.integer
    import aws_sdk_lightsail.types.string


class EndpointRequest(TypedDict, closed=True):
    container_name: "aws_sdk_lightsail.types.string.string"
    """<p>The name of the container for the endpoint.</p>"""
    container_port: "aws_sdk_lightsail.types.integer.integer"
    """<p>The port of the container to which traffic is forwarded to.</p>"""
    health_check: NotRequired[
        "aws_sdk_lightsail.types.container_service_health_check_config.ContainerServiceHealthCheckConfig"
    ]
    """<p>An object that describes the health check configuration of the container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointRequest) -> dict:
    out: dict = {}
    out["containerName"] = value["container_name"]
    out["containerPort"] = value["container_port"]
    if "health_check" in value:
        import aws_sdk_lightsail.types.container_service_health_check_config

        out["healthCheck"] = (
            aws_sdk_lightsail.types.container_service_health_check_config.serialize_aws_json_1_1(
                value["health_check"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointRequest:
    out: EndpointRequest = {}  # type: ignore[typeddict-item]
    if "containerName" in data:
        out["container_name"] = data["containerName"]
    else:
        raise DeserializationError("EndpointRequest.container_name required")
    if "containerPort" in data:
        out["container_port"] = data["containerPort"]
    else:
        raise DeserializationError("EndpointRequest.container_port required")
    if "healthCheck" in data:
        import aws_sdk_lightsail.types.container_service_health_check_config

        out["health_check"] = (
            aws_sdk_lightsail.types.container_service_health_check_config.deserialize_aws_json_1_1(
                data["healthCheck"]
            )
        )
    return out
