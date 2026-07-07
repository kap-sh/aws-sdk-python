"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatefulRulesOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.rule_group_source_stateful_rules_rule_options_settings_list


class RuleGroupSourceStatefulRulesOptionsDetails(TypedDict, closed=True):
    keyword: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A keyword to look for.</p>"""
    settings: NotRequired[
        "aws_sdk_securityhub.types.rule_group_source_stateful_rules_rule_options_settings_list.RuleGroupSourceStatefulRulesRuleOptionsSettingsList"
    ]
    """<p>A list of settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupSourceStatefulRulesOptionsDetails) -> dict:
    out: dict = {}
    if "keyword" in value:
        out["Keyword"] = value["keyword"]
    if "settings" in value:
        import aws_sdk_securityhub.types.rule_group_source_stateful_rules_rule_options_settings_list

        out["Settings"] = (
            aws_sdk_securityhub.types.rule_group_source_stateful_rules_rule_options_settings_list.serialize_json(
                value["settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuleGroupSourceStatefulRulesOptionsDetails:
    out: RuleGroupSourceStatefulRulesOptionsDetails = {}  # type: ignore[typeddict-item]
    if "Keyword" in data:
        out["keyword"] = data["Keyword"]
    if "Settings" in data:
        import aws_sdk_securityhub.types.rule_group_source_stateful_rules_rule_options_settings_list

        out["settings"] = (
            aws_sdk_securityhub.types.rule_group_source_stateful_rules_rule_options_settings_list.deserialize_json(
                data["Settings"]
            )
        )
    return out
