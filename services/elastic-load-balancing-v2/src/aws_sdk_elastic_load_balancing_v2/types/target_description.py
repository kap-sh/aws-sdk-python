"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TargetDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.port
    import aws_sdk_elastic_load_balancing_v2.types.quic_server_id
    import aws_sdk_elastic_load_balancing_v2.types.target_id
    import aws_sdk_elastic_load_balancing_v2.types.zone_name


class TargetDescription(TypedDict):
    id: NotRequired["aws_sdk_elastic_load_balancing_v2.types.target_id.TargetId"]
    """<p>The ID of the target. If the target type of the target group is <code>instance</code>, specify an instance ID. If the target type is <code>ip</code>, specify an IP address. If the target type is <code>lambda</code>, specify the ARN of the Lambda function. If the target type is <code>alb</code>, specify the ARN of the Application Load Balancer target. </p>"""
    port: NotRequired["aws_sdk_elastic_load_balancing_v2.types.port.Port"]
    """<p>The port on which the target is listening. If the target group protocol is GENEVE, the supported port is 6081. If the target type is <code>alb</code>, the targeted Application Load Balancer must have at least one listener whose port matches the target group port. This parameter is not used if the target is a Lambda function.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.zone_name.ZoneName"
    ]
    """<p>An Availability Zone or <code>all</code>. This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer.</p> <p>For Application Load Balancer target groups, the specified Availability Zone value is only applicable when cross-zone load balancing is off. Otherwise the parameter is ignored and treated as <code>all</code>.</p> <p>This parameter is not supported if the target type of the target group is <code>instance</code> or <code>alb</code>.</p> <p>If the target type is <code>ip</code> and the IP address is in a subnet of the VPC for the target group, the Availability Zone is automatically detected and this parameter is optional. If the IP address is outside the VPC, this parameter is required.</p> <p>For Application Load Balancer target groups with cross-zone load balancing off, if the target type is <code>ip</code> and the IP address is outside of the VPC for the target group, this should be an Availability Zone inside the VPC for the target group.</p> <p>If the target type is <code>lambda</code>, this parameter is optional and the only supported value is <code>all</code>.</p>"""
    quic_server_id: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.quic_server_id.QuicServerId"
    ]
    """<p>The server ID for the targets. This value is required if the protocol is <code>QUIC</code> or <code>TCP_QUIC</code> and can't be used with other protocols.</p> <p>The ID consists of the <code>0x</code> prefix followed by 16 hexadecimal characters. Any letters must be lowercase. The value must be unique at the listener level. You can't modify the server ID for a registered target. You must deregister the target and then provide a new server ID when you register the target again.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "id" in value:
        pairs.append((f"{prefix}.Id", str(value["id"])))
    if "port" in value:
        pairs.append((f"{prefix}.Port", str(value["port"])))
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "quic_server_id" in value:
        pairs.append((f"{prefix}.QuicServerId", str(value["quic_server_id"])))


def deserialize_query(el: Element) -> TargetDescription:
    out: TargetDescription = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_quic_server_id = el.find("QuicServerId")
    if child_quic_server_id is not None:
        out["quic_server_id"] = str(child_quic_server_id.text or "")
    return out
