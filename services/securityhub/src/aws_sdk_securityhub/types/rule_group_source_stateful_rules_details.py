"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatefulRulesDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.rule_group_source_stateful_rules_header_details
    import aws_sdk_securityhub.types.rule_group_source_stateful_rules_options_list


class RuleGroupSourceStatefulRulesDetails(TypedDict):
    action: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Defines what Network Firewall should do with the packets in a traffic flow when the flow matches the stateful rule criteria.</p>"""
    header: NotRequired[
        "aws_sdk_securityhub.types.rule_group_source_stateful_rules_header_details.RuleGroupSourceStatefulRulesHeaderDetails"
    ]
    """<p>The stateful inspection criteria for the rule.</p>"""
    rule_options: NotRequired[
        "aws_sdk_securityhub.types.rule_group_source_stateful_rules_options_list.RuleGroupSourceStatefulRulesOptionsList"
    ]
    """<p>Additional options for the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupSourceStatefulRulesDetails) -> dict:
    out: dict = {}
    if "action" in value:
        out["Action"] = value["action"]
    if "header" in value:
        import aws_sdk_securityhub.types.rule_group_source_stateful_rules_header_details

        out["Header"] = (
            aws_sdk_securityhub.types.rule_group_source_stateful_rules_header_details.serialize_json(
                value["header"]
            )
        )
    if "rule_options" in value:
        import aws_sdk_securityhub.types.rule_group_source_stateful_rules_options_list

        out["RuleOptions"] = (
            aws_sdk_securityhub.types.rule_group_source_stateful_rules_options_list.serialize_json(
                value["rule_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuleGroupSourceStatefulRulesDetails:
    out: RuleGroupSourceStatefulRulesDetails = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        out["action"] = data["Action"]
    if "Header" in data:
        import aws_sdk_securityhub.types.rule_group_source_stateful_rules_header_details

        out["header"] = (
            aws_sdk_securityhub.types.rule_group_source_stateful_rules_header_details.deserialize_json(
                data["Header"]
            )
        )
    if "RuleOptions" in data:
        import aws_sdk_securityhub.types.rule_group_source_stateful_rules_options_list

        out["rule_options"] = (
            aws_sdk_securityhub.types.rule_group_source_stateful_rules_options_list.deserialize_json(
                data["RuleOptions"]
            )
        )
    return out
