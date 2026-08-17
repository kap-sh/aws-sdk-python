"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewaySet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.local_gateway

LocalGatewaySet: TypeAlias = list["capo_ec2.types.local_gateway.LocalGateway"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LocalGatewaySet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.local_gateway

        capo_ec2.types.local_gateway.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> LocalGatewaySet:
    import capo_ec2.types.local_gateway

    out: LocalGatewaySet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.local_gateway.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> LocalGatewaySet:
    import capo_ec2.types.local_gateway

    out: LocalGatewaySet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.local_gateway.deserialize_ec2_query(child))
    return out
