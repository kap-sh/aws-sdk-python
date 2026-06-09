"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverVersionSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_version

IpamPrefixListResolverVersionSet: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_prefix_list_resolver_version.IpamPrefixListResolverVersion"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPrefixListResolverVersionSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_version

        aws_sdk_ec2.types.ipam_prefix_list_resolver_version.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> IpamPrefixListResolverVersionSet:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_version

    out: IpamPrefixListResolverVersionSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.ipam_prefix_list_resolver_version.deserialize_ec2_query(
                child
            )
        )
    return out
