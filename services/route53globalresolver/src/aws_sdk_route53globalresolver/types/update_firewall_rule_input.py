"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UpdateFirewallRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.block_override_dns_query_type
    import aws_sdk_route53globalresolver.types.block_override_ttl
    import aws_sdk_route53globalresolver.types.client_token
    import aws_sdk_route53globalresolver.types.confidence_threshold
    import aws_sdk_route53globalresolver.types.dns_advanced_protection
    import aws_sdk_route53globalresolver.types.domain
    import aws_sdk_route53globalresolver.types.firewall_block_response
    import aws_sdk_route53globalresolver.types.firewall_rule_action
    import aws_sdk_route53globalresolver.types.firewall_rule_priority
    import aws_sdk_route53globalresolver.types.resource_description
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name


class UpdateFirewallRuleInput(TypedDict, closed=True):
    action: NotRequired[
        "aws_sdk_route53globalresolver.types.firewall_rule_action.FirewallRuleAction"
    ]
    """<p>The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list, or a threat in a DNS Firewall Advanced rule.</p>"""
    block_override_dns_type: NotRequired[
        "aws_sdk_route53globalresolver.types.block_override_dns_query_type.BlockOverrideDnsQueryType"
    ]
    """<p>The DNS record's type. This determines the format of the record value that you provided in <code>BlockOverrideDomain</code>. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>"""
    block_override_domain: NotRequired[
        "aws_sdk_route53globalresolver.types.domain.Domain"
    ]
    """<p>The custom DNS record to send back in response to the query. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>"""
    block_override_ttl: NotRequired[
        "aws_sdk_route53globalresolver.types.block_override_ttl.BlockOverrideTtl"
    ]
    """<p>The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>"""
    block_response: NotRequired[
        "aws_sdk_route53globalresolver.types.firewall_block_response.FirewallBlockResponse"
    ]
    """<p>The way that you want DNS Firewall to block the request. Used for the rule action setting <code>BLOCK</code>.</p>"""
    client_token: "aws_sdk_route53globalresolver.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>"""
    confidence_threshold: NotRequired[
        "aws_sdk_route53globalresolver.types.confidence_threshold.ConfidenceThreshold"
    ]
    """<p>The confidence threshold for DNS Firewall Advanced. You must provide this value when you create a DNS Firewall Advanced rule.</p>"""
    description: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>The description for the Firewall rule.</p>"""
    dns_advanced_protection: NotRequired[
        "aws_sdk_route53globalresolver.types.dns_advanced_protection.DnsAdvancedProtection"
    ]
    """<p>The type of the DNS Firewall Advanced rule. Valid values are DGA, DNS_TUNNELING, and DICTIONARY_DGA.</p>"""
    firewall_rule_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the DNS Firewall rule.</p>"""
    name: NotRequired["aws_sdk_route53globalresolver.types.resource_name.ResourceName"]
    """<p>The name of the DNS Firewall rule.</p>"""
    priority: NotRequired[
        "aws_sdk_route53globalresolver.types.firewall_rule_priority.FirewallRulePriority"
    ]
    """<p>The setting that determines the processing order of the rule in the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFirewallRuleInput) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_route53globalresolver.types.firewall_rule_action

        out["action"] = (
            aws_sdk_route53globalresolver.types.firewall_rule_action.serialize_json(
                value["action"]
            )
        )
    if "block_override_dns_type" in value:
        import aws_sdk_route53globalresolver.types.block_override_dns_query_type

        out["blockOverrideDnsType"] = (
            aws_sdk_route53globalresolver.types.block_override_dns_query_type.serialize_json(
                value["block_override_dns_type"]
            )
        )
    if "block_override_domain" in value:
        out["blockOverrideDomain"] = value["block_override_domain"]
    if "block_override_ttl" in value:
        out["blockOverrideTtl"] = value["block_override_ttl"]
    if "block_response" in value:
        import aws_sdk_route53globalresolver.types.firewall_block_response

        out["blockResponse"] = (
            aws_sdk_route53globalresolver.types.firewall_block_response.serialize_json(
                value["block_response"]
            )
        )
    out["clientToken"] = value["client_token"]
    if "confidence_threshold" in value:
        import aws_sdk_route53globalresolver.types.confidence_threshold

        out["confidenceThreshold"] = (
            aws_sdk_route53globalresolver.types.confidence_threshold.serialize_json(
                value["confidence_threshold"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "dns_advanced_protection" in value:
        import aws_sdk_route53globalresolver.types.dns_advanced_protection

        out["dnsAdvancedProtection"] = (
            aws_sdk_route53globalresolver.types.dns_advanced_protection.serialize_json(
                value["dns_advanced_protection"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "priority" in value:
        out["priority"] = value["priority"]
    return out


def deserialize_json(data: dict) -> UpdateFirewallRuleInput:
    out: UpdateFirewallRuleInput = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import aws_sdk_route53globalresolver.types.firewall_rule_action

        out["action"] = (
            aws_sdk_route53globalresolver.types.firewall_rule_action.deserialize_json(
                data["action"]
            )
        )
    if "blockOverrideDnsType" in data:
        import aws_sdk_route53globalresolver.types.block_override_dns_query_type

        out["block_override_dns_type"] = (
            aws_sdk_route53globalresolver.types.block_override_dns_query_type.deserialize_json(
                data["blockOverrideDnsType"]
            )
        )
    if "blockOverrideDomain" in data:
        out["block_override_domain"] = data["blockOverrideDomain"]
    if "blockOverrideTtl" in data:
        out["block_override_ttl"] = data["blockOverrideTtl"]
    if "blockResponse" in data:
        import aws_sdk_route53globalresolver.types.firewall_block_response

        out["block_response"] = (
            aws_sdk_route53globalresolver.types.firewall_block_response.deserialize_json(
                data["blockResponse"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("UpdateFirewallRuleInput.client_token required")
    if "confidenceThreshold" in data:
        import aws_sdk_route53globalresolver.types.confidence_threshold

        out["confidence_threshold"] = (
            aws_sdk_route53globalresolver.types.confidence_threshold.deserialize_json(
                data["confidenceThreshold"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "dnsAdvancedProtection" in data:
        import aws_sdk_route53globalresolver.types.dns_advanced_protection

        out["dns_advanced_protection"] = (
            aws_sdk_route53globalresolver.types.dns_advanced_protection.deserialize_json(
                data["dnsAdvancedProtection"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "priority" in data:
        out["priority"] = data["priority"]
    return out
