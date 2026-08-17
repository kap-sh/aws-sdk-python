"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPolicyTableList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_policy_table

TransitGatewayPolicyTableList: TypeAlias = list[
    "capo_ec2.types.transit_gateway_policy_table.TransitGatewayPolicyTable"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayPolicyTableList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.transit_gateway_policy_table

        capo_ec2.types.transit_gateway_policy_table.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayPolicyTableList:
    import capo_ec2.types.transit_gateway_policy_table

    out: TransitGatewayPolicyTableList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.transit_gateway_policy_table.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> TransitGatewayPolicyTableList:
    import capo_ec2.types.transit_gateway_policy_table

    out: TransitGatewayPolicyTableList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.transit_gateway_policy_table.deserialize_ec2_query(child)
        )
    return out
