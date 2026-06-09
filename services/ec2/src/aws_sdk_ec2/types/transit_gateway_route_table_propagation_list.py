"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRouteTablePropagationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_route_table_propagation

TransitGatewayRouteTablePropagationList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_route_table_propagation.TransitGatewayRouteTablePropagation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayRouteTablePropagationList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.transit_gateway_route_table_propagation

        aws_sdk_ec2.types.transit_gateway_route_table_propagation.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> TransitGatewayRouteTablePropagationList:
    import aws_sdk_ec2.types.transit_gateway_route_table_propagation

    out: TransitGatewayRouteTablePropagationList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.transit_gateway_route_table_propagation.deserialize_ec2_query(
                child
            )
        )
    return out
