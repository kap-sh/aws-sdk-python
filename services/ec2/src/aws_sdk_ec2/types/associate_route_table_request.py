"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateRouteTableRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipv4_pool_ec2_id
    import aws_sdk_ec2.types.route_gateway_id
    import aws_sdk_ec2.types.route_table_id
    import aws_sdk_ec2.types.subnet_id


class AssociateRouteTableRequest(TypedDict):
    gateway_id: NotRequired["aws_sdk_ec2.types.route_gateway_id.RouteGatewayId"]
    """<p>The ID of the internet gateway or virtual private gateway.</p>"""
    public_ipv4_pool: NotRequired["aws_sdk_ec2.types.ipv4_pool_ec2_id.Ipv4PoolEc2Id"]
    """<p>The ID of a public IPv4 pool. A public IPv4 pool is a pool of IPv4 addresses that you've brought to Amazon Web Services with BYOIP.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet.</p>"""
    route_table_id: NotRequired["aws_sdk_ec2.types.route_table_id.RouteTableId"]
    """<p>The ID of the route table.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateRouteTableRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "gateway_id" in value:
        pairs.append((f"{prefix}.GatewayId", str(value["gateway_id"])))
    if "public_ipv4_pool" in value:
        pairs.append((f"{prefix}.PublicIpv4Pool", str(value["public_ipv4_pool"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "route_table_id" in value:
        pairs.append((f"{prefix}.RouteTableId", str(value["route_table_id"])))


def deserialize_ec2_query(el: Element) -> AssociateRouteTableRequest:
    out: AssociateRouteTableRequest = {}  # type: ignore[typeddict-item]
    child_gateway_id = el.find("GatewayId")
    if child_gateway_id is not None:
        out["gateway_id"] = str(child_gateway_id.text or "")
    child_public_ipv4_pool = el.find("PublicIpv4Pool")
    if child_public_ipv4_pool is not None:
        out["public_ipv4_pool"] = str(child_public_ipv4_pool.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_route_table_id = el.find("RouteTableId")
    if child_route_table_id is not None:
        out["route_table_id"] = str(child_route_table_id.text or "")
    return out
