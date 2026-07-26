"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ManagedFirewallDomainLists``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53globalresolver.types.managed_firewall_domain_lists_item

ManagedFirewallDomainLists: TypeAlias = list[
    "capo_route53globalresolver.types.managed_firewall_domain_lists_item.ManagedFirewallDomainListsItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedFirewallDomainLists) -> list:
    import capo_route53globalresolver.types.managed_firewall_domain_lists_item

    out: list = []
    for item in value:
        out.append(
            capo_route53globalresolver.types.managed_firewall_domain_lists_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ManagedFirewallDomainLists:
    import capo_route53globalresolver.types.managed_firewall_domain_lists_item

    out: ManagedFirewallDomainLists = []
    for item in data:
        out.append(
            capo_route53globalresolver.types.managed_firewall_domain_lists_item.deserialize_json(
                item
            )
        )
    return out
