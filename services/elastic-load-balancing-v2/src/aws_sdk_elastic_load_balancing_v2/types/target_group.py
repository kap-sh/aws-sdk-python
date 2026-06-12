"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TargetGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.health_check_enabled
    import aws_sdk_elastic_load_balancing_v2.types.health_check_interval_seconds
    import aws_sdk_elastic_load_balancing_v2.types.health_check_port
    import aws_sdk_elastic_load_balancing_v2.types.health_check_threshold_count
    import aws_sdk_elastic_load_balancing_v2.types.health_check_timeout_seconds
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_arns
    import aws_sdk_elastic_load_balancing_v2.types.matcher
    import aws_sdk_elastic_load_balancing_v2.types.path
    import aws_sdk_elastic_load_balancing_v2.types.port
    import aws_sdk_elastic_load_balancing_v2.types.protocol_enum
    import aws_sdk_elastic_load_balancing_v2.types.protocol_version
    import aws_sdk_elastic_load_balancing_v2.types.target_control_port
    import aws_sdk_elastic_load_balancing_v2.types.target_group_arn
    import aws_sdk_elastic_load_balancing_v2.types.target_group_ip_address_type_enum
    import aws_sdk_elastic_load_balancing_v2.types.target_group_name
    import aws_sdk_elastic_load_balancing_v2.types.target_type_enum
    import aws_sdk_elastic_load_balancing_v2.types.vpc_id


class TargetGroup(TypedDict):
    target_group_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_group_arn.TargetGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the target group.</p>"""
    target_group_name: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_group_name.TargetGroupName"
    ]
    """<p>The name of the target group.</p>"""
    protocol: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.protocol_enum.ProtocolEnum"
    ]
    """<p>The protocol to use for routing traffic to the targets.</p>"""
    port: NotRequired["aws_sdk_elastic_load_balancing_v2.types.port.Port"]
    """<p>The port on which the targets are listening. This parameter is not used if the target is a Lambda function.</p>"""
    vpc_id: NotRequired["aws_sdk_elastic_load_balancing_v2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC for the targets.</p>"""
    health_check_protocol: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.protocol_enum.ProtocolEnum"
    ]
    """<p>The protocol to use to connect with the target. The GENEVE, TLS, UDP, and TCP_UDP protocols are not supported for health checks.</p>"""
    health_check_port: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.health_check_port.HealthCheckPort"
    ]
    """<p>The port to use to connect with the target.</p>"""
    health_check_enabled: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.health_check_enabled.HealthCheckEnabled"
    ]
    """<p>Indicates whether health checks are enabled.</p>"""
    health_check_interval_seconds: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.health_check_interval_seconds.HealthCheckIntervalSeconds"
    ]
    """<p>The approximate amount of time, in seconds, between health checks of an individual target.</p>"""
    health_check_timeout_seconds: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.health_check_timeout_seconds.HealthCheckTimeoutSeconds"
    ]
    """<p>The amount of time, in seconds, during which no response means a failed health check.</p>"""
    healthy_threshold_count: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.health_check_threshold_count.HealthCheckThresholdCount"
    ]
    """<p>The number of consecutive health checks successes required before considering an unhealthy target healthy.</p>"""
    unhealthy_threshold_count: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.health_check_threshold_count.HealthCheckThresholdCount"
    ]
    """<p>The number of consecutive health check failures required before considering the target unhealthy.</p>"""
    health_check_path: NotRequired["aws_sdk_elastic_load_balancing_v2.types.path.Path"]
    """<p>The destination for health checks on the targets.</p>"""
    matcher: NotRequired["aws_sdk_elastic_load_balancing_v2.types.matcher.Matcher"]
    """<p>The HTTP or gRPC codes to use when checking for a successful response from a target.</p>"""
    load_balancer_arns: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.load_balancer_arns.LoadBalancerArns"
    ]
    """<p>The Amazon Resource Name (ARN) of the load balancer that routes traffic to this target group. You can use each target group with only one load balancer.</p>"""
    target_type: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_type_enum.TargetTypeEnum"
    ]
    """<p>The type of target that you must specify when registering targets with this target group. The possible values are <code>instance</code> (register targets by instance ID), <code>ip</code> (register targets by IP address), <code>lambda</code> (register a single Lambda function as a target), or <code>alb</code> (register a single Application Load Balancer as a target).</p>"""
    protocol_version: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.protocol_version.ProtocolVersion"
    ]
    """<p>[HTTP/HTTPS protocol] The protocol version. The possible values are <code>GRPC</code>, <code>HTTP1</code>, and <code>HTTP2</code>.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_group_ip_address_type_enum.TargetGroupIpAddressTypeEnum"
    ]
    """<p>The IP address type. The default value is <code>ipv4</code>.</p>"""
    target_control_port: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_control_port.TargetControlPort"
    ]
    """<p>The port on which the target control agent and application load balancer exchange management traffic for the target optimizer feature.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "target_group_arn" in value:
        pairs.append((f"{prefix}.TargetGroupArn", str(value["target_group_arn"])))
    if "target_group_name" in value:
        pairs.append((f"{prefix}.TargetGroupName", str(value["target_group_name"])))
    if "protocol" in value:
        import aws_sdk_elastic_load_balancing_v2.types.protocol_enum

        aws_sdk_elastic_load_balancing_v2.types.protocol_enum.serialize_query(
            value["protocol"], pairs, f"{prefix}.Protocol"
        )
    if "port" in value:
        pairs.append((f"{prefix}.Port", str(value["port"])))
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "health_check_protocol" in value:
        import aws_sdk_elastic_load_balancing_v2.types.protocol_enum

        aws_sdk_elastic_load_balancing_v2.types.protocol_enum.serialize_query(
            value["health_check_protocol"], pairs, f"{prefix}.HealthCheckProtocol"
        )
    if "health_check_port" in value:
        pairs.append((f"{prefix}.HealthCheckPort", str(value["health_check_port"])))
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
    if "health_check_path" in value:
        pairs.append((f"{prefix}.HealthCheckPath", str(value["health_check_path"])))
    if "matcher" in value:
        import aws_sdk_elastic_load_balancing_v2.types.matcher

        aws_sdk_elastic_load_balancing_v2.types.matcher.serialize_query(
            value["matcher"], pairs, f"{prefix}.Matcher"
        )
    if "load_balancer_arns" in value:
        import aws_sdk_elastic_load_balancing_v2.types.load_balancer_arns

        aws_sdk_elastic_load_balancing_v2.types.load_balancer_arns.serialize_query(
            value["load_balancer_arns"], pairs, f"{prefix}.LoadBalancerArns"
        )
    if "target_type" in value:
        import aws_sdk_elastic_load_balancing_v2.types.target_type_enum

        aws_sdk_elastic_load_balancing_v2.types.target_type_enum.serialize_query(
            value["target_type"], pairs, f"{prefix}.TargetType"
        )
    if "protocol_version" in value:
        pairs.append((f"{prefix}.ProtocolVersion", str(value["protocol_version"])))
    if "ip_address_type" in value:
        import aws_sdk_elastic_load_balancing_v2.types.target_group_ip_address_type_enum

        aws_sdk_elastic_load_balancing_v2.types.target_group_ip_address_type_enum.serialize_query(
            value["ip_address_type"], pairs, f"{prefix}.IpAddressType"
        )
    if "target_control_port" in value:
        pairs.append((f"{prefix}.TargetControlPort", str(value["target_control_port"])))


def deserialize_query(el: Element) -> TargetGroup:
    out: TargetGroup = {}  # type: ignore[typeddict-item]
    child_target_group_arn = el.find("TargetGroupArn")
    if child_target_group_arn is not None:
        out["target_group_arn"] = str(child_target_group_arn.text or "")
    child_target_group_name = el.find("TargetGroupName")
    if child_target_group_name is not None:
        out["target_group_name"] = str(child_target_group_name.text or "")
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        import aws_sdk_elastic_load_balancing_v2.types.protocol_enum

        out["protocol"] = (
            aws_sdk_elastic_load_balancing_v2.types.protocol_enum.deserialize_query(
                child_protocol
            )
        )
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
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
    child_health_check_path = el.find("HealthCheckPath")
    if child_health_check_path is not None:
        out["health_check_path"] = str(child_health_check_path.text or "")
    child_matcher = el.find("Matcher")
    if child_matcher is not None:
        import aws_sdk_elastic_load_balancing_v2.types.matcher

        out["matcher"] = (
            aws_sdk_elastic_load_balancing_v2.types.matcher.deserialize_query(
                child_matcher
            )
        )
    child_load_balancer_arns = el.find("LoadBalancerArns")
    if child_load_balancer_arns is not None:
        import aws_sdk_elastic_load_balancing_v2.types.load_balancer_arns

        out["load_balancer_arns"] = (
            aws_sdk_elastic_load_balancing_v2.types.load_balancer_arns.deserialize_query(
                child_load_balancer_arns
            )
        )
    child_target_type = el.find("TargetType")
    if child_target_type is not None:
        import aws_sdk_elastic_load_balancing_v2.types.target_type_enum

        out["target_type"] = (
            aws_sdk_elastic_load_balancing_v2.types.target_type_enum.deserialize_query(
                child_target_type
            )
        )
    child_protocol_version = el.find("ProtocolVersion")
    if child_protocol_version is not None:
        out["protocol_version"] = str(child_protocol_version.text or "")
    child_ip_address_type = el.find("IpAddressType")
    if child_ip_address_type is not None:
        import aws_sdk_elastic_load_balancing_v2.types.target_group_ip_address_type_enum

        out["ip_address_type"] = (
            aws_sdk_elastic_load_balancing_v2.types.target_group_ip_address_type_enum.deserialize_query(
                child_ip_address_type
            )
        )
    child_target_control_port = el.find("TargetControlPort")
    if child_target_control_port is not None:
        out["target_control_port"] = int(child_target_control_port.text or "")
    return out
