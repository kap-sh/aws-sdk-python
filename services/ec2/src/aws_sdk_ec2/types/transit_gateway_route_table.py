"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRouteTable``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.transit_gateway_route_table_state


class TransitGatewayRouteTable(TypedDict):
    transit_gateway_route_table_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway route table.</p>"""
    transit_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_state.TransitGatewayRouteTableState"
    ]
    """<p>The state of the transit gateway route table.</p>"""
    default_association_route_table: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this is the default association route table for the transit gateway.</p>"""
    default_propagation_route_table: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this is the default propagation route table for the transit gateway.</p>"""
    creation_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The creation time.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the route table.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayRouteTable, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "transit_gateway_route_table_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayRouteTableId",
                str(value["transit_gateway_route_table_id"]),
            )
        )
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))
    if "state" in value:
        import aws_sdk_ec2.types.transit_gateway_route_table_state

        aws_sdk_ec2.types.transit_gateway_route_table_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "default_association_route_table" in value:
        pairs.append(
            (
                f"{prefix}.DefaultAssociationRouteTable",
                "true" if value["default_association_route_table"] else "false",
            )
        )
    if "default_propagation_route_table" in value:
        pairs.append(
            (
                f"{prefix}.DefaultPropagationRouteTable",
                "true" if value["default_propagation_route_table"] else "false",
            )
        )
    if "creation_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["creation_time"], pairs, f"{prefix}.CreationTime"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayRouteTable:
    out: TransitGatewayRouteTable = {}  # type: ignore[typeddict-item]
    child_transit_gateway_route_table_id = el.find("TransitGatewayRouteTableId")
    if child_transit_gateway_route_table_id is not None:
        out["transit_gateway_route_table_id"] = str(
            child_transit_gateway_route_table_id.text or ""
        )
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.transit_gateway_route_table_state

        out["state"] = (
            aws_sdk_ec2.types.transit_gateway_route_table_state.deserialize_ec2_query(
                child_state
            )
        )
    child_default_association_route_table = el.find("DefaultAssociationRouteTable")
    if child_default_association_route_table is not None:
        out["default_association_route_table"] = (
            child_default_association_route_table.text or ""
        ).lower() == "true"
    child_default_propagation_route_table = el.find("DefaultPropagationRouteTable")
    if child_default_propagation_route_table is not None:
        out["default_propagation_route_table"] = (
            child_default_propagation_route_table.text or ""
        ).lower() == "true"
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        import aws_sdk_ec2.types.date_time

        out["creation_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_creation_time
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
