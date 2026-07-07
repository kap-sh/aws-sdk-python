"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsNetworkFirewallRuleGroupDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.rule_group_details


class AwsNetworkFirewallRuleGroupDetails(TypedDict, closed=True):
    capacity: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The maximum number of operating resources that this rule group can use.</p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A description of the rule group.</p>"""
    rule_group: NotRequired[
        "aws_sdk_securityhub.types.rule_group_details.RuleGroupDetails"
    ]
    """<p>Details about the rule group.</p>"""
    rule_group_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the rule group.</p>"""
    rule_group_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the rule group.</p>"""
    rule_group_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The descriptive name of the rule group.</p>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of rule group. A rule group can be stateful or stateless.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsNetworkFirewallRuleGroupDetails) -> dict:
    out: dict = {}
    if "capacity" in value:
        out["Capacity"] = value["capacity"]
    if "description" in value:
        out["Description"] = value["description"]
    if "rule_group" in value:
        import aws_sdk_securityhub.types.rule_group_details

        out["RuleGroup"] = aws_sdk_securityhub.types.rule_group_details.serialize_json(
            value["rule_group"]
        )
    if "rule_group_arn" in value:
        out["RuleGroupArn"] = value["rule_group_arn"]
    if "rule_group_id" in value:
        out["RuleGroupId"] = value["rule_group_id"]
    if "rule_group_name" in value:
        out["RuleGroupName"] = value["rule_group_name"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsNetworkFirewallRuleGroupDetails:
    out: AwsNetworkFirewallRuleGroupDetails = {}  # type: ignore[typeddict-item]
    if "Capacity" in data:
        out["capacity"] = data["Capacity"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "RuleGroup" in data:
        import aws_sdk_securityhub.types.rule_group_details

        out["rule_group"] = (
            aws_sdk_securityhub.types.rule_group_details.deserialize_json(
                data["RuleGroup"]
            )
        )
    if "RuleGroupArn" in data:
        out["rule_group_arn"] = data["RuleGroupArn"]
    if "RuleGroupId" in data:
        out["rule_group_id"] = data["RuleGroupId"]
    if "RuleGroupName" in data:
        out["rule_group_name"] = data["RuleGroupName"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
