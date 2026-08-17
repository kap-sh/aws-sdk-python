"""Generated from Smithy shape ``com.amazonaws.ec2#InstancePrivateIpAddressList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_private_ip_address

InstancePrivateIpAddressList: TypeAlias = list[
    "capo_ec2.types.instance_private_ip_address.InstancePrivateIpAddress"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstancePrivateIpAddressList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.instance_private_ip_address

        capo_ec2.types.instance_private_ip_address.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> InstancePrivateIpAddressList:
    import capo_ec2.types.instance_private_ip_address

    out: InstancePrivateIpAddressList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.instance_private_ip_address.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> InstancePrivateIpAddressList:
    import capo_ec2.types.instance_private_ip_address

    out: InstancePrivateIpAddressList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.instance_private_ip_address.deserialize_ec2_query(child)
        )
    return out
