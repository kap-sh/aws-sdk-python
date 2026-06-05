"""Generated from Smithy shape ``com.amazonaws.ec2#PublicIpv4PoolRangeSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.public_ipv4_pool_range

PublicIpv4PoolRangeSet: TypeAlias = list[
    "aws_sdk_ec2.types.public_ipv4_pool_range.PublicIpv4PoolRange"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PublicIpv4PoolRangeSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.public_ipv4_pool_range

        aws_sdk_ec2.types.public_ipv4_pool_range.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> PublicIpv4PoolRangeSet:
    import aws_sdk_ec2.types.public_ipv4_pool_range

    out: PublicIpv4PoolRangeSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.public_ipv4_pool_range.deserialize_ec2_query(child)
        )
    return out
