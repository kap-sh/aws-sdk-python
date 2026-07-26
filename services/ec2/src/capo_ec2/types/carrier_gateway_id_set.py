"""Generated from Smithy shape ``com.amazonaws.ec2#CarrierGatewayIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.carrier_gateway_id

CarrierGatewayIdSet: TypeAlias = list[
    "capo_ec2.types.carrier_gateway_id.CarrierGatewayId"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CarrierGatewayIdSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(parent: Element, tag: str) -> CarrierGatewayIdSet:
    out: CarrierGatewayIdSet = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
