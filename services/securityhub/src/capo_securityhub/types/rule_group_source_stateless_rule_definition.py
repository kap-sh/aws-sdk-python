"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatelessRuleDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string_list
    import capo_securityhub.types.rule_group_source_stateless_rule_match_attributes


class RuleGroupSourceStatelessRuleDefinition(TypedDict, closed=True):
    actions: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The actions to take on a packet that matches one of the stateless rule definition's match attributes. You must specify a standard action (<code>aws:pass</code>, <code>aws:drop</code>, or <code>aws:forward_to_sfe</code>). You can then add custom actions.</p>"""
    match_attributes: NotRequired[
        "capo_securityhub.types.rule_group_source_stateless_rule_match_attributes.RuleGroupSourceStatelessRuleMatchAttributes"
    ]
    """<p>The criteria for Network Firewall to use to inspect an individual packet in a stateless rule inspection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupSourceStatelessRuleDefinition) -> dict:
    out: dict = {}
    if "actions" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Actions"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["actions"]
        )
    if "match_attributes" in value:
        import capo_securityhub.types.rule_group_source_stateless_rule_match_attributes

        out["MatchAttributes"] = (
            capo_securityhub.types.rule_group_source_stateless_rule_match_attributes.serialize_json(
                value["match_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuleGroupSourceStatelessRuleDefinition:
    out: RuleGroupSourceStatelessRuleDefinition = {}  # type: ignore[typeddict-item]
    if "Actions" in data:
        import capo_securityhub.types.non_empty_string_list

        out["actions"] = capo_securityhub.types.non_empty_string_list.deserialize_json(
            data["Actions"]
        )
    if "MatchAttributes" in data:
        import capo_securityhub.types.rule_group_source_stateless_rule_match_attributes

        out["match_attributes"] = (
            capo_securityhub.types.rule_group_source_stateless_rule_match_attributes.deserialize_json(
                data["MatchAttributes"]
            )
        )
    return out
