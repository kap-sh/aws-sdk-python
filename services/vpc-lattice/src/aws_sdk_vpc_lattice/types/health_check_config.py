"""Generated from Smithy shape ``com.amazonaws.vpclattice#HealthCheckConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.boolean
    import aws_sdk_vpc_lattice.types.health_check_interval_seconds
    import aws_sdk_vpc_lattice.types.health_check_path
    import aws_sdk_vpc_lattice.types.health_check_port
    import aws_sdk_vpc_lattice.types.health_check_protocol_version
    import aws_sdk_vpc_lattice.types.health_check_timeout_seconds
    import aws_sdk_vpc_lattice.types.healthy_threshold_count
    import aws_sdk_vpc_lattice.types.matcher
    import aws_sdk_vpc_lattice.types.target_group_protocol
    import aws_sdk_vpc_lattice.types.unhealthy_threshold_count


class HealthCheckConfig(TypedDict):
    enabled: NotRequired["aws_sdk_vpc_lattice.types.boolean.Boolean"]
    """<p>Indicates whether health checking is enabled.</p>"""
    protocol: NotRequired[
        "aws_sdk_vpc_lattice.types.target_group_protocol.TargetGroupProtocol"
    ]
    """<p>The protocol used when performing health checks on targets. The possible protocols are <code>HTTP</code> and <code>HTTPS</code>. The default is <code>HTTP</code>.</p>"""
    protocol_version: NotRequired[
        "aws_sdk_vpc_lattice.types.health_check_protocol_version.HealthCheckProtocolVersion"
    ]
    """<p>The protocol version used when performing health checks on targets. The possible protocol versions are <code>HTTP1</code> and <code>HTTP2</code>.</p>"""
    port: NotRequired["aws_sdk_vpc_lattice.types.health_check_port.HealthCheckPort"]
    """<p>The port used when performing health checks on targets. The default setting is the port that a target receives traffic on.</p>"""
    path: NotRequired["aws_sdk_vpc_lattice.types.health_check_path.HealthCheckPath"]
    """<p>The destination for health checks on the targets. If the protocol version is <code>HTTP/1.1</code> or <code>HTTP/2</code>, specify a valid URI (for example, <code>/path?query</code>). The default path is <code>/</code>. Health checks are not supported if the protocol version is <code>gRPC</code>, however, you can choose <code>HTTP/1.1</code> or <code>HTTP/2</code> and specify a valid URI.</p>"""
    health_check_interval_seconds: NotRequired[
        "aws_sdk_vpc_lattice.types.health_check_interval_seconds.HealthCheckIntervalSeconds"
    ]
    """<p>The approximate amount of time, in seconds, between health checks of an individual target. The range is 5–300 seconds. The default is 30 seconds.</p>"""
    health_check_timeout_seconds: NotRequired[
        "aws_sdk_vpc_lattice.types.health_check_timeout_seconds.HealthCheckTimeoutSeconds"
    ]
    """<p>The amount of time, in seconds, to wait before reporting a target as unhealthy. The range is 1–120 seconds. The default is 5 seconds.</p>"""
    healthy_threshold_count: NotRequired[
        "aws_sdk_vpc_lattice.types.healthy_threshold_count.HealthyThresholdCount"
    ]
    """<p>The number of consecutive successful health checks required before considering an unhealthy target healthy. The range is 2–10. The default is 5.</p>"""
    unhealthy_threshold_count: NotRequired[
        "aws_sdk_vpc_lattice.types.unhealthy_threshold_count.UnhealthyThresholdCount"
    ]
    """<p>The number of consecutive failed health checks required before considering a target unhealthy. The range is 2–10. The default is 2.</p>"""
    matcher: NotRequired["aws_sdk_vpc_lattice.types.matcher.Matcher"]
    """<p>The codes to use when checking for a successful response from a target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HealthCheckConfig) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "protocol" in value:
        out["protocol"] = value["protocol"]
    if "protocol_version" in value:
        out["protocolVersion"] = value["protocol_version"]
    if "port" in value:
        out["port"] = value["port"]
    if "path" in value:
        out["path"] = value["path"]
    if "health_check_interval_seconds" in value:
        out["healthCheckIntervalSeconds"] = value["health_check_interval_seconds"]
    if "health_check_timeout_seconds" in value:
        out["healthCheckTimeoutSeconds"] = value["health_check_timeout_seconds"]
    if "healthy_threshold_count" in value:
        out["healthyThresholdCount"] = value["healthy_threshold_count"]
    if "unhealthy_threshold_count" in value:
        out["unhealthyThresholdCount"] = value["unhealthy_threshold_count"]
    if "matcher" in value:
        import aws_sdk_vpc_lattice.types.matcher

        out["matcher"] = aws_sdk_vpc_lattice.types.matcher.serialize_json(
            value["matcher"]
        )
    return out


def deserialize_json(data: dict) -> HealthCheckConfig:
    out: HealthCheckConfig = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "protocol" in data:
        out["protocol"] = data["protocol"]
    if "protocolVersion" in data:
        out["protocol_version"] = data["protocolVersion"]
    if "port" in data:
        out["port"] = data["port"]
    if "path" in data:
        out["path"] = data["path"]
    if "healthCheckIntervalSeconds" in data:
        out["health_check_interval_seconds"] = data["healthCheckIntervalSeconds"]
    if "healthCheckTimeoutSeconds" in data:
        out["health_check_timeout_seconds"] = data["healthCheckTimeoutSeconds"]
    if "healthyThresholdCount" in data:
        out["healthy_threshold_count"] = data["healthyThresholdCount"]
    if "unhealthyThresholdCount" in data:
        out["unhealthy_threshold_count"] = data["unhealthyThresholdCount"]
    if "matcher" in data:
        import aws_sdk_vpc_lattice.types.matcher

        out["matcher"] = aws_sdk_vpc_lattice.types.matcher.deserialize_json(
            data["matcher"]
        )
    return out
