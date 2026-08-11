"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPublicAddressTagList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_public_address_tag

IpamPublicAddressTagList: TypeAlias = list[
    "capo_ec2.types.ipam_public_address_tag.IpamPublicAddressTag"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPublicAddressTagList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_public_address_tag

        capo_ec2.types.ipam_public_address_tag.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> IpamPublicAddressTagList:
    import capo_ec2.types.ipam_public_address_tag

    out: IpamPublicAddressTagList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.ipam_public_address_tag.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> IpamPublicAddressTagList:
    import capo_ec2.types.ipam_public_address_tag

    out: IpamPublicAddressTagList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.ipam_public_address_tag.deserialize_ec2_query(child))
    return out
