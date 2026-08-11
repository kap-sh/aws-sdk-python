"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConnectList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_connect

TransitGatewayConnectList: TypeAlias = list[
    "capo_ec2.types.transit_gateway_connect.TransitGatewayConnect"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayConnectList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.transit_gateway_connect

        capo_ec2.types.transit_gateway_connect.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayConnectList:
    import capo_ec2.types.transit_gateway_connect

    out: TransitGatewayConnectList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.transit_gateway_connect.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> TransitGatewayConnectList:
    import capo_ec2.types.transit_gateway_connect

    out: TransitGatewayConnectList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.transit_gateway_connect.deserialize_ec2_query(child))
    return out
