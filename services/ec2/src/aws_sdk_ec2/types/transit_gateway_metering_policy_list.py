"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMeteringPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_metering_policy

TransitGatewayMeteringPolicyList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_metering_policy.TransitGatewayMeteringPolicy"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayMeteringPolicyList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.transit_gateway_metering_policy

        aws_sdk_ec2.types.transit_gateway_metering_policy.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> TransitGatewayMeteringPolicyList:
    import aws_sdk_ec2.types.transit_gateway_metering_policy

    out: TransitGatewayMeteringPolicyList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.transit_gateway_metering_policy.deserialize_ec2_query(
                child
            )
        )
    return out
