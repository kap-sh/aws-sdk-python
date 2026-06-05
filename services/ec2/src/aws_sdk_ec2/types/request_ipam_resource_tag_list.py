"""Generated from Smithy shape ``com.amazonaws.ec2#RequestIpamResourceTagList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.request_ipam_resource_tag

RequestIpamResourceTagList: TypeAlias = list[
    "aws_sdk_ec2.types.request_ipam_resource_tag.RequestIpamResourceTag"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RequestIpamResourceTagList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.request_ipam_resource_tag

        aws_sdk_ec2.types.request_ipam_resource_tag.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> RequestIpamResourceTagList:
    import aws_sdk_ec2.types.request_ipam_resource_tag

    out: RequestIpamResourceTagList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.request_ipam_resource_tag.deserialize_ec2_query(child)
        )
    return out
