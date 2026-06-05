"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool

IpamPoolSet: TypeAlias = list["aws_sdk_ec2.types.ipam_pool.IpamPool"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPoolSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.ipam_pool

        aws_sdk_ec2.types.ipam_pool.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> IpamPoolSet:
    import aws_sdk_ec2.types.ipam_pool

    out: IpamPoolSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.ipam_pool.deserialize_ec2_query(child))
    return out
