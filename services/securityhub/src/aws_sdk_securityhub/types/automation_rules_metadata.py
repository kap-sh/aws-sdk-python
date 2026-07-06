"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.rule_order_value
    import aws_sdk_securityhub.types.rule_status
    import aws_sdk_securityhub.types.timestamp


class AutomationRulesMetadata(TypedDict, closed=True):
    rule_arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) for the rule. </p>"""
    rule_status: NotRequired["aws_sdk_securityhub.types.rule_status.RuleStatus"]
    r"""<p> Whether the rule is active after it is created. If this parameter is equal to <code>ENABLED</code>, Security Hub CSPM starts applying the rule to findings and finding updates after the rule is created. To change the value of this parameter after creating a rule, use <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateAutomationRules.html\"> <code>BatchUpdateAutomationRules</code> </a>. </p>"""
    rule_order: NotRequired["aws_sdk_securityhub.types.rule_order_value.RuleOrderValue"]
    """<p>An integer ranging from 1 to 1000 that represents the order in which the rule action is applied to findings. Security Hub CSPM applies rules with lower values for this parameter first. </p>"""
    rule_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the rule. </p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> A description of the rule. </p>"""
    is_terminal: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Specifies whether a rule is the last to be applied with respect to a finding that matches the rule criteria. This is useful when a finding matches the criteria for multiple rules, and each rule has different actions. If a rule is terminal, Security Hub CSPM applies the rule action to a finding that matches the rule criteria and doesn't evaluate other rules for the finding. By default, a rule isn't terminal. </p>"""
    created_at: NotRequired["aws_sdk_securityhub.types.timestamp.Timestamp"]
    r"""<p> A timestamp that indicates when the rule was created. </p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    updated_at: NotRequired["aws_sdk_securityhub.types.timestamp.Timestamp"]
    r"""<p> A timestamp that indicates when the rule was most recently updated. </p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    created_by: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The principal that created a rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesMetadata) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["RuleArn"] = value["rule_arn"]
    if "rule_status" in value:
        import aws_sdk_securityhub.types.rule_status

        out["RuleStatus"] = aws_sdk_securityhub.types.rule_status.serialize_json(
            value["rule_status"]
        )
    if "rule_order" in value:
        out["RuleOrder"] = value["rule_order"]
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "is_terminal" in value:
        out["IsTerminal"] = value["is_terminal"]
    if "created_at" in value:
        import aws_sdk_securityhub.types.timestamp

        out["CreatedAt"] = aws_sdk_securityhub.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_securityhub.types.timestamp

        out["UpdatedAt"] = aws_sdk_securityhub.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    return out


def deserialize_json(data: dict) -> AutomationRulesMetadata:
    out: AutomationRulesMetadata = {}  # type: ignore[typeddict-item]
    if "RuleArn" in data:
        out["rule_arn"] = data["RuleArn"]
    if "RuleStatus" in data:
        import aws_sdk_securityhub.types.rule_status

        out["rule_status"] = aws_sdk_securityhub.types.rule_status.deserialize_json(
            data["RuleStatus"]
        )
    if "RuleOrder" in data:
        out["rule_order"] = data["RuleOrder"]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "IsTerminal" in data:
        out["is_terminal"] = data["IsTerminal"]
    if "CreatedAt" in data:
        import aws_sdk_securityhub.types.timestamp

        out["created_at"] = aws_sdk_securityhub.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import aws_sdk_securityhub.types.timestamp

        out["updated_at"] = aws_sdk_securityhub.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    return out
