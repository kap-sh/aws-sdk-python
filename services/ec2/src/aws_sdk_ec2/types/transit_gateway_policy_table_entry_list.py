"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPolicyTableEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_policy_table_entry

TransitGatewayPolicyTableEntryList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_policy_table_entry.TransitGatewayPolicyTableEntry"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayPolicyTableEntryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.transit_gateway_policy_table_entry

        aws_sdk_ec2.types.transit_gateway_policy_table_entry.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> TransitGatewayPolicyTableEntryList:
    import aws_sdk_ec2.types.transit_gateway_policy_table_entry

    out: TransitGatewayPolicyTableEntryList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.transit_gateway_policy_table_entry.deserialize_ec2_query(
                child
            )
        )
    return out
