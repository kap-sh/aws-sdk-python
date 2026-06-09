"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConnectList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_connect

TransitGatewayConnectList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_connect.TransitGatewayConnect"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayConnectList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.transit_gateway_connect

        aws_sdk_ec2.types.transit_gateway_connect.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> TransitGatewayConnectList:
    import aws_sdk_ec2.types.transit_gateway_connect

    out: TransitGatewayConnectList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.transit_gateway_connect.deserialize_ec2_query(child)
        )
    return out
