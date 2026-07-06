"""Generated from Smithy shape ``com.amazonaws.appmesh#HealthCheckPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.health_check_interval_millis
    import aws_sdk_app_mesh.types.health_check_threshold
    import aws_sdk_app_mesh.types.health_check_timeout_millis
    import aws_sdk_app_mesh.types.port_number
    import aws_sdk_app_mesh.types.port_protocol


class HealthCheckPolicy(TypedDict, closed=True):
    timeout_millis: (
        "aws_sdk_app_mesh.types.health_check_timeout_millis.HealthCheckTimeoutMillis"
    )
    """<p>The amount of time to wait when receiving a response from the health check, in milliseconds.</p>"""
    interval_millis: (
        "aws_sdk_app_mesh.types.health_check_interval_millis.HealthCheckIntervalMillis"
    )
    """<p>The time period in milliseconds between each health check execution.</p>"""
    protocol: "aws_sdk_app_mesh.types.port_protocol.PortProtocol"
    r"""<p>The protocol for the health check request. If you specify <code>grpc</code>, then your service must conform to the <a href=\"https://github.com/grpc/grpc/blob/master/doc/health-checking.md\">GRPC Health Checking Protocol</a>.</p>"""
    port: NotRequired["aws_sdk_app_mesh.types.port_number.PortNumber"]
    """<p>The destination port for the health check request. This port must match the port defined in the <a>PortMapping</a> for the listener.</p>"""
    path: NotRequired["str"]
    """<p>The destination path for the health check request. This value is only used if the specified protocol is HTTP or HTTP/2. For any other protocol, this value is ignored.</p>"""
    healthy_threshold: (
        "aws_sdk_app_mesh.types.health_check_threshold.HealthCheckThreshold"
    )
    """<p>The number of consecutive successful health checks that must occur before declaring listener healthy.</p>"""
    unhealthy_threshold: (
        "aws_sdk_app_mesh.types.health_check_threshold.HealthCheckThreshold"
    )
    """<p>The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HealthCheckPolicy) -> dict:
    out: dict = {}
    out["timeoutMillis"] = value["timeout_millis"]
    out["intervalMillis"] = value["interval_millis"]
    out["protocol"] = value["protocol"]
    if "port" in value:
        out["port"] = value["port"]
    if "path" in value:
        out["path"] = value["path"]
    out["healthyThreshold"] = value["healthy_threshold"]
    out["unhealthyThreshold"] = value["unhealthy_threshold"]
    return out


def deserialize_json(data: dict) -> HealthCheckPolicy:
    out: HealthCheckPolicy = {}  # type: ignore[typeddict-item]
    if "timeoutMillis" in data:
        out["timeout_millis"] = data["timeoutMillis"]
    else:
        raise DeserializationError("HealthCheckPolicy.timeout_millis required")
    if "intervalMillis" in data:
        out["interval_millis"] = data["intervalMillis"]
    else:
        raise DeserializationError("HealthCheckPolicy.interval_millis required")
    if "protocol" in data:
        out["protocol"] = data["protocol"]
    else:
        raise DeserializationError("HealthCheckPolicy.protocol required")
    if "port" in data:
        out["port"] = data["port"]
    if "path" in data:
        out["path"] = data["path"]
    if "healthyThreshold" in data:
        out["healthy_threshold"] = data["healthyThreshold"]
    else:
        raise DeserializationError("HealthCheckPolicy.healthy_threshold required")
    if "unhealthyThreshold" in data:
        out["unhealthy_threshold"] = data["unhealthyThreshold"]
    else:
        raise DeserializationError("HealthCheckPolicy.unhealthy_threshold required")
    return out
