"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverVersionEntrySet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_prefix_list_resolver_version_entry

IpamPrefixListResolverVersionEntrySet: TypeAlias = list[
    "capo_ec2.types.ipam_prefix_list_resolver_version_entry.IpamPrefixListResolverVersionEntry"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPrefixListResolverVersionEntrySet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_prefix_list_resolver_version_entry

        capo_ec2.types.ipam_prefix_list_resolver_version_entry.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> IpamPrefixListResolverVersionEntrySet:
    import capo_ec2.types.ipam_prefix_list_resolver_version_entry

    out: IpamPrefixListResolverVersionEntrySet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ipam_prefix_list_resolver_version_entry.deserialize_ec2_query(
                child
            )
        )
    return out
