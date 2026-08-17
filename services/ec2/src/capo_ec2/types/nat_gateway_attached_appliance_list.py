"""Generated from Smithy shape ``com.amazonaws.ec2#NatGatewayAttachedApplianceList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.nat_gateway_attached_appliance

NatGatewayAttachedApplianceList: TypeAlias = list[
    "capo_ec2.types.nat_gateway_attached_appliance.NatGatewayAttachedAppliance"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NatGatewayAttachedApplianceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.nat_gateway_attached_appliance

        capo_ec2.types.nat_gateway_attached_appliance.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> NatGatewayAttachedApplianceList:
    import capo_ec2.types.nat_gateway_attached_appliance

    out: NatGatewayAttachedApplianceList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.nat_gateway_attached_appliance.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> NatGatewayAttachedApplianceList:
    import capo_ec2.types.nat_gateway_attached_appliance

    out: NatGatewayAttachedApplianceList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.nat_gateway_attached_appliance.deserialize_ec2_query(child)
        )
    return out
