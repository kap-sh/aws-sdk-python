"""Generated from Smithy shape ``com.amazonaws.vpclattice#TargetGroupConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.health_check_config
    import capo_vpc_lattice.types.ip_address_type
    import capo_vpc_lattice.types.lambda_event_structure_version
    import capo_vpc_lattice.types.port
    import capo_vpc_lattice.types.target_group_protocol
    import capo_vpc_lattice.types.target_group_protocol_version
    import capo_vpc_lattice.types.vpc_id


class TargetGroupConfig(TypedDict, closed=True):
    port: NotRequired["capo_vpc_lattice.types.port.Port"]
    """<p>The port on which the targets are listening. For HTTP, the default is 80. For HTTPS, the default is 443. Not supported if the target group type is <code>LAMBDA</code>.</p>"""
    protocol: NotRequired[
        "capo_vpc_lattice.types.target_group_protocol.TargetGroupProtocol"
    ]
    """<p>The protocol to use for routing traffic to the targets. The default is the protocol of the target group. Not supported if the target group type is <code>LAMBDA</code>.</p>"""
    protocol_version: NotRequired[
        "capo_vpc_lattice.types.target_group_protocol_version.TargetGroupProtocolVersion"
    ]
    """<p>The protocol version. The default is <code>HTTP1</code>. Not supported if the target group type is <code>LAMBDA</code>.</p>"""
    ip_address_type: NotRequired["capo_vpc_lattice.types.ip_address_type.IpAddressType"]
    """<p>The type of IP address used for the target group. Supported only if the target group type is <code>IP</code>. The default is <code>IPV4</code>.</p>"""
    vpc_identifier: NotRequired["capo_vpc_lattice.types.vpc_id.VpcId"]
    """<p>The ID of the VPC. Not supported if the target group type is <code>LAMBDA</code>.</p>"""
    health_check: NotRequired[
        "capo_vpc_lattice.types.health_check_config.HealthCheckConfig"
    ]
    """<p>The health check configuration. Not supported if the target group type is <code>LAMBDA</code> or <code>ALB</code>.</p>"""
    lambda_event_structure_version: NotRequired[
        "capo_vpc_lattice.types.lambda_event_structure_version.LambdaEventStructureVersion"
    ]
    """<p>The version of the event structure that your Lambda function receives. Supported only if the target group type is <code>LAMBDA</code>. The default is <code>V1</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetGroupConfig) -> dict:
    out: dict = {}
    if "port" in value:
        out["port"] = value["port"]
    if "protocol" in value:
        out["protocol"] = value["protocol"]
    if "protocol_version" in value:
        out["protocolVersion"] = value["protocol_version"]
    if "ip_address_type" in value:
        out["ipAddressType"] = value["ip_address_type"]
    if "vpc_identifier" in value:
        out["vpcIdentifier"] = value["vpc_identifier"]
    if "health_check" in value:
        import capo_vpc_lattice.types.health_check_config

        out["healthCheck"] = capo_vpc_lattice.types.health_check_config.serialize_json(
            value["health_check"]
        )
    if "lambda_event_structure_version" in value:
        out["lambdaEventStructureVersion"] = value["lambda_event_structure_version"]
    return out


def deserialize_json(data: dict) -> TargetGroupConfig:
    out: TargetGroupConfig = {}  # type: ignore[typeddict-item]
    if "port" in data:
        out["port"] = data["port"]
    if "protocol" in data:
        out["protocol"] = data["protocol"]
    if "protocolVersion" in data:
        out["protocol_version"] = data["protocolVersion"]
    if "ipAddressType" in data:
        out["ip_address_type"] = data["ipAddressType"]
    if "vpcIdentifier" in data:
        out["vpc_identifier"] = data["vpcIdentifier"]
    if "healthCheck" in data:
        import capo_vpc_lattice.types.health_check_config

        out["health_check"] = (
            capo_vpc_lattice.types.health_check_config.deserialize_json(
                data["healthCheck"]
            )
        )
    if "lambdaEventStructureVersion" in data:
        out["lambda_event_structure_version"] = data["lambdaEventStructureVersion"]
    return out
