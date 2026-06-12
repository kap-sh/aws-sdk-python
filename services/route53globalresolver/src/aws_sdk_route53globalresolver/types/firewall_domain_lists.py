"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#FirewallDomainLists``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.firewall_domain_lists_item

FirewallDomainLists: TypeAlias = list[
    "aws_sdk_route53globalresolver.types.firewall_domain_lists_item.FirewallDomainListsItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: FirewallDomainLists) -> list:
    import aws_sdk_route53globalresolver.types.firewall_domain_lists_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53globalresolver.types.firewall_domain_lists_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FirewallDomainLists:
    import aws_sdk_route53globalresolver.types.firewall_domain_lists_item

    out: FirewallDomainLists = []
    for item in data:
        out.append(
            aws_sdk_route53globalresolver.types.firewall_domain_lists_item.deserialize_json(
                item
            )
        )
    return out
