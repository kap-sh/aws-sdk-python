"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#FirewallRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53globalresolver.types.firewall_rules_item

FirewallRules: TypeAlias = list[
    "capo_route53globalresolver.types.firewall_rules_item.FirewallRulesItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: FirewallRules) -> list:
    import capo_route53globalresolver.types.firewall_rules_item

    out: list = []
    for item in value:
        out.append(
            capo_route53globalresolver.types.firewall_rules_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FirewallRules:
    import capo_route53globalresolver.types.firewall_rules_item

    out: FirewallRules = []
    for item in data:
        out.append(
            capo_route53globalresolver.types.firewall_rules_item.deserialize_json(item)
        )
    return out
