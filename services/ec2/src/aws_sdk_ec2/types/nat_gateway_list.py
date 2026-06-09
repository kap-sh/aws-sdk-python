"""Generated from Smithy shape ``com.amazonaws.ec2#NatGatewayList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.nat_gateway

NatGatewayList: TypeAlias = list["aws_sdk_ec2.types.nat_gateway.NatGateway"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NatGatewayList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.nat_gateway

        aws_sdk_ec2.types.nat_gateway.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> NatGatewayList:
    import aws_sdk_ec2.types.nat_gateway

    out: NatGatewayList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.nat_gateway.deserialize_ec2_query(child))
    return out
