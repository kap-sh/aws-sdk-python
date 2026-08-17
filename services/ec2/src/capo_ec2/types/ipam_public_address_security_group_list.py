"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPublicAddressSecurityGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_public_address_security_group

IpamPublicAddressSecurityGroupList: TypeAlias = list[
    "capo_ec2.types.ipam_public_address_security_group.IpamPublicAddressSecurityGroup"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPublicAddressSecurityGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_public_address_security_group

        capo_ec2.types.ipam_public_address_security_group.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> IpamPublicAddressSecurityGroupList:
    import capo_ec2.types.ipam_public_address_security_group

    out: IpamPublicAddressSecurityGroupList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.ipam_public_address_security_group.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> IpamPublicAddressSecurityGroupList:
    import capo_ec2.types.ipam_public_address_security_group

    out: IpamPublicAddressSecurityGroupList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ipam_public_address_security_group.deserialize_ec2_query(
                child
            )
        )
    return out
