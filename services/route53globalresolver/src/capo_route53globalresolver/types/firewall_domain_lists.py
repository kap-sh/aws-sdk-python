"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#FirewallDomainLists``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53globalresolver.types.firewall_domain_lists_item

FirewallDomainLists: TypeAlias = list[
    "capo_route53globalresolver.types.firewall_domain_lists_item.FirewallDomainListsItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: FirewallDomainLists) -> list:
    import capo_route53globalresolver.types.firewall_domain_lists_item

    out: list = []
    for item in value:
        out.append(
            capo_route53globalresolver.types.firewall_domain_lists_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FirewallDomainLists:
    import capo_route53globalresolver.types.firewall_domain_lists_item

    out: FirewallDomainLists = []
    for item in data:
        out.append(
            capo_route53globalresolver.types.firewall_domain_lists_item.deserialize_json(
                item
            )
        )
    return out
