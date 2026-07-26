"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatefulRulesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.rule_group_source_stateful_rules_header_details
    import capo_securityhub.types.rule_group_source_stateful_rules_options_list


class RuleGroupSourceStatefulRulesDetails(TypedDict, closed=True):
    action: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Defines what Network Firewall should do with the packets in a traffic flow when the flow matches the stateful rule criteria.</p>"""
    header: NotRequired[
        "capo_securityhub.types.rule_group_source_stateful_rules_header_details.RuleGroupSourceStatefulRulesHeaderDetails"
    ]
    """<p>The stateful inspection criteria for the rule.</p>"""
    rule_options: NotRequired[
        "capo_securityhub.types.rule_group_source_stateful_rules_options_list.RuleGroupSourceStatefulRulesOptionsList"
    ]
    """<p>Additional options for the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupSourceStatefulRulesDetails) -> dict:
    out: dict = {}
    if "action" in value:
        out["Action"] = value["action"]
    if "header" in value:
        import capo_securityhub.types.rule_group_source_stateful_rules_header_details

        out["Header"] = (
            capo_securityhub.types.rule_group_source_stateful_rules_header_details.serialize_json(
                value["header"]
            )
        )
    if "rule_options" in value:
        import capo_securityhub.types.rule_group_source_stateful_rules_options_list

        out["RuleOptions"] = (
            capo_securityhub.types.rule_group_source_stateful_rules_options_list.serialize_json(
                value["rule_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuleGroupSourceStatefulRulesDetails:
    out: RuleGroupSourceStatefulRulesDetails = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        out["action"] = data["Action"]
    if "Header" in data:
        import capo_securityhub.types.rule_group_source_stateful_rules_header_details

        out["header"] = (
            capo_securityhub.types.rule_group_source_stateful_rules_header_details.deserialize_json(
                data["Header"]
            )
        )
    if "RuleOptions" in data:
        import capo_securityhub.types.rule_group_source_stateful_rules_options_list

        out["rule_options"] = (
            capo_securityhub.types.rule_group_source_stateful_rules_options_list.deserialize_json(
                data["RuleOptions"]
            )
        )
    return out
