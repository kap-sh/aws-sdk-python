"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#CreateTargetGroupInput``."""

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
    import aws_sdk_elastic_load_balancing_v2.types.port
    import aws_sdk_elastic_load_balancing_v2.types.protocol_enum
    import aws_sdk_elastic_load_balancing_v2.types.protocol_version
    import aws_sdk_elastic_load_balancing_v2.types.tag_list
    import aws_sdk_elastic_load_balancing_v2.types.target_control_port
    import aws_sdk_elastic_load_balancing_v2.types.target_group_ip_address_type_enum
    import aws_sdk_elastic_load_balancing_v2.types.target_group_name
    import aws_sdk_elastic_load_balancing_v2.types.target_type_enum
    import aws_sdk_elastic_load_balancing_v2.types.vpc_id


class CreateTargetGroupInput(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_group_name.TargetGroupName"
    ]
    """<p>The name of the target group.</p> <p>This name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.</p>"""
    protocol: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.protocol_enum.ProtocolEnum"
    ]
    """<p>The protocol to use for routing traffic to the targets. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocols are TCP, TLS, UDP, TCP_UDP, QUIC, or TCP_QUIC. For Gateway Load Balancers, the supported protocol is GENEVE. A TCP_UDP listener must be associated with a TCP_UDP target group. A TCP_QUIC listener must be associated with a TCP_QUIC target group. If the target is a Lambda function, this parameter does not apply.</p>"""
    protocol_version: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.protocol_version.ProtocolVersion"
    ]
    """<p>[HTTP/HTTPS protocol] The protocol version. Specify <code>GRPC</code> to send requests to targets using gRPC. Specify <code>HTTP2</code> to send requests to targets using HTTP/2. The default is <code>HTTP1</code>, which sends requests to targets using HTTP/1.1.</p>"""
    port: NotRequired["aws_sdk_elastic_load_balancing_v2.types.port.Port"]
    """<p>The port on which the targets receive traffic. This port is used unless you specify a port override when registering the target. If the target is a Lambda function, this parameter does not apply. If the protocol is GENEVE, the supported port is 6081.</p>"""
    vpc_id: NotRequired["aws_sdk_elastic_load_balancing_v2.types.vpc_id.VpcId"]
    """<p>The identifier of the virtual private cloud (VPC). If the target is a Lambda function, this parameter does not apply. Otherwise, this parameter is required.</p>"""
    health_check_protocol: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.protocol_enum.ProtocolEnum"
    ]
    """<p>The protocol the load balancer uses when performing health checks on targets. For Application Load Balancers, the default is HTTP. For Network Load Balancers and Gateway Load Balancers, the default is TCP. The TCP protocol is not supported for health checks if the protocol of the target group is HTTP or HTTPS. The GENEVE, TLS, UDP, TCP_UDP, QUIC, and TCP_QUIC protocols are not supported for health checks.</p>"""
    health_check_port: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.health_check_port.HealthCheckPort"
    ]
    """<p>The port the load balancer uses when performing health checks on targets. If the protocol is HTTP, HTTPS, TCP, TLS, UDP, TCP_UDP, QUIC, or TCP_QUIC the default is <code>traffic-port</code>, which is the port on which each target receives traffic from the load balancer. If the protocol is GENEVE, the default is port 80.</p>"""
    health_check_enabled: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.health_check_enabled.HealthCheckEnabled"
    ]
    """<p>Indicates whether health checks are enabled. If the target type is <code>lambda</code>, health checks are disabled by default but can be enabled. If the target type is <code>instance</code>, <code>ip</code>, or <code>alb</code>, health checks are always enabled and can't be disabled.</p>"""
    health_check_path: NotRequired["aws_sdk_elastic_load_balancing_v2.types.path.Path"]
    """<p>[HTTP/HTTPS health checks] The destination for health checks on the targets.</p> <p>[HTTP1 or HTTP2 protocol version] The ping path. The default is /.</p> <p>[GRPC protocol version] The path of a custom health check method with the format /package.service/method. The default is /Amazon Web Services.ALB/healthcheck.</p>"""
    health_check_interval_seconds: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.health_check_interval_seconds.HealthCheckIntervalSeconds"
    ]
    """<p>The approximate amount of time, in seconds, between health checks of an individual target. The range is 5-300. If the target group protocol is TCP, TLS, UDP, TCP_UDP, QUIC, TCP_QUIC, HTTP or HTTPS, the default is 30 seconds. If the target group protocol is GENEVE, the default is 10 seconds. If the target type is <code>lambda</code>, the default is 35 seconds.</p>"""
    health_check_timeout_seconds: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.health_check_timeout_seconds.HealthCheckTimeoutSeconds"
    ]
    """<p>The amount of time, in seconds, during which no response from a target means a failed health check. The range is 2–120 seconds. For target groups with a protocol of HTTP, the default is 6 seconds. For target groups with a protocol of TCP, TLS or HTTPS, the default is 10 seconds. For target groups with a protocol of GENEVE, the default is 5 seconds. If the target type is <code>lambda</code>, the default is 30 seconds.</p>"""
    healthy_threshold_count: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.health_check_threshold_count.HealthCheckThresholdCount"
    ]
    """<p>The number of consecutive health check successes required before considering a target healthy. The range is 2-10. If the target group protocol is TCP, TCP_UDP, UDP, TLS, HTTP or HTTPS, the default is 5. For target groups with a protocol of GENEVE, the default is 5. If the target type is <code>lambda</code>, the default is 5.</p>"""
    unhealthy_threshold_count: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.health_check_threshold_count.HealthCheckThresholdCount"
    ]
    """<p>The number of consecutive health check failures required before considering a target unhealthy. The range is 2-10. If the target group protocol is TCP, TCP_UDP, UDP, TLS, QUIC, TCP_QUIC, HTTP or HTTPS, the default is 2. For target groups with a protocol of GENEVE, the default is 2. If the target type is <code>lambda</code>, the default is 5.</p>"""
    matcher: NotRequired["aws_sdk_elastic_load_balancing_v2.types.matcher.Matcher"]
    """<p>[HTTP/HTTPS health checks] The HTTP or gRPC codes to use when checking for a successful response from a target. For target groups with a protocol of TCP, TCP_UDP, UDP, QUIC, TCP_QUIC, or TLS the range is 200-599. For target groups with a protocol of HTTP or HTTPS, the range is 200-499. For target groups with a protocol of GENEVE, the range is 200-399.</p>"""
    target_type: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_type_enum.TargetTypeEnum"
    ]
    """<p>The type of target that you must specify when registering targets with this target group. You can't specify targets for a target group using more than one target type.</p> <ul> <li> <p> <code>instance</code> - Register targets by instance ID. This is the default value.</p> </li> <li> <p> <code>ip</code> - Register targets by IP address. You can specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group, the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10). You can't specify publicly routable IP addresses.</p> </li> <li> <p> <code>lambda</code> - Register a single Lambda function as a target.</p> </li> <li> <p> <code>alb</code> - Register a single Application Load Balancer as a target.</p> </li> </ul>"""
    tags: NotRequired["aws_sdk_elastic_load_balancing_v2.types.tag_list.TagList"]
    """<p>The tags to assign to the target group.</p>"""
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
    value: CreateTargetGroupInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "protocol" in value:
        import aws_sdk_elastic_load_balancing_v2.types.protocol_enum

        aws_sdk_elastic_load_balancing_v2.types.protocol_enum.serialize_query(
            value["protocol"], pairs, f"{prefix}.Protocol"
        )
    if "protocol_version" in value:
        pairs.append((f"{prefix}.ProtocolVersion", str(value["protocol_version"])))
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
    if "health_check_path" in value:
        pairs.append((f"{prefix}.HealthCheckPath", str(value["health_check_path"])))
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
    if "target_type" in value:
        import aws_sdk_elastic_load_balancing_v2.types.target_type_enum

        aws_sdk_elastic_load_balancing_v2.types.target_type_enum.serialize_query(
            value["target_type"], pairs, f"{prefix}.TargetType"
        )
    if "tags" in value:
        import aws_sdk_elastic_load_balancing_v2.types.tag_list

        aws_sdk_elastic_load_balancing_v2.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )
    if "ip_address_type" in value:
        import aws_sdk_elastic_load_balancing_v2.types.target_group_ip_address_type_enum

        aws_sdk_elastic_load_balancing_v2.types.target_group_ip_address_type_enum.serialize_query(
            value["ip_address_type"], pairs, f"{prefix}.IpAddressType"
        )
    if "target_control_port" in value:
        pairs.append((f"{prefix}.TargetControlPort", str(value["target_control_port"])))


def deserialize_query(el: Element) -> CreateTargetGroupInput:
    out: CreateTargetGroupInput = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        import aws_sdk_elastic_load_balancing_v2.types.protocol_enum

        out["protocol"] = (
            aws_sdk_elastic_load_balancing_v2.types.protocol_enum.deserialize_query(
                child_protocol
            )
        )
    child_protocol_version = el.find("ProtocolVersion")
    if child_protocol_version is not None:
        out["protocol_version"] = str(child_protocol_version.text or "")
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
    child_health_check_path = el.find("HealthCheckPath")
    if child_health_check_path is not None:
        out["health_check_path"] = str(child_health_check_path.text or "")
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
    child_target_type = el.find("TargetType")
    if child_target_type is not None:
        import aws_sdk_elastic_load_balancing_v2.types.target_type_enum

        out["target_type"] = (
            aws_sdk_elastic_load_balancing_v2.types.target_type_enum.deserialize_query(
                child_target_type
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_elastic_load_balancing_v2.types.tag_list

        out["tags"] = (
            aws_sdk_elastic_load_balancing_v2.types.tag_list.deserialize_query(
                child_tags
            )
        )
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
