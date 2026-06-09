"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceIpv6PrefixList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_ipv6_prefix

InstanceIpv6PrefixList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_ipv6_prefix.InstanceIpv6Prefix"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceIpv6PrefixList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.instance_ipv6_prefix

        aws_sdk_ec2.types.instance_ipv6_prefix.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> InstanceIpv6PrefixList:
    import aws_sdk_ec2.types.instance_ipv6_prefix

    out: InstanceIpv6PrefixList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.instance_ipv6_prefix.deserialize_ec2_query(child))
    return out
