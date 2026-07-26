"""Generated from Smithy shape ``com.amazonaws.route53resolver#DeleteFirewallRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.firewall_rule


class DeleteFirewallRuleResponse(TypedDict, closed=True):
    firewall_rule: NotRequired["capo_route53resolver.types.firewall_rule.FirewallRule"]
    """<p>The specification for the firewall rule that you just deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFirewallRuleResponse) -> dict:
    out: dict = {}
    if "firewall_rule" in value:
        import capo_route53resolver.types.firewall_rule

        out["FirewallRule"] = (
            capo_route53resolver.types.firewall_rule.serialize_aws_json_1_1(
                value["firewall_rule"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFirewallRuleResponse:
    out: DeleteFirewallRuleResponse = {}  # type: ignore[typeddict-item]
    if "FirewallRule" in data:
        import capo_route53resolver.types.firewall_rule

        out["firewall_rule"] = (
            capo_route53resolver.types.firewall_rule.deserialize_aws_json_1_1(
                data["FirewallRule"]
            )
        )
    return out
