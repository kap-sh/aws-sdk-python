"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.rule_group_source_list_details
    import aws_sdk_securityhub.types.rule_group_source_stateful_rules_list
    import aws_sdk_securityhub.types.rule_group_source_stateless_rules_and_custom_actions_details


class RuleGroupSource(TypedDict):
    rules_source_list: NotRequired[
        "aws_sdk_securityhub.types.rule_group_source_list_details.RuleGroupSourceListDetails"
    ]
    """<p>Stateful inspection criteria for a domain list rule group. A domain list rule group determines access by specific protocols to specific domains.</p>"""
    rules_string: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Stateful inspection criteria, provided in Suricata compatible intrusion prevention system (IPS) rules.</p>"""
    stateful_rules: NotRequired[
        "aws_sdk_securityhub.types.rule_group_source_stateful_rules_list.RuleGroupSourceStatefulRulesList"
    ]
    """<p>Suricata rule specifications.</p>"""
    stateless_rules_and_custom_actions: NotRequired[
        "aws_sdk_securityhub.types.rule_group_source_stateless_rules_and_custom_actions_details.RuleGroupSourceStatelessRulesAndCustomActionsDetails"
    ]
    """<p>The stateless rules and custom actions used by a stateless rule group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupSource) -> dict:
    out: dict = {}
    if "rules_source_list" in value:
        import aws_sdk_securityhub.types.rule_group_source_list_details

        out["RulesSourceList"] = (
            aws_sdk_securityhub.types.rule_group_source_list_details.serialize_json(
                value["rules_source_list"]
            )
        )
    if "rules_string" in value:
        out["RulesString"] = value["rules_string"]
    if "stateful_rules" in value:
        import aws_sdk_securityhub.types.rule_group_source_stateful_rules_list

        out["StatefulRules"] = (
            aws_sdk_securityhub.types.rule_group_source_stateful_rules_list.serialize_json(
                value["stateful_rules"]
            )
        )
    if "stateless_rules_and_custom_actions" in value:
        import aws_sdk_securityhub.types.rule_group_source_stateless_rules_and_custom_actions_details

        out["StatelessRulesAndCustomActions"] = (
            aws_sdk_securityhub.types.rule_group_source_stateless_rules_and_custom_actions_details.serialize_json(
                value["stateless_rules_and_custom_actions"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuleGroupSource:
    out: RuleGroupSource = {}  # type: ignore[typeddict-item]
    if "RulesSourceList" in data:
        import aws_sdk_securityhub.types.rule_group_source_list_details

        out["rules_source_list"] = (
            aws_sdk_securityhub.types.rule_group_source_list_details.deserialize_json(
                data["RulesSourceList"]
            )
        )
    if "RulesString" in data:
        out["rules_string"] = data["RulesString"]
    if "StatefulRules" in data:
        import aws_sdk_securityhub.types.rule_group_source_stateful_rules_list

        out["stateful_rules"] = (
            aws_sdk_securityhub.types.rule_group_source_stateful_rules_list.deserialize_json(
                data["StatefulRules"]
            )
        )
    if "StatelessRulesAndCustomActions" in data:
        import aws_sdk_securityhub.types.rule_group_source_stateless_rules_and_custom_actions_details

        out["stateless_rules_and_custom_actions"] = (
            aws_sdk_securityhub.types.rule_group_source_stateless_rules_and_custom_actions_details.deserialize_json(
                data["StatelessRulesAndCustomActions"]
            )
        )
    return out
