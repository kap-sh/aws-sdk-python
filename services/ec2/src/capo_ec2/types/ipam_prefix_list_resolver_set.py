"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_prefix_list_resolver

IpamPrefixListResolverSet: TypeAlias = list[
    "capo_ec2.types.ipam_prefix_list_resolver.IpamPrefixListResolver"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPrefixListResolverSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_prefix_list_resolver

        capo_ec2.types.ipam_prefix_list_resolver.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> IpamPrefixListResolverSet:
    import capo_ec2.types.ipam_prefix_list_resolver

    out: IpamPrefixListResolverSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ipam_prefix_list_resolver.deserialize_ec2_query(child)
        )
    return out
