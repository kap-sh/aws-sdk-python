"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceIpv6AddressList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_ipv6_address

InstanceIpv6AddressList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_ipv6_address.InstanceIpv6Address"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceIpv6AddressList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.instance_ipv6_address

        aws_sdk_ec2.types.instance_ipv6_address.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> InstanceIpv6AddressList:
    import aws_sdk_ec2.types.instance_ipv6_address

    out: InstanceIpv6AddressList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.instance_ipv6_address.deserialize_ec2_query(child))
    return out
