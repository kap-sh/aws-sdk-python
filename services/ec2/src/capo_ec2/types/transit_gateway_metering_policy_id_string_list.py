"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMeteringPolicyIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_metering_policy_id

TransitGatewayMeteringPolicyIdStringList: TypeAlias = list[
    "capo_ec2.types.transit_gateway_metering_policy_id.TransitGatewayMeteringPolicyId"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayMeteringPolicyIdStringList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(
    parent: Element, tag: str
) -> TransitGatewayMeteringPolicyIdStringList:
    out: TransitGatewayMeteringPolicyIdStringList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
