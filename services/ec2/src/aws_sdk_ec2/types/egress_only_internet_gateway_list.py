"""Generated from Smithy shape ``com.amazonaws.ec2#EgressOnlyInternetGatewayList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.egress_only_internet_gateway

EgressOnlyInternetGatewayList: TypeAlias = list[
    "aws_sdk_ec2.types.egress_only_internet_gateway.EgressOnlyInternetGateway"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EgressOnlyInternetGatewayList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.egress_only_internet_gateway

        aws_sdk_ec2.types.egress_only_internet_gateway.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> EgressOnlyInternetGatewayList:
    import aws_sdk_ec2.types.egress_only_internet_gateway

    out: EgressOnlyInternetGatewayList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.egress_only_internet_gateway.deserialize_ec2_query(child)
        )
    return out
