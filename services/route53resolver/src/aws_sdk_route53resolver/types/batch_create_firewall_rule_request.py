"""Generated from Smithy shape ``com.amazonaws.route53resolver#BatchCreateFirewallRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.create_firewall_rule_entries


class BatchCreateFirewallRuleRequest(TypedDict):
    create_firewall_rule_entries: "aws_sdk_route53resolver.types.create_firewall_rule_entries.CreateFirewallRuleEntries"
    """<p>The list of firewall rules to create.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchCreateFirewallRuleRequest) -> dict:
    out: dict = {}
    import aws_sdk_route53resolver.types.create_firewall_rule_entries

    out["CreateFirewallRuleEntries"] = (
        aws_sdk_route53resolver.types.create_firewall_rule_entries.serialize_aws_json_1_1(
            value["create_firewall_rule_entries"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchCreateFirewallRuleRequest:
    out: BatchCreateFirewallRuleRequest = {}  # type: ignore[typeddict-item]
    if "CreateFirewallRuleEntries" in data:
        import aws_sdk_route53resolver.types.create_firewall_rule_entries

        out["create_firewall_rule_entries"] = (
            aws_sdk_route53resolver.types.create_firewall_rule_entries.deserialize_aws_json_1_1(
                data["CreateFirewallRuleEntries"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateFirewallRuleRequest.create_firewall_rule_entries required"
        )
    return out
