"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceIpv6PrefixList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_ipv6_prefix

InstanceIpv6PrefixList: TypeAlias = list[
    "capo_ec2.types.instance_ipv6_prefix.InstanceIpv6Prefix"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceIpv6PrefixList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.instance_ipv6_prefix

        capo_ec2.types.instance_ipv6_prefix.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> InstanceIpv6PrefixList:
    import capo_ec2.types.instance_ipv6_prefix

    out: InstanceIpv6PrefixList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.instance_ipv6_prefix.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> InstanceIpv6PrefixList:
    import capo_ec2.types.instance_ipv6_prefix

    out: InstanceIpv6PrefixList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.instance_ipv6_prefix.deserialize_ec2_query(child))
    return out
