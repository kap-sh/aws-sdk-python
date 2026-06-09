"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayRouteList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_route

LocalGatewayRouteList: TypeAlias = list[
    "aws_sdk_ec2.types.local_gateway_route.LocalGatewayRoute"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LocalGatewayRouteList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.local_gateway_route

        aws_sdk_ec2.types.local_gateway_route.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> LocalGatewayRouteList:
    import aws_sdk_ec2.types.local_gateway_route

    out: LocalGatewayRouteList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.local_gateway_route.deserialize_ec2_query(child))
    return out
