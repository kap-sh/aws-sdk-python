"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecurityGroupRulesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_rule_list
    import aws_sdk_ec2.types.string


class DescribeSecurityGroupRulesResult(TypedDict):
    security_group_rules: NotRequired[
        "aws_sdk_ec2.types.security_group_rule_list.SecurityGroupRuleList"
    ]
    """<p>Information about security group rules.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSecurityGroupRulesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "security_group_rules" in value:
        import aws_sdk_ec2.types.security_group_rule_list

        aws_sdk_ec2.types.security_group_rule_list.serialize_ec2_query(
            value["security_group_rules"], pairs, f"{prefix}.SecurityGroupRuleSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeSecurityGroupRulesResult:
    out: DescribeSecurityGroupRulesResult = {}  # type: ignore[typeddict-item]
    if el.find("SecurityGroupRuleSet") is not None:
        import aws_sdk_ec2.types.security_group_rule_list

        out["security_group_rules"] = (
            aws_sdk_ec2.types.security_group_rule_list.deserialize_ec2_query(
                el, "SecurityGroupRuleSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
