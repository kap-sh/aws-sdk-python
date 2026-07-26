"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BatchCreateFirewallRuleInputItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53globalresolver.types.block_override_dns_query_type
    import capo_route53globalresolver.types.block_override_ttl
    import capo_route53globalresolver.types.client_token
    import capo_route53globalresolver.types.confidence_threshold
    import capo_route53globalresolver.types.dns_advanced_protection
    import capo_route53globalresolver.types.dns_query_type
    import capo_route53globalresolver.types.domain
    import capo_route53globalresolver.types.firewall_block_response
    import capo_route53globalresolver.types.firewall_rule_action
    import capo_route53globalresolver.types.firewall_rule_priority
    import capo_route53globalresolver.types.resource_description
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name


class BatchCreateFirewallRuleInputItem(TypedDict, closed=True):
    action: "capo_route53globalresolver.types.firewall_rule_action.FirewallRuleAction"
    """<p>The action to take when a DNS query matches the firewall rule.</p>"""
    block_override_dns_type: NotRequired[
        "capo_route53globalresolver.types.block_override_dns_query_type.BlockOverrideDnsQueryType"
    ]
    """<p>The DNS record type for the custom response when the action is BLOCK.</p>"""
    block_override_domain: NotRequired["capo_route53globalresolver.types.domain.Domain"]
    """<p>The custom domain name for the BLOCK response.</p>"""
    block_override_ttl: NotRequired[
        "capo_route53globalresolver.types.block_override_ttl.BlockOverrideTtl"
    ]
    """<p>The TTL value for the custom response when the action is BLOCK.</p>"""
    block_response: NotRequired[
        "capo_route53globalresolver.types.firewall_block_response.FirewallBlockResponse"
    ]
    """<p>The type of block response to return when the action is BLOCK.</p>"""
    client_token: "capo_route53globalresolver.types.client_token.ClientToken"
    """<p>A unique string that identifies the request and ensures idempotency.</p>"""
    confidence_threshold: NotRequired[
        "capo_route53globalresolver.types.confidence_threshold.ConfidenceThreshold"
    ]
    """<p>The confidence threshold for advanced threat detection.</p>"""
    description: NotRequired[
        "capo_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>A description of the firewall rule.</p>"""
    dns_advanced_protection: NotRequired[
        "capo_route53globalresolver.types.dns_advanced_protection.DnsAdvancedProtection"
    ]
    """<p>Whether to enable advanced DNS threat protection for the firewall rule.</p>"""
    firewall_domain_list_id: NotRequired[
        "capo_route53globalresolver.types.resource_id.ResourceId"
    ]
    """<p>The ID of the firewall domain list to associate with the rule.</p>"""
    name: "capo_route53globalresolver.types.resource_name.ResourceName"
    """<p>A name for the firewall rule.</p>"""
    priority: NotRequired[
        "capo_route53globalresolver.types.firewall_rule_priority.FirewallRulePriority"
    ]
    """<p>The priority of the firewall rule.</p>"""
    dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the DNS view to associate the firewall rule with.</p>"""
    q_type: NotRequired["capo_route53globalresolver.types.dns_query_type.DnsQueryType"]
    """<p>The DNS query type that the firewall rule should match.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateFirewallRuleInputItem) -> dict:
    out: dict = {}
    import capo_route53globalresolver.types.firewall_rule_action

    out["action"] = (
        capo_route53globalresolver.types.firewall_rule_action.serialize_json(
            value["action"]
        )
    )
    if "block_override_dns_type" in value:
        import capo_route53globalresolver.types.block_override_dns_query_type

        out["blockOverrideDnsType"] = (
            capo_route53globalresolver.types.block_override_dns_query_type.serialize_json(
                value["block_override_dns_type"]
            )
        )
    if "block_override_domain" in value:
        out["blockOverrideDomain"] = value["block_override_domain"]
    if "block_override_ttl" in value:
        out["blockOverrideTtl"] = value["block_override_ttl"]
    if "block_response" in value:
        import capo_route53globalresolver.types.firewall_block_response

        out["blockResponse"] = (
            capo_route53globalresolver.types.firewall_block_response.serialize_json(
                value["block_response"]
            )
        )
    out["clientToken"] = value["client_token"]
    if "confidence_threshold" in value:
        import capo_route53globalresolver.types.confidence_threshold

        out["confidenceThreshold"] = (
            capo_route53globalresolver.types.confidence_threshold.serialize_json(
                value["confidence_threshold"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "dns_advanced_protection" in value:
        import capo_route53globalresolver.types.dns_advanced_protection

        out["dnsAdvancedProtection"] = (
            capo_route53globalresolver.types.dns_advanced_protection.serialize_json(
                value["dns_advanced_protection"]
            )
        )
    if "firewall_domain_list_id" in value:
        out["firewallDomainListId"] = value["firewall_domain_list_id"]
    out["name"] = value["name"]
    if "priority" in value:
        out["priority"] = value["priority"]
    out["dnsViewId"] = value["dns_view_id"]
    if "q_type" in value:
        out["qType"] = value["q_type"]
    return out


def deserialize_json(data: dict) -> BatchCreateFirewallRuleInputItem:
    out: BatchCreateFirewallRuleInputItem = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import capo_route53globalresolver.types.firewall_rule_action

        out["action"] = (
            capo_route53globalresolver.types.firewall_rule_action.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("BatchCreateFirewallRuleInputItem.action required")
    if "blockOverrideDnsType" in data:
        import capo_route53globalresolver.types.block_override_dns_query_type

        out["block_override_dns_type"] = (
            capo_route53globalresolver.types.block_override_dns_query_type.deserialize_json(
                data["blockOverrideDnsType"]
            )
        )
    if "blockOverrideDomain" in data:
        out["block_override_domain"] = data["blockOverrideDomain"]
    if "blockOverrideTtl" in data:
        out["block_override_ttl"] = data["blockOverrideTtl"]
    if "blockResponse" in data:
        import capo_route53globalresolver.types.firewall_block_response

        out["block_response"] = (
            capo_route53globalresolver.types.firewall_block_response.deserialize_json(
                data["blockResponse"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "BatchCreateFirewallRuleInputItem.client_token required"
        )
    if "confidenceThreshold" in data:
        import capo_route53globalresolver.types.confidence_threshold

        out["confidence_threshold"] = (
            capo_route53globalresolver.types.confidence_threshold.deserialize_json(
                data["confidenceThreshold"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "dnsAdvancedProtection" in data:
        import capo_route53globalresolver.types.dns_advanced_protection

        out["dns_advanced_protection"] = (
            capo_route53globalresolver.types.dns_advanced_protection.deserialize_json(
                data["dnsAdvancedProtection"]
            )
        )
    if "firewallDomainListId" in data:
        out["firewall_domain_list_id"] = data["firewallDomainListId"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("BatchCreateFirewallRuleInputItem.name required")
    if "priority" in data:
        out["priority"] = data["priority"]
    if "dnsViewId" in data:
        out["dns_view_id"] = data["dnsViewId"]
    else:
        raise DeserializationError(
            "BatchCreateFirewallRuleInputItem.dns_view_id required"
        )
    if "qType" in data:
        out["q_type"] = data["qType"]
    return out
