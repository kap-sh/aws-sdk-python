"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server_association_state
    import capo_ec2.types.route_server_id
    import capo_ec2.types.vpc_id


class RouteServerAssociation(TypedDict, closed=True):
    route_server_id: NotRequired["capo_ec2.types.route_server_id.RouteServerId"]
    """<p>The ID of the associated route server.</p>"""
    vpc_id: NotRequired["capo_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the associated VPC.</p>"""
    state: NotRequired[
        "capo_ec2.types.route_server_association_state.RouteServerAssociationState"
    ]
    """<p>The current state of the association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServerAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "route_server_id" in value:
        pairs.append((f"{key_prefix}RouteServerId", str(value["route_server_id"])))
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "state" in value:
        import capo_ec2.types.route_server_association_state

        capo_ec2.types.route_server_association_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )


def deserialize_ec2_query(el: Element) -> RouteServerAssociation:
    out: RouteServerAssociation = {}  # type: ignore[typeddict-item]
    child_route_server_id = el.find("routeServerId")
    if child_route_server_id is not None:
        out["route_server_id"] = str(child_route_server_id.text or "")
    child_vpc_id = el.find("vpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.route_server_association_state

        out["state"] = (
            capo_ec2.types.route_server_association_state.deserialize_ec2_query(
                child_state
            )
        )
    return out
