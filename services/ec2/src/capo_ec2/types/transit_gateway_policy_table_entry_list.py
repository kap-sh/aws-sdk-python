"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPolicyTableEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_policy_table_entry

TransitGatewayPolicyTableEntryList: TypeAlias = list[
    "capo_ec2.types.transit_gateway_policy_table_entry.TransitGatewayPolicyTableEntry"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayPolicyTableEntryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.transit_gateway_policy_table_entry

        capo_ec2.types.transit_gateway_policy_table_entry.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayPolicyTableEntryList:
    import capo_ec2.types.transit_gateway_policy_table_entry

    out: TransitGatewayPolicyTableEntryList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.transit_gateway_policy_table_entry.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> TransitGatewayPolicyTableEntryList:
    import capo_ec2.types.transit_gateway_policy_table_entry

    out: TransitGatewayPolicyTableEntryList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.transit_gateway_policy_table_entry.deserialize_ec2_query(
                child
            )
        )
    return out
