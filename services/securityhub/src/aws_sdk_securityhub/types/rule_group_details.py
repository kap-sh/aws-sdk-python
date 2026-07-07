"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.rule_group_source
    import aws_sdk_securityhub.types.rule_group_variables


class RuleGroupDetails(TypedDict, closed=True):
    rule_variables: NotRequired[
        "aws_sdk_securityhub.types.rule_group_variables.RuleGroupVariables"
    ]
    """<p>Additional settings to use in the specified rules.</p>"""
    rules_source: NotRequired[
        "aws_sdk_securityhub.types.rule_group_source.RuleGroupSource"
    ]
    """<p>The rules and actions for the rule group.</p> <p>For stateful rule groups, can contain <code>RulesString</code>, <code>RulesSourceList</code>, or <code>StatefulRules</code>.</p> <p>For stateless rule groups, contains <code>StatelessRulesAndCustomActions</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupDetails) -> dict:
    out: dict = {}
    if "rule_variables" in value:
        import aws_sdk_securityhub.types.rule_group_variables

        out["RuleVariables"] = (
            aws_sdk_securityhub.types.rule_group_variables.serialize_json(
                value["rule_variables"]
            )
        )
    if "rules_source" in value:
        import aws_sdk_securityhub.types.rule_group_source

        out["RulesSource"] = aws_sdk_securityhub.types.rule_group_source.serialize_json(
            value["rules_source"]
        )
    return out


def deserialize_json(data: dict) -> RuleGroupDetails:
    out: RuleGroupDetails = {}  # type: ignore[typeddict-item]
    if "RuleVariables" in data:
        import aws_sdk_securityhub.types.rule_group_variables

        out["rule_variables"] = (
            aws_sdk_securityhub.types.rule_group_variables.deserialize_json(
                data["RuleVariables"]
            )
        )
    if "RulesSource" in data:
        import aws_sdk_securityhub.types.rule_group_source

        out["rules_source"] = (
            aws_sdk_securityhub.types.rule_group_source.deserialize_json(
                data["RulesSource"]
            )
        )
    return out
