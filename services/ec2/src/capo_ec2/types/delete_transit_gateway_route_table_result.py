"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayRouteTableResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_route_table


class DeleteTransitGatewayRouteTableResult(TypedDict, closed=True):
    transit_gateway_route_table: NotRequired[
        "capo_ec2.types.transit_gateway_route_table.TransitGatewayRouteTable"
    ]
    """<p>Information about the deleted transit gateway route table.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTransitGatewayRouteTableResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_route_table" in value:
        import capo_ec2.types.transit_gateway_route_table

        capo_ec2.types.transit_gateway_route_table.serialize_ec2_query(
            value["transit_gateway_route_table"],
            pairs,
            f"{key_prefix}TransitGatewayRouteTable",
        )


def deserialize_ec2_query(el: Element) -> DeleteTransitGatewayRouteTableResult:
    out: DeleteTransitGatewayRouteTableResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_route_table = el.find("TransitGatewayRouteTable")
    if child_transit_gateway_route_table is not None:
        import capo_ec2.types.transit_gateway_route_table

        out["transit_gateway_route_table"] = (
            capo_ec2.types.transit_gateway_route_table.deserialize_ec2_query(
                child_transit_gateway_route_table
            )
        )
    return out
