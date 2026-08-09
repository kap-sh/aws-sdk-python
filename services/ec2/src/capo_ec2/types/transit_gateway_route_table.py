"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRouteTable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.date_time
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.transit_gateway_route_table_state


class TransitGatewayRouteTable(TypedDict, closed=True):
    transit_gateway_route_table_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the transit gateway route table.</p>"""
    transit_gateway_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the transit gateway.</p>"""
    state: NotRequired[
        "capo_ec2.types.transit_gateway_route_table_state.TransitGatewayRouteTableState"
    ]
    """<p>The state of the transit gateway route table.</p>"""
    default_association_route_table: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this is the default association route table for the transit gateway.</p>"""
    default_propagation_route_table: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this is the default propagation route table for the transit gateway.</p>"""
    creation_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The creation time.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the route table.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayRouteTable, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_route_table_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayRouteTableId",
                str(value["transit_gateway_route_table_id"]),
            )
        )
    if "transit_gateway_id" in value:
        pairs.append(
            (f"{key_prefix}TransitGatewayId", str(value["transit_gateway_id"]))
        )
    if "state" in value:
        import capo_ec2.types.transit_gateway_route_table_state

        capo_ec2.types.transit_gateway_route_table_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "default_association_route_table" in value:
        pairs.append(
            (
                f"{key_prefix}DefaultAssociationRouteTable",
                "true" if value["default_association_route_table"] else "false",
            )
        )
    if "default_propagation_route_table" in value:
        pairs.append(
            (
                f"{key_prefix}DefaultPropagationRouteTable",
                "true" if value["default_propagation_route_table"] else "false",
            )
        )
    if "creation_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["creation_time"], pairs, f"{key_prefix}CreationTime"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayRouteTable:
    out: TransitGatewayRouteTable = {}  # type: ignore[typeddict-item]
    child_transit_gateway_route_table_id = el.find("transitGatewayRouteTableId")
    if child_transit_gateway_route_table_id is not None:
        out["transit_gateway_route_table_id"] = str(
            child_transit_gateway_route_table_id.text or ""
        )
    child_transit_gateway_id = el.find("transitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.transit_gateway_route_table_state

        out["state"] = (
            capo_ec2.types.transit_gateway_route_table_state.deserialize_ec2_query(
                child_state
            )
        )
    child_default_association_route_table = el.find("defaultAssociationRouteTable")
    if child_default_association_route_table is not None:
        out["default_association_route_table"] = (
            child_default_association_route_table.text or ""
        ).lower() == "true"
    child_default_propagation_route_table = el.find("defaultPropagationRouteTable")
    if child_default_propagation_route_table is not None:
        out["default_propagation_route_table"] = (
            child_default_propagation_route_table.text or ""
        ).lower() == "true"
    child_creation_time = el.find("creationTime")
    if child_creation_time is not None:
        import capo_ec2.types.date_time

        out["creation_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_creation_time
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out
