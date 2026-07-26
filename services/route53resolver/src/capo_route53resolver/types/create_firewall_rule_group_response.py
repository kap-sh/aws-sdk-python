"""Generated from Smithy shape ``com.amazonaws.route53resolver#CreateFirewallRuleGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.firewall_rule_group


class CreateFirewallRuleGroupResponse(TypedDict, closed=True):
    firewall_rule_group: NotRequired[
        "capo_route53resolver.types.firewall_rule_group.FirewallRuleGroup"
    ]
    """<p>A collection of rules used to filter DNS network traffic. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFirewallRuleGroupResponse) -> dict:
    out: dict = {}
    if "firewall_rule_group" in value:
        import capo_route53resolver.types.firewall_rule_group

        out["FirewallRuleGroup"] = (
            capo_route53resolver.types.firewall_rule_group.serialize_aws_json_1_1(
                value["firewall_rule_group"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFirewallRuleGroupResponse:
    out: CreateFirewallRuleGroupResponse = {}  # type: ignore[typeddict-item]
    if "FirewallRuleGroup" in data:
        import capo_route53resolver.types.firewall_rule_group

        out["firewall_rule_group"] = (
            capo_route53resolver.types.firewall_rule_group.deserialize_aws_json_1_1(
                data["FirewallRuleGroup"]
            )
        )
    return out
