"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverVersionSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_prefix_list_resolver_version

IpamPrefixListResolverVersionSet: TypeAlias = list[
    "capo_ec2.types.ipam_prefix_list_resolver_version.IpamPrefixListResolverVersion"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPrefixListResolverVersionSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_prefix_list_resolver_version

        capo_ec2.types.ipam_prefix_list_resolver_version.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> IpamPrefixListResolverVersionSet:
    import capo_ec2.types.ipam_prefix_list_resolver_version

    out: IpamPrefixListResolverVersionSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.ipam_prefix_list_resolver_version.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> IpamPrefixListResolverVersionSet:
    import capo_ec2.types.ipam_prefix_list_resolver_version

    out: IpamPrefixListResolverVersionSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ipam_prefix_list_resolver_version.deserialize_ec2_query(
                child
            )
        )
    return out
