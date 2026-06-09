"""Generated from Smithy shape ``com.amazonaws.ec2#PublicIpv4PoolIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv4_pool_ec2_id

PublicIpv4PoolIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.ipv4_pool_ec2_id.Ipv4PoolEc2Id"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PublicIpv4PoolIdStringList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(parent: Element, tag: str) -> PublicIpv4PoolIdStringList:
    out: PublicIpv4PoolIdStringList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
