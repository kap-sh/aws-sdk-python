"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceIpv6AddressListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_ipv6_address_request

InstanceIpv6AddressListRequest: TypeAlias = list[
    "capo_ec2.types.instance_ipv6_address_request.InstanceIpv6AddressRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceIpv6AddressListRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.instance_ipv6_address_request

        capo_ec2.types.instance_ipv6_address_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> InstanceIpv6AddressListRequest:
    import capo_ec2.types.instance_ipv6_address_request

    out: InstanceIpv6AddressListRequest = []
    for child in el.findall("InstanceIpv6Address"):
        out.append(
            capo_ec2.types.instance_ipv6_address_request.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> InstanceIpv6AddressListRequest:
    import capo_ec2.types.instance_ipv6_address_request

    out: InstanceIpv6AddressListRequest = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.instance_ipv6_address_request.deserialize_ec2_query(child)
        )
    return out
