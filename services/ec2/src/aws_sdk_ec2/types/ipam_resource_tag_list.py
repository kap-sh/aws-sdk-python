"""Generated from Smithy shape ``com.amazonaws.ec2#IpamResourceTagList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_resource_tag

IpamResourceTagList: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_resource_tag.IpamResourceTag"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamResourceTagList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.ipam_resource_tag

        aws_sdk_ec2.types.ipam_resource_tag.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> IpamResourceTagList:
    import aws_sdk_ec2.types.ipam_resource_tag

    out: IpamResourceTagList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.ipam_resource_tag.deserialize_ec2_query(child))
    return out
