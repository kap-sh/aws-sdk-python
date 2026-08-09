"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceSecondaryInterfacePrivateIpAddressListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_secondary_interface_private_ip_address_request

InstanceSecondaryInterfacePrivateIpAddressListRequest: TypeAlias = list[
    "capo_ec2.types.instance_secondary_interface_private_ip_address_request.InstanceSecondaryInterfacePrivateIpAddressRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceSecondaryInterfacePrivateIpAddressListRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.instance_secondary_interface_private_ip_address_request

        capo_ec2.types.instance_secondary_interface_private_ip_address_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    el: Element,
) -> InstanceSecondaryInterfacePrivateIpAddressListRequest:
    import capo_ec2.types.instance_secondary_interface_private_ip_address_request

    out: InstanceSecondaryInterfacePrivateIpAddressListRequest = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.instance_secondary_interface_private_ip_address_request.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> InstanceSecondaryInterfacePrivateIpAddressListRequest:
    import capo_ec2.types.instance_secondary_interface_private_ip_address_request

    out: InstanceSecondaryInterfacePrivateIpAddressListRequest = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.instance_secondary_interface_private_ip_address_request.deserialize_ec2_query(
                child
            )
        )
    return out
