"""Generated from Smithy shape ``com.amazonaws.rtbfabric#LinkRoutingRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rtbfabric.types.link_routing_rule_summary

LinkRoutingRuleList: TypeAlias = list[
    "capo_rtbfabric.types.link_routing_rule_summary.LinkRoutingRuleSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: LinkRoutingRuleList) -> list:
    import capo_rtbfabric.types.link_routing_rule_summary

    out: list = []
    for item in value:
        out.append(capo_rtbfabric.types.link_routing_rule_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> LinkRoutingRuleList:
    import capo_rtbfabric.types.link_routing_rule_summary

    out: LinkRoutingRuleList = []
    for item in data:
        out.append(
            capo_rtbfabric.types.link_routing_rule_summary.deserialize_json(item)
        )
    return out
