"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatelessRulesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.rule_group_source_stateless_rule_definition


class RuleGroupSourceStatelessRulesDetails(TypedDict, closed=True):
    priority: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>Indicates the order in which to run this rule relative to all of the rules in the stateless rule group.</p>"""
    rule_definition: NotRequired[
        "capo_securityhub.types.rule_group_source_stateless_rule_definition.RuleGroupSourceStatelessRuleDefinition"
    ]
    """<p>Provides the definition of the stateless rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupSourceStatelessRulesDetails) -> dict:
    out: dict = {}
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "rule_definition" in value:
        import capo_securityhub.types.rule_group_source_stateless_rule_definition

        out["RuleDefinition"] = (
            capo_securityhub.types.rule_group_source_stateless_rule_definition.serialize_json(
                value["rule_definition"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuleGroupSourceStatelessRulesDetails:
    out: RuleGroupSourceStatelessRulesDetails = {}  # type: ignore[typeddict-item]
    if "Priority" in data:
        out["priority"] = data["Priority"]
    if "RuleDefinition" in data:
        import capo_securityhub.types.rule_group_source_stateless_rule_definition

        out["rule_definition"] = (
            capo_securityhub.types.rule_group_source_stateless_rule_definition.deserialize_json(
                data["RuleDefinition"]
            )
        )
    return out
