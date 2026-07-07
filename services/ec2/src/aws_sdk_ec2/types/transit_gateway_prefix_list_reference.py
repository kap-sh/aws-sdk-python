"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPrefixListReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.prefix_list_resource_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_prefix_list_attachment
    import aws_sdk_ec2.types.transit_gateway_prefix_list_reference_state
    import aws_sdk_ec2.types.transit_gateway_route_table_id


class TransitGatewayPrefixListReference(TypedDict, closed=True):
    transit_gateway_route_table_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_id.TransitGatewayRouteTableId"
    ]
    """<p>The ID of the transit gateway route table.</p>"""
    prefix_list_id: NotRequired[
        "aws_sdk_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of the prefix list.</p>"""
    prefix_list_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the prefix list owner.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_prefix_list_reference_state.TransitGatewayPrefixListReferenceState"
    ]
    """<p>The state of the prefix list reference.</p>"""
    blackhole: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether traffic that matches this route is dropped.</p>"""
    transit_gateway_attachment: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_prefix_list_attachment.TransitGatewayPrefixListAttachment"
    ]
    """<p>Information about the transit gateway attachment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayPrefixListReference, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "transit_gateway_route_table_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayRouteTableId",
                str(value["transit_gateway_route_table_id"]),
            )
        )
    if "prefix_list_id" in value:
        pairs.append((f"{prefix}.PrefixListId", str(value["prefix_list_id"])))
    if "prefix_list_owner_id" in value:
        pairs.append(
            (f"{prefix}.PrefixListOwnerId", str(value["prefix_list_owner_id"]))
        )
    if "state" in value:
        import aws_sdk_ec2.types.transit_gateway_prefix_list_reference_state

        aws_sdk_ec2.types.transit_gateway_prefix_list_reference_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "blackhole" in value:
        pairs.append((f"{prefix}.Blackhole", "true" if value["blackhole"] else "false"))
    if "transit_gateway_attachment" in value:
        import aws_sdk_ec2.types.transit_gateway_prefix_list_attachment

        aws_sdk_ec2.types.transit_gateway_prefix_list_attachment.serialize_ec2_query(
            value["transit_gateway_attachment"],
            pairs,
            f"{prefix}.TransitGatewayAttachment",
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayPrefixListReference:
    out: TransitGatewayPrefixListReference = {}  # type: ignore[typeddict-item]
    child_transit_gateway_route_table_id = el.find("TransitGatewayRouteTableId")
    if child_transit_gateway_route_table_id is not None:
        out["transit_gateway_route_table_id"] = str(
            child_transit_gateway_route_table_id.text or ""
        )
    child_prefix_list_id = el.find("PrefixListId")
    if child_prefix_list_id is not None:
        out["prefix_list_id"] = str(child_prefix_list_id.text or "")
    child_prefix_list_owner_id = el.find("PrefixListOwnerId")
    if child_prefix_list_owner_id is not None:
        out["prefix_list_owner_id"] = str(child_prefix_list_owner_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.transit_gateway_prefix_list_reference_state

        out["state"] = (
            aws_sdk_ec2.types.transit_gateway_prefix_list_reference_state.deserialize_ec2_query(
                child_state
            )
        )
    child_blackhole = el.find("Blackhole")
    if child_blackhole is not None:
        out["blackhole"] = (child_blackhole.text or "").lower() == "true"
    child_transit_gateway_attachment = el.find("TransitGatewayAttachment")
    if child_transit_gateway_attachment is not None:
        import aws_sdk_ec2.types.transit_gateway_prefix_list_attachment

        out["transit_gateway_attachment"] = (
            aws_sdk_ec2.types.transit_gateway_prefix_list_attachment.deserialize_ec2_query(
                child_transit_gateway_attachment
            )
        )
    return out
