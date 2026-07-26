"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPolicyTableAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_policy_table_association

TransitGatewayPolicyTableAssociationList: TypeAlias = list[
    "capo_ec2.types.transit_gateway_policy_table_association.TransitGatewayPolicyTableAssociation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayPolicyTableAssociationList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.transit_gateway_policy_table_association

        capo_ec2.types.transit_gateway_policy_table_association.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> TransitGatewayPolicyTableAssociationList:
    import capo_ec2.types.transit_gateway_policy_table_association

    out: TransitGatewayPolicyTableAssociationList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.transit_gateway_policy_table_association.deserialize_ec2_query(
                child
            )
        )
    return out
