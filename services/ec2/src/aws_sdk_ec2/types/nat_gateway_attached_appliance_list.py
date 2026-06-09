"""Generated from Smithy shape ``com.amazonaws.ec2#NatGatewayAttachedApplianceList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.nat_gateway_attached_appliance

NatGatewayAttachedApplianceList: TypeAlias = list[
    "aws_sdk_ec2.types.nat_gateway_attached_appliance.NatGatewayAttachedAppliance"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NatGatewayAttachedApplianceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.nat_gateway_attached_appliance

        aws_sdk_ec2.types.nat_gateway_attached_appliance.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> NatGatewayAttachedApplianceList:
    import aws_sdk_ec2.types.nat_gateway_attached_appliance

    out: NatGatewayAttachedApplianceList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.nat_gateway_attached_appliance.deserialize_ec2_query(
                child
            )
        )
    return out
