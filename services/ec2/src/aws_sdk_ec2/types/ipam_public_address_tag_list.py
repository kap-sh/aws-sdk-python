"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPublicAddressTagList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_public_address_tag

IpamPublicAddressTagList: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_public_address_tag.IpamPublicAddressTag"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPublicAddressTagList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.ipam_public_address_tag

        aws_sdk_ec2.types.ipam_public_address_tag.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> IpamPublicAddressTagList:
    import aws_sdk_ec2.types.ipam_public_address_tag

    out: IpamPublicAddressTagList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.ipam_public_address_tag.deserialize_ec2_query(child)
        )
    return out
