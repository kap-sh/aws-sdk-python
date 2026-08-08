"""Generated from Smithy shape ``com.amazonaws.ec2#RouteTableAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.route_table_association_state
    import capo_ec2.types.string


class RouteTableAssociation(TypedDict, closed=True):
    main: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this is the main route table.</p>"""
    route_table_association_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the association.</p>"""
    route_table_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the route table.</p>"""
    subnet_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the subnet. A subnet ID is not returned for an implicit association.</p>"""
    gateway_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the internet gateway or virtual private gateway.</p>"""
    public_ipv4_pool: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of a public IPv4 pool. A public IPv4 pool is a pool of IPv4 addresses that you've brought to Amazon Web Services with BYOIP.</p>"""
    association_state: NotRequired[
        "capo_ec2.types.route_table_association_state.RouteTableAssociationState"
    ]
    """<p>The state of the association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteTableAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "main" in value:
        pairs.append((f"{key_prefix}Main", "true" if value["main"] else "false"))
    if "route_table_association_id" in value:
        pairs.append(
            (
                f"{key_prefix}RouteTableAssociationId",
                str(value["route_table_association_id"]),
            )
        )
    if "route_table_id" in value:
        pairs.append((f"{key_prefix}RouteTableId", str(value["route_table_id"])))
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "gateway_id" in value:
        pairs.append((f"{key_prefix}GatewayId", str(value["gateway_id"])))
    if "public_ipv4_pool" in value:
        pairs.append((f"{key_prefix}PublicIpv4Pool", str(value["public_ipv4_pool"])))
    if "association_state" in value:
        import capo_ec2.types.route_table_association_state

        capo_ec2.types.route_table_association_state.serialize_ec2_query(
            value["association_state"], pairs, f"{key_prefix}AssociationState"
        )


def deserialize_ec2_query(el: Element) -> RouteTableAssociation:
    out: RouteTableAssociation = {}  # type: ignore[typeddict-item]
    child_main = el.find("main")
    if child_main is not None:
        out["main"] = (child_main.text or "").lower() == "true"
    child_route_table_association_id = el.find("routeTableAssociationId")
    if child_route_table_association_id is not None:
        out["route_table_association_id"] = str(
            child_route_table_association_id.text or ""
        )
    child_route_table_id = el.find("routeTableId")
    if child_route_table_id is not None:
        out["route_table_id"] = str(child_route_table_id.text or "")
    child_subnet_id = el.find("subnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_gateway_id = el.find("gatewayId")
    if child_gateway_id is not None:
        out["gateway_id"] = str(child_gateway_id.text or "")
    child_public_ipv4_pool = el.find("publicIpv4Pool")
    if child_public_ipv4_pool is not None:
        out["public_ipv4_pool"] = str(child_public_ipv4_pool.text or "")
    child_association_state = el.find("associationState")
    if child_association_state is not None:
        import capo_ec2.types.route_table_association_state

        out["association_state"] = (
            capo_ec2.types.route_table_association_state.deserialize_ec2_query(
                child_association_state
            )
        )
    return out
