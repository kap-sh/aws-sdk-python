"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ModifyTargetGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.health_check_enabled
    import aws_sdk_elastic_load_balancing_v2.types.health_check_interval_seconds
    import aws_sdk_elastic_load_balancing_v2.types.health_check_port
    import aws_sdk_elastic_load_balancing_v2.types.health_check_threshold_count
    import aws_sdk_elastic_load_balancing_v2.types.health_check_timeout_seconds
    import aws_sdk_elastic_load_balancing_v2.types.matcher
    import aws_sdk_elastic_load_balancing_v2.types.path
    import aws_sdk_elastic_load_balancing_v2.types.protocol_enum
    import aws_sdk_elastic_load_balancing_v2.types.target_group_arn


class ModifyTargetGroupInput(TypedDict, closed=True):
    target_group_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_group_arn.TargetGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the target group.</p>"""
    health_check_protocol: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.protocol_enum.ProtocolEnum"
    ]
    """<p>The protocol the load balancer uses when performing health checks on targets. For Application Load Balancers, the default is HTTP. For Network Load Balancers and Gateway Load Balancers, the default is TCP. The TCP protocol is not supported for health checks if the protocol of the target group is HTTP or HTTPS. It is supported for health checks only if the protocol of the target group is TCP, TLS, UDP, or TCP_UDP. The GENEVE, TLS, UDP, TCP_UDP, QUIC, and TCP_QUIC protocols are not supported for health checks.</p>"""
    health_check_port: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.health_check_port.HealthCheckPort"
    ]
    """<p>The port the load balancer uses when performing health checks on targets.</p>"""
    health_check_path: NotRequired["aws_sdk_elastic_load_balancing_v2.types.path.Path"]
    """<p>[HTTP/HTTPS health checks] The destination for health checks on the targets.</p> <p>[HTTP1 or HTTP2 protocol version] The ping path. The default is /.</p> <p>[GRPC protocol version] The path of a custom health check method with the format /package.service/method. The default is /Amazon Web Services.ALB/healthcheck.</p>"""
    health_check_enabled: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.health_check_enabled.HealthCheckEnabled"
    ]
    """<p>Indicates whether health checks are enabled. If the target type is <code>lambda</code>, health checks are disabled by default but can be enabled. If the target type is <code>instance</code>, <code>ip</code>, or <code>alb</code>, health checks are always enabled and can't be disabled.</p>"""
    health_check_interval_seconds: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.health_check_interval_seconds.HealthCheckIntervalSeconds"
    ]
    """<p>The approximate amount of time, in seconds, between health checks of an individual target.</p>"""
    health_check_timeout_seconds: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.health_check_timeout_seconds.HealthCheckTimeoutSeconds"
    ]
    """<p>[HTTP/HTTPS health checks] The amount of time, in seconds, during which no response means a failed health check.</p>"""
    healthy_threshold_count: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.health_check_threshold_count.HealthCheckThresholdCount"
    ]
    """<p>The number of consecutive health checks successes required before considering an unhealthy target healthy.</p>"""
    unhealthy_threshold_count: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.health_check_threshold_count.HealthCheckThresholdCount"
    ]
    """<p>The number of consecutive health check failures required before considering the target unhealthy.</p>"""
    matcher: NotRequired["aws_sdk_elastic_load_balancing_v2.types.matcher.Matcher"]
    """<p>[HTTP/HTTPS health checks] The HTTP or gRPC codes to use when checking for a successful response from a target. For target groups with a protocol of TCP, TCP_UDP, UDP or TLS the range is 200-599. For target groups with a protocol of HTTP or HTTPS, the range is 200-499. For target groups with a protocol of GENEVE, the range is 200-399.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyTargetGroupInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "target_group_arn" in value:
        pairs.append((f"{prefix}.TargetGroupArn", str(value["target_group_arn"])))
    if "health_check_protocol" in value:
        import aws_sdk_elastic_load_balancing_v2.types.protocol_enum

        aws_sdk_elastic_load_balancing_v2.types.protocol_enum.serialize_query(
            value["health_check_protocol"], pairs, f"{prefix}.HealthCheckProtocol"
        )
    if "health_check_port" in value:
        pairs.append((f"{prefix}.HealthCheckPort", str(value["health_check_port"])))
    if "health_check_path" in value:
        pairs.append((f"{prefix}.HealthCheckPath", str(value["health_check_path"])))
    if "health_check_enabled" in value:
        pairs.append(
            (
                f"{prefix}.HealthCheckEnabled",
                "true" if value["health_check_enabled"] else "false",
            )
        )
    if "health_check_interval_seconds" in value:
        pairs.append(
            (
                f"{prefix}.HealthCheckIntervalSeconds",
                str(value["health_check_interval_seconds"]),
            )
        )
    if "health_check_timeout_seconds" in value:
        pairs.append(
            (
                f"{prefix}.HealthCheckTimeoutSeconds",
                str(value["health_check_timeout_seconds"]),
            )
        )
    if "healthy_threshold_count" in value:
        pairs.append(
            (f"{prefix}.HealthyThresholdCount", str(value["healthy_threshold_count"]))
        )
    if "unhealthy_threshold_count" in value:
        pairs.append(
            (
                f"{prefix}.UnhealthyThresholdCount",
                str(value["unhealthy_threshold_count"]),
            )
        )
    if "matcher" in value:
        import aws_sdk_elastic_load_balancing_v2.types.matcher

        aws_sdk_elastic_load_balancing_v2.types.matcher.serialize_query(
            value["matcher"], pairs, f"{prefix}.Matcher"
        )


def deserialize_query(el: Element) -> ModifyTargetGroupInput:
    out: ModifyTargetGroupInput = {}  # type: ignore[typeddict-item]
    child_target_group_arn = el.find("TargetGroupArn")
    if child_target_group_arn is not None:
        out["target_group_arn"] = str(child_target_group_arn.text or "")
    child_health_check_protocol = el.find("HealthCheckProtocol")
    if child_health_check_protocol is not None:
        import aws_sdk_elastic_load_balancing_v2.types.protocol_enum

        out["health_check_protocol"] = (
            aws_sdk_elastic_load_balancing_v2.types.protocol_enum.deserialize_query(
                child_health_check_protocol
            )
        )
    child_health_check_port = el.find("HealthCheckPort")
    if child_health_check_port is not None:
        out["health_check_port"] = str(child_health_check_port.text or "")
    child_health_check_path = el.find("HealthCheckPath")
    if child_health_check_path is not None:
        out["health_check_path"] = str(child_health_check_path.text or "")
    child_health_check_enabled = el.find("HealthCheckEnabled")
    if child_health_check_enabled is not None:
        out["health_check_enabled"] = (
            child_health_check_enabled.text or ""
        ).lower() == "true"
    child_health_check_interval_seconds = el.find("HealthCheckIntervalSeconds")
    if child_health_check_interval_seconds is not None:
        out["health_check_interval_seconds"] = int(
            child_health_check_interval_seconds.text or ""
        )
    child_health_check_timeout_seconds = el.find("HealthCheckTimeoutSeconds")
    if child_health_check_timeout_seconds is not None:
        out["health_check_timeout_seconds"] = int(
            child_health_check_timeout_seconds.text or ""
        )
    child_healthy_threshold_count = el.find("HealthyThresholdCount")
    if child_healthy_threshold_count is not None:
        out["healthy_threshold_count"] = int(child_healthy_threshold_count.text or "")
    child_unhealthy_threshold_count = el.find("UnhealthyThresholdCount")
    if child_unhealthy_threshold_count is not None:
        out["unhealthy_threshold_count"] = int(
            child_unhealthy_threshold_count.text or ""
        )
    child_matcher = el.find("Matcher")
    if child_matcher is not None:
        import aws_sdk_elastic_load_balancing_v2.types.matcher

        out["matcher"] = (
            aws_sdk_elastic_load_balancing_v2.types.matcher.deserialize_query(
                child_matcher
            )
        )
    return out
