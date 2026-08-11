"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesIpv6AddressList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.scheduled_instances_ipv6_address

ScheduledInstancesIpv6AddressList: TypeAlias = list[
    "capo_ec2.types.scheduled_instances_ipv6_address.ScheduledInstancesIpv6Address"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScheduledInstancesIpv6AddressList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.scheduled_instances_ipv6_address

        capo_ec2.types.scheduled_instances_ipv6_address.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ScheduledInstancesIpv6AddressList:
    import capo_ec2.types.scheduled_instances_ipv6_address

    out: ScheduledInstancesIpv6AddressList = []
    for child in el.findall("Ipv6Address"):
        out.append(
            capo_ec2.types.scheduled_instances_ipv6_address.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> ScheduledInstancesIpv6AddressList:
    import capo_ec2.types.scheduled_instances_ipv6_address

    out: ScheduledInstancesIpv6AddressList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.scheduled_instances_ipv6_address.deserialize_ec2_query(child)
        )
    return out
