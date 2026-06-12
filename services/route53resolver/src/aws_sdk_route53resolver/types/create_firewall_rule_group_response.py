"""Generated from Smithy shape ``com.amazonaws.route53resolver#CreateFirewallRuleGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.firewall_rule_group


class CreateFirewallRuleGroupResponse(TypedDict):
    firewall_rule_group: NotRequired[
        "aws_sdk_route53resolver.types.firewall_rule_group.FirewallRuleGroup"
    ]
    """<p>A collection of rules used to filter DNS network traffic. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFirewallRuleGroupResponse) -> dict:
    out: dict = {}
    if "firewall_rule_group" in value:
        import aws_sdk_route53resolver.types.firewall_rule_group

        out["FirewallRuleGroup"] = (
            aws_sdk_route53resolver.types.firewall_rule_group.serialize_aws_json_1_1(
                value["firewall_rule_group"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFirewallRuleGroupResponse:
    out: CreateFirewallRuleGroupResponse = {}  # type: ignore[typeddict-item]
    if "FirewallRuleGroup" in data:
        import aws_sdk_route53resolver.types.firewall_rule_group

        out["firewall_rule_group"] = (
            aws_sdk_route53resolver.types.firewall_rule_group.deserialize_aws_json_1_1(
                data["FirewallRuleGroup"]
            )
        )
    return out
