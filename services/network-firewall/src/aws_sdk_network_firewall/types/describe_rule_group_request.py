"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeRuleGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.boolean
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_name
    import aws_sdk_network_firewall.types.rule_group_type


class DescribeRuleGroupRequest(TypedDict):
    rule_group_name: NotRequired[
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the rule group. You can't change the name of a rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    rule_group_arn: NotRequired[
        "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    type: NotRequired["aws_sdk_network_firewall.types.rule_group_type.RuleGroupType"]
    """<p>Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules. </p> <note> <p>This setting is required for requests that do not include the <code>RuleGroupARN</code>.</p> </note>"""
    analyze_rule_group: "aws_sdk_network_firewall.types.boolean.Boolean"
    """<p>Indicates whether you want Network Firewall to analyze the stateless rules in the rule group for rule behavior such as asymmetric routing. If set to <code>TRUE</code>, Network Firewall runs the analysis.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRuleGroupRequest) -> dict:
    out: dict = {}
    if "rule_group_name" in value:
        out["RuleGroupName"] = value["rule_group_name"]
    if "rule_group_arn" in value:
        out["RuleGroupArn"] = value["rule_group_arn"]
    if "type" in value:
        import aws_sdk_network_firewall.types.rule_group_type

        out["Type"] = (
            aws_sdk_network_firewall.types.rule_group_type.serialize_aws_json_1_0(
                value["type"]
            )
        )
    out["AnalyzeRuleGroup"] = value.get("analyze_rule_group", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRuleGroupRequest:
    out: DescribeRuleGroupRequest = {}  # type: ignore[typeddict-item]
    if "RuleGroupName" in data:
        out["rule_group_name"] = data["RuleGroupName"]
    if "RuleGroupArn" in data:
        out["rule_group_arn"] = data["RuleGroupArn"]
    if "Type" in data:
        import aws_sdk_network_firewall.types.rule_group_type

        out["type"] = (
            aws_sdk_network_firewall.types.rule_group_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    if "AnalyzeRuleGroup" in data:
        out["analyze_rule_group"] = data["AnalyzeRuleGroup"]
    else:
        out["analyze_rule_group"] = False
    return out
