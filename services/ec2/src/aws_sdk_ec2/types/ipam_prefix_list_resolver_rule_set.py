"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverRuleSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule

IpamPrefixListResolverRuleSet: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_prefix_list_resolver_rule.IpamPrefixListResolverRule"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPrefixListResolverRuleSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule

        aws_sdk_ec2.types.ipam_prefix_list_resolver_rule.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> IpamPrefixListResolverRuleSet:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule

    out: IpamPrefixListResolverRuleSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.ipam_prefix_list_resolver_rule.deserialize_ec2_query(
                child
            )
        )
    return out
