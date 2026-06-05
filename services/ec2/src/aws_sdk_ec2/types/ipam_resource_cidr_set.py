"""Generated from Smithy shape ``com.amazonaws.ec2#IpamResourceCidrSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_resource_cidr

IpamResourceCidrSet: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_resource_cidr.IpamResourceCidr"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamResourceCidrSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.ipam_resource_cidr

        aws_sdk_ec2.types.ipam_resource_cidr.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> IpamResourceCidrSet:
    import aws_sdk_ec2.types.ipam_resource_cidr

    out: IpamResourceCidrSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.ipam_resource_cidr.deserialize_ec2_query(child))
    return out
