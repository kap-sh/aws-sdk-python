"""Generated from Smithy shape ``com.amazonaws.ec2#CoipCidr``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipv4_pool_coip_id
    import capo_ec2.types.string


class CoipCidr(TypedDict, closed=True):
    cidr: NotRequired["capo_ec2.types.string.String"]
    """<p> An address range in a customer-owned IP address space. </p>"""
    coip_pool_id: NotRequired["capo_ec2.types.ipv4_pool_coip_id.Ipv4PoolCoipId"]
    """<p> The ID of the address pool. </p>"""
    local_gateway_route_table_id: NotRequired["capo_ec2.types.string.String"]
    """<p> The ID of the local gateway route table. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CoipCidr, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cidr" in value:
        pairs.append((f"{prefix}.Cidr", str(value["cidr"])))
    if "coip_pool_id" in value:
        pairs.append((f"{prefix}.CoipPoolId", str(value["coip_pool_id"])))
    if "local_gateway_route_table_id" in value:
        pairs.append(
            (
                f"{prefix}.LocalGatewayRouteTableId",
                str(value["local_gateway_route_table_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> CoipCidr:
    out: CoipCidr = {}  # type: ignore[typeddict-item]
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    child_coip_pool_id = el.find("CoipPoolId")
    if child_coip_pool_id is not None:
        out["coip_pool_id"] = str(child_coip_pool_id.text or "")
    child_local_gateway_route_table_id = el.find("LocalGatewayRouteTableId")
    if child_local_gateway_route_table_id is not None:
        out["local_gateway_route_table_id"] = str(
            child_local_gateway_route_table_id.text or ""
        )
    return out
