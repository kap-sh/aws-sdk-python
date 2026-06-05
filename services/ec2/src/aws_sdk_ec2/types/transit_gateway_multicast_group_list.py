"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulticastGroupList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_multicast_group

TransitGatewayMulticastGroupList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_multicast_group.TransitGatewayMulticastGroup"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayMulticastGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.transit_gateway_multicast_group

        aws_sdk_ec2.types.transit_gateway_multicast_group.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> TransitGatewayMulticastGroupList:
    import aws_sdk_ec2.types.transit_gateway_multicast_group

    out: TransitGatewayMulticastGroupList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.transit_gateway_multicast_group.deserialize_ec2_query(
                child
            )
        )
    return out
