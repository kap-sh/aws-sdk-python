"""Generated from Smithy shape ``com.amazonaws.route53resolver#CreateFirewallRuleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.firewall_rule


class CreateFirewallRuleResponse(TypedDict):
    firewall_rule: NotRequired[
        "aws_sdk_route53resolver.types.firewall_rule.FirewallRule"
    ]
    """<p>The firewall rule that you just created. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFirewallRuleResponse) -> dict:
    out: dict = {}
    if "firewall_rule" in value:
        import aws_sdk_route53resolver.types.firewall_rule

        out["FirewallRule"] = (
            aws_sdk_route53resolver.types.firewall_rule.serialize_aws_json_1_1(
                value["firewall_rule"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFirewallRuleResponse:
    out: CreateFirewallRuleResponse = {}  # type: ignore[typeddict-item]
    if "FirewallRule" in data:
        import aws_sdk_route53resolver.types.firewall_rule

        out["firewall_rule"] = (
            aws_sdk_route53resolver.types.firewall_rule.deserialize_aws_json_1_1(
                data["FirewallRule"]
            )
        )
    return out
