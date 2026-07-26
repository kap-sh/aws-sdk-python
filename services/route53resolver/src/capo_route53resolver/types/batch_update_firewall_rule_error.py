"""Generated from Smithy shape ``com.amazonaws.route53resolver#BatchUpdateFirewallRuleError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.string
    import capo_route53resolver.types.update_firewall_rule_entry


class BatchUpdateFirewallRuleError(TypedDict, closed=True):
    firewall_rule: NotRequired[
        "capo_route53resolver.types.update_firewall_rule_entry.UpdateFirewallRuleEntry"
    ]
    """<p>The firewall rule entry that caused the error.</p>"""
    code: NotRequired["capo_route53resolver.types.string.String"]
    """<p>The error code for the failure.</p>"""
    message: NotRequired["capo_route53resolver.types.string.String"]
    """<p>A message that provides details about the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchUpdateFirewallRuleError) -> dict:
    out: dict = {}
    if "firewall_rule" in value:
        import capo_route53resolver.types.update_firewall_rule_entry

        out["FirewallRule"] = (
            capo_route53resolver.types.update_firewall_rule_entry.serialize_aws_json_1_1(
                value["firewall_rule"]
            )
        )
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchUpdateFirewallRuleError:
    out: BatchUpdateFirewallRuleError = {}  # type: ignore[typeddict-item]
    if "FirewallRule" in data:
        import capo_route53resolver.types.update_firewall_rule_entry

        out["firewall_rule"] = (
            capo_route53resolver.types.update_firewall_rule_entry.deserialize_aws_json_1_1(
                data["FirewallRule"]
            )
        )
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
