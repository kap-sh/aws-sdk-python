"""Generated from Smithy shape ``com.amazonaws.ec2#EgressOnlyInternetGatewayList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.egress_only_internet_gateway

EgressOnlyInternetGatewayList: TypeAlias = list[
    "capo_ec2.types.egress_only_internet_gateway.EgressOnlyInternetGateway"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EgressOnlyInternetGatewayList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.egress_only_internet_gateway

        capo_ec2.types.egress_only_internet_gateway.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> EgressOnlyInternetGatewayList:
    import capo_ec2.types.egress_only_internet_gateway

    out: EgressOnlyInternetGatewayList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.egress_only_internet_gateway.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> EgressOnlyInternetGatewayList:
    import capo_ec2.types.egress_only_internet_gateway

    out: EgressOnlyInternetGatewayList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.egress_only_internet_gateway.deserialize_ec2_query(child)
        )
    return out
