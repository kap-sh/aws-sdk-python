"""Generated from Smithy shape ``com.amazonaws.ec2#CustomerGatewayList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.customer_gateway

CustomerGatewayList: TypeAlias = list[
    "aws_sdk_ec2.types.customer_gateway.CustomerGateway"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CustomerGatewayList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.customer_gateway

        aws_sdk_ec2.types.customer_gateway.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> CustomerGatewayList:
    import aws_sdk_ec2.types.customer_gateway

    out: CustomerGatewayList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.customer_gateway.deserialize_ec2_query(child))
    return out
