"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BatchCreateFirewallRuleResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53globalresolver.types.block_override_dns_query_type
    import capo_route53globalresolver.types.block_override_ttl
    import capo_route53globalresolver.types.client_token
    import capo_route53globalresolver.types.confidence_threshold
    import capo_route53globalresolver.types.cr_resource_status
    import capo_route53globalresolver.types.dns_advanced_protection
    import capo_route53globalresolver.types.dns_query_type
    import capo_route53globalresolver.types.domain
    import capo_route53globalresolver.types.firewall_block_response
    import capo_route53globalresolver.types.firewall_rule_action
    import capo_route53globalresolver.types.firewall_rule_priority
    import capo_route53globalresolver.types.iso8601_time_string
    import capo_route53globalresolver.types.resource_description
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name


class BatchCreateFirewallRuleResult(TypedDict, closed=True):
    action: "capo_route53globalresolver.types.firewall_rule_action.FirewallRuleAction"
    """<p>The action configured for the created firewall rule.</p>"""
    block_override_dns_type: NotRequired[
        "capo_route53globalresolver.types.block_override_dns_query_type.BlockOverrideDnsQueryType"
    ]
    """<p>The DNS record type configured for the created firewall rule's custom response.</p>"""
    block_override_domain: NotRequired["capo_route53globalresolver.types.domain.Domain"]
    """<p>The custom domain name configured for the created firewall rule's BLOCK response.</p>"""
    block_override_ttl: NotRequired[
        "capo_route53globalresolver.types.block_override_ttl.BlockOverrideTtl"
    ]
    """<p>The TTL value configured for the created firewall rule's custom response.</p>"""
    block_response: NotRequired[
        "capo_route53globalresolver.types.firewall_block_response.FirewallBlockResponse"
    ]
    """<p>The type of block response configured for the created firewall rule.</p>"""
    client_token: "capo_route53globalresolver.types.client_token.ClientToken"
    """<p>The unique string that identified the request and ensured idempotency.</p>"""
    confidence_threshold: NotRequired[
        "capo_route53globalresolver.types.confidence_threshold.ConfidenceThreshold"
    ]
    """<p>The confidence threshold configured for the created firewall rule's advanced threat detection.</p>"""
    created_at: NotRequired[
        "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    ]
    """<p>The date and time when the firewall rule was created.</p>"""
    description: NotRequired[
        "capo_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the created firewall rule.</p>"""
    dns_advanced_protection: NotRequired[
        "capo_route53globalresolver.types.dns_advanced_protection.DnsAdvancedProtection"
    ]
    """<p>Whether advanced DNS threat protection is enabled for the created firewall rule.</p>"""
    firewall_domain_list_id: NotRequired[
        "capo_route53globalresolver.types.resource_id.ResourceId"
    ]
    """<p>The ID of the firewall domain list associated with the created firewall rule.</p>"""
    id: NotRequired["capo_route53globalresolver.types.resource_id.ResourceId"]
    """<p>The unique identifier of the created firewall rule.</p>"""
    managed_domain_list_name: NotRequired[
        "capo_route53globalresolver.types.resource_name.ResourceName"
    ]
    """<p>The name of the managed domain list associated with the created firewall rule.</p>"""
    name: "capo_route53globalresolver.types.resource_name.ResourceName"
    """<p>The name of the created firewall rule.</p>"""
    priority: NotRequired[
        "capo_route53globalresolver.types.firewall_rule_priority.FirewallRulePriority"
    ]
    """<p>The priority of the created firewall rule.</p>"""
    dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the DNS view associated with the created firewall rule.</p>"""
    query_type: NotRequired[
        "capo_route53globalresolver.types.dns_query_type.DnsQueryType"
    ]
    """<p>The DNS query type that the created firewall rule matches.</p>"""
    status: NotRequired[
        "capo_route53globalresolver.types.cr_resource_status.CRResourceStatus"
    ]
    """<p>The current status of the created firewall rule.</p>"""
    updated_at: NotRequired[
        "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    ]
    """<p>The date and time when the firewall rule was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateFirewallRuleResult) -> dict:
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
    if "created_at" in value:
        import capo_route53globalresolver.types.iso8601_time_string

        out["createdAt"] = (
            capo_route53globalresolver.types.iso8601_time_string.serialize_json(
                value["created_at"]
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
    if "id" in value:
        out["id"] = value["id"]
    if "managed_domain_list_name" in value:
        out["managedDomainListName"] = value["managed_domain_list_name"]
    out["name"] = value["name"]
    if "priority" in value:
        out["priority"] = value["priority"]
    out["dnsViewId"] = value["dns_view_id"]
    if "query_type" in value:
        out["queryType"] = value["query_type"]
    if "status" in value:
        import capo_route53globalresolver.types.cr_resource_status

        out["status"] = (
            capo_route53globalresolver.types.cr_resource_status.serialize_json(
                value["status"]
            )
        )
    if "updated_at" in value:
        import capo_route53globalresolver.types.iso8601_time_string

        out["updatedAt"] = (
            capo_route53globalresolver.types.iso8601_time_string.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchCreateFirewallRuleResult:
    out: BatchCreateFirewallRuleResult = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import capo_route53globalresolver.types.firewall_rule_action

        out["action"] = (
            capo_route53globalresolver.types.firewall_rule_action.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("BatchCreateFirewallRuleResult.action required")
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
            "BatchCreateFirewallRuleResult.client_token required"
        )
    if "confidenceThreshold" in data:
        import capo_route53globalresolver.types.confidence_threshold

        out["confidence_threshold"] = (
            capo_route53globalresolver.types.confidence_threshold.deserialize_json(
                data["confidenceThreshold"]
            )
        )
    if "createdAt" in data:
        import capo_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
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
    if "id" in data:
        out["id"] = data["id"]
    if "managedDomainListName" in data:
        out["managed_domain_list_name"] = data["managedDomainListName"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("BatchCreateFirewallRuleResult.name required")
    if "priority" in data:
        out["priority"] = data["priority"]
    if "dnsViewId" in data:
        out["dns_view_id"] = data["dnsViewId"]
    else:
        raise DeserializationError("BatchCreateFirewallRuleResult.dns_view_id required")
    if "queryType" in data:
        out["query_type"] = data["queryType"]
    if "status" in data:
        import capo_route53globalresolver.types.cr_resource_status

        out["status"] = (
            capo_route53globalresolver.types.cr_resource_status.deserialize_json(
                data["status"]
            )
        )
    if "updatedAt" in data:
        import capo_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
