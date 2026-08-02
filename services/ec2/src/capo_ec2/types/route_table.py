"""Generated from Smithy shape ``com.amazonaws.ec2#RouteTable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.propagating_vgw_list
    import capo_ec2.types.route_list
    import capo_ec2.types.route_table_association_list
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class RouteTable(TypedDict, closed=True):
    associations: NotRequired[
        "capo_ec2.types.route_table_association_list.RouteTableAssociationList"
    ]
    """<p>The associations between the route table and your subnets or gateways.</p>"""
    propagating_vgws: NotRequired[
        "capo_ec2.types.propagating_vgw_list.PropagatingVgwList"
    ]
    """<p>Any virtual private gateway (VGW) propagating routes.</p>"""
    route_table_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the route table.</p>"""
    routes: NotRequired["capo_ec2.types.route_list.RouteList"]
    """<p>The routes in the route table.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the route table.</p>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the route table.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteTable, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "associations" in value:
        import capo_ec2.types.route_table_association_list

        capo_ec2.types.route_table_association_list.serialize_ec2_query(
            value["associations"], pairs, f"{key_prefix}AssociationSet"
        )
    if "propagating_vgws" in value:
        import capo_ec2.types.propagating_vgw_list

        capo_ec2.types.propagating_vgw_list.serialize_ec2_query(
            value["propagating_vgws"], pairs, f"{key_prefix}PropagatingVgwSet"
        )
    if "route_table_id" in value:
        pairs.append((f"{key_prefix}RouteTableId", str(value["route_table_id"])))
    if "routes" in value:
        import capo_ec2.types.route_list

        capo_ec2.types.route_list.serialize_ec2_query(
            value["routes"], pairs, f"{key_prefix}RouteSet"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))


def deserialize_ec2_query(el: Element) -> RouteTable:
    out: RouteTable = {}  # type: ignore[typeddict-item]
    if el.find("AssociationSet") is not None:
        import capo_ec2.types.route_table_association_list

        out["associations"] = (
            capo_ec2.types.route_table_association_list.deserialize_ec2_query(
                el, "AssociationSet"
            )
        )
    if el.find("PropagatingVgwSet") is not None:
        import capo_ec2.types.propagating_vgw_list

        out["propagating_vgws"] = (
            capo_ec2.types.propagating_vgw_list.deserialize_ec2_query(
                el, "PropagatingVgwSet"
            )
        )
    child_route_table_id = el.find("RouteTableId")
    if child_route_table_id is not None:
        out["route_table_id"] = str(child_route_table_id.text or "")
    if el.find("RouteSet") is not None:
        import capo_ec2.types.route_list

        out["routes"] = capo_ec2.types.route_list.deserialize_ec2_query(el, "RouteSet")
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    return out
