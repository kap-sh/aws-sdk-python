"""Generated from Smithy shape ``com.amazonaws.ec2#IpamResourceTagList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_resource_tag

IpamResourceTagList: TypeAlias = list[
    "capo_ec2.types.ipam_resource_tag.IpamResourceTag"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamResourceTagList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_resource_tag

        capo_ec2.types.ipam_resource_tag.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> IpamResourceTagList:
    import capo_ec2.types.ipam_resource_tag

    out: IpamResourceTagList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.ipam_resource_tag.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> IpamResourceTagList:
    import capo_ec2.types.ipam_resource_tag

    out: IpamResourceTagList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.ipam_resource_tag.deserialize_ec2_query(child))
    return out
