"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceIpv4PrefixList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_ipv4_prefix

InstanceIpv4PrefixList: TypeAlias = list[
    "capo_ec2.types.instance_ipv4_prefix.InstanceIpv4Prefix"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceIpv4PrefixList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.instance_ipv4_prefix

        capo_ec2.types.instance_ipv4_prefix.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> InstanceIpv4PrefixList:
    import capo_ec2.types.instance_ipv4_prefix

    out: InstanceIpv4PrefixList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.instance_ipv4_prefix.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> InstanceIpv4PrefixList:
    import capo_ec2.types.instance_ipv4_prefix

    out: InstanceIpv4PrefixList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.instance_ipv4_prefix.deserialize_ec2_query(child))
    return out
