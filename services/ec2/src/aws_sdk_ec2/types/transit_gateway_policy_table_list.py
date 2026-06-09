"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPolicyTableList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_policy_table

TransitGatewayPolicyTableList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_policy_table.TransitGatewayPolicyTable"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayPolicyTableList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.transit_gateway_policy_table

        aws_sdk_ec2.types.transit_gateway_policy_table.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> TransitGatewayPolicyTableList:
    import aws_sdk_ec2.types.transit_gateway_policy_table

    out: TransitGatewayPolicyTableList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.transit_gateway_policy_table.deserialize_ec2_query(child)
        )
    return out
