"""Generated from Smithy shape ``com.amazonaws.ec2#InternetGatewayList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.internet_gateway

InternetGatewayList: TypeAlias = list[
    "aws_sdk_ec2.types.internet_gateway.InternetGateway"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InternetGatewayList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.internet_gateway

        aws_sdk_ec2.types.internet_gateway.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> InternetGatewayList:
    import aws_sdk_ec2.types.internet_gateway

    out: InternetGatewayList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.internet_gateway.deserialize_ec2_query(child))
    return out
