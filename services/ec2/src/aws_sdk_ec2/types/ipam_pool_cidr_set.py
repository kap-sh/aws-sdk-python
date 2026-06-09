"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolCidrSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool_cidr

IpamPoolCidrSet: TypeAlias = list["aws_sdk_ec2.types.ipam_pool_cidr.IpamPoolCidr"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPoolCidrSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.ipam_pool_cidr

        aws_sdk_ec2.types.ipam_pool_cidr.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> IpamPoolCidrSet:
    import aws_sdk_ec2.types.ipam_pool_cidr

    out: IpamPoolCidrSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.ipam_pool_cidr.deserialize_ec2_query(child))
    return out
