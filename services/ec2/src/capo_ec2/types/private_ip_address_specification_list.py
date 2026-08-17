"""Generated from Smithy shape ``com.amazonaws.ec2#PrivateIpAddressSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.private_ip_address_specification

PrivateIpAddressSpecificationList: TypeAlias = list[
    "capo_ec2.types.private_ip_address_specification.PrivateIpAddressSpecification"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PrivateIpAddressSpecificationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.private_ip_address_specification

        capo_ec2.types.private_ip_address_specification.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> PrivateIpAddressSpecificationList:
    import capo_ec2.types.private_ip_address_specification

    out: PrivateIpAddressSpecificationList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.private_ip_address_specification.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> PrivateIpAddressSpecificationList:
    import capo_ec2.types.private_ip_address_specification

    out: PrivateIpAddressSpecificationList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.private_ip_address_specification.deserialize_ec2_query(child)
        )
    return out
