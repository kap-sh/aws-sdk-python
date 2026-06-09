"""Generated from Smithy shape ``com.amazonaws.ec2#CarrierGatewaySet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.carrier_gateway

CarrierGatewaySet: TypeAlias = list["aws_sdk_ec2.types.carrier_gateway.CarrierGateway"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CarrierGatewaySet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.carrier_gateway

        aws_sdk_ec2.types.carrier_gateway.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> CarrierGatewaySet:
    import aws_sdk_ec2.types.carrier_gateway

    out: CarrierGatewaySet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.carrier_gateway.deserialize_ec2_query(child))
    return out
