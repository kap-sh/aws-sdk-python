"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6PoolSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv6_pool

Ipv6PoolSet: TypeAlias = list["aws_sdk_ec2.types.ipv6_pool.Ipv6Pool"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Ipv6PoolSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.ipv6_pool

        aws_sdk_ec2.types.ipv6_pool.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> Ipv6PoolSet:
    import aws_sdk_ec2.types.ipv6_pool

    out: Ipv6PoolSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.ipv6_pool.deserialize_ec2_query(child))
    return out
