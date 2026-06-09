"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayRouteTableResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_route_table


class DeleteTransitGatewayRouteTableResult(TypedDict):
    transit_gateway_route_table: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table.TransitGatewayRouteTable"
    ]
    """<p>Information about the deleted transit gateway route table.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTransitGatewayRouteTableResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_route_table" in value:
        import aws_sdk_ec2.types.transit_gateway_route_table

        aws_sdk_ec2.types.transit_gateway_route_table.serialize_ec2_query(
            value["transit_gateway_route_table"],
            pairs,
            f"{prefix}.TransitGatewayRouteTable",
        )


def deserialize_ec2_query(el: Element) -> DeleteTransitGatewayRouteTableResult:
    out: DeleteTransitGatewayRouteTableResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_route_table = el.find("TransitGatewayRouteTable")
    if child_transit_gateway_route_table is not None:
        import aws_sdk_ec2.types.transit_gateway_route_table

        out["transit_gateway_route_table"] = (
            aws_sdk_ec2.types.transit_gateway_route_table.deserialize_ec2_query(
                child_transit_gateway_route_table
            )
        )
    return out
