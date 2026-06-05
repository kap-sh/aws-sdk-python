"""Generated from Smithy shape ``com.amazonaws.ec2#PublicIpv4PoolSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.public_ipv4_pool

PublicIpv4PoolSet: TypeAlias = list["aws_sdk_ec2.types.public_ipv4_pool.PublicIpv4Pool"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PublicIpv4PoolSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.public_ipv4_pool

        aws_sdk_ec2.types.public_ipv4_pool.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> PublicIpv4PoolSet:
    import aws_sdk_ec2.types.public_ipv4_pool

    out: PublicIpv4PoolSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.public_ipv4_pool.deserialize_ec2_query(child))
    return out
