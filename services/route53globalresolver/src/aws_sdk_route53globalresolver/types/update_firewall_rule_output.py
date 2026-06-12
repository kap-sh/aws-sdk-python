"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UpdateFirewallRuleOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.block_override_dns_query_type
    import aws_sdk_route53globalresolver.types.block_override_ttl
    import aws_sdk_route53globalresolver.types.confidence_threshold
    import aws_sdk_route53globalresolver.types.cr_resource_status
    import aws_sdk_route53globalresolver.types.dns_advanced_protection
    import aws_sdk_route53globalresolver.types.dns_query_type
    import aws_sdk_route53globalresolver.types.domain
    import aws_sdk_route53globalresolver.types.firewall_block_response
    import aws_sdk_route53globalresolver.types.firewall_rule_action
    import aws_sdk_route53globalresolver.types.firewall_rule_priority
    import aws_sdk_route53globalresolver.types.iso8601_time_string
    import aws_sdk_route53globalresolver.types.resource_description
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name


class UpdateFirewallRuleOutput(TypedDict):
    action: (
        "aws_sdk_route53globalresolver.types.firewall_rule_action.FirewallRuleAction"
    )
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
    confidence_threshold: NotRequired[
        "aws_sdk_route53globalresolver.types.confidence_threshold.ConfidenceThreshold"
    ]
    """<p>The confidence threshold for DNS Firewall Advanced. You must provide this value when you create a DNS Firewall Advanced rule.</p>"""
    created_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The time and date the Firewall rule was created.</p>"""
    description: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the Firewall rule.</p>"""
    dns_advanced_protection: NotRequired[
        "aws_sdk_route53globalresolver.types.dns_advanced_protection.DnsAdvancedProtection"
    ]
    """<p>The type of the DNS Firewall Advanced rule. Valid values are DGA, DNS_TUNNELING, and DICTIONARY_DGA.</p>"""
    firewall_domain_list_id: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    ]
    """<p>The ID of the domain list associated with the Firewall rule.</p>"""
    id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the Firewall rule.</p>"""
    name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
    """<p>The name of the Firewall rule.</p>"""
    priority: "aws_sdk_route53globalresolver.types.firewall_rule_priority.FirewallRulePriority"
    """<p>The setting that determines the processing order of the rule in the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.</p>"""
    dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the DNS view the Firewall rule is associated with.</p>"""
    query_type: NotRequired[
        "aws_sdk_route53globalresolver.types.dns_query_type.DnsQueryType"
    ]
    """<p>The DNS query type you want the rule to evaluate.</p>"""
    status: "aws_sdk_route53globalresolver.types.cr_resource_status.CRResourceStatus"
    """<p>The operational status of the firewall rule.</p>"""
    updated_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The time and date the rule was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFirewallRuleOutput) -> dict:
    out: dict = {}
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
    if "confidence_threshold" in value:
        import aws_sdk_route53globalresolver.types.confidence_threshold

        out["confidenceThreshold"] = (
            aws_sdk_route53globalresolver.types.confidence_threshold.serialize_json(
                value["confidence_threshold"]
            )
        )
    import aws_sdk_route53globalresolver.types.iso8601_time_string

    out["createdAt"] = (
        aws_sdk_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["created_at"]
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
    if "firewall_domain_list_id" in value:
        out["firewallDomainListId"] = value["firewall_domain_list_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["priority"] = value["priority"]
    out["dnsViewId"] = value["dns_view_id"]
    if "query_type" in value:
        out["queryType"] = value["query_type"]
    import aws_sdk_route53globalresolver.types.cr_resource_status

    out["status"] = (
        aws_sdk_route53globalresolver.types.cr_resource_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_route53globalresolver.types.iso8601_time_string

    out["updatedAt"] = (
        aws_sdk_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateFirewallRuleOutput:
    out: UpdateFirewallRuleOutput = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import aws_sdk_route53globalresolver.types.firewall_rule_action

        out["action"] = (
            aws_sdk_route53globalresolver.types.firewall_rule_action.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("UpdateFirewallRuleOutput.action required")
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
    if "confidenceThreshold" in data:
        import aws_sdk_route53globalresolver.types.confidence_threshold

        out["confidence_threshold"] = (
            aws_sdk_route53globalresolver.types.confidence_threshold.deserialize_json(
                data["confidenceThreshold"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("UpdateFirewallRuleOutput.created_at required")
    if "description" in data:
        out["description"] = data["description"]
    if "dnsAdvancedProtection" in data:
        import aws_sdk_route53globalresolver.types.dns_advanced_protection

        out["dns_advanced_protection"] = (
            aws_sdk_route53globalresolver.types.dns_advanced_protection.deserialize_json(
                data["dnsAdvancedProtection"]
            )
        )
    if "firewallDomainListId" in data:
        out["firewall_domain_list_id"] = data["firewallDomainListId"]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateFirewallRuleOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateFirewallRuleOutput.name required")
    if "priority" in data:
        out["priority"] = data["priority"]
    else:
        raise DeserializationError("UpdateFirewallRuleOutput.priority required")
    if "dnsViewId" in data:
        out["dns_view_id"] = data["dnsViewId"]
    else:
        raise DeserializationError("UpdateFirewallRuleOutput.dns_view_id required")
    if "queryType" in data:
        out["query_type"] = data["queryType"]
    if "status" in data:
        import aws_sdk_route53globalresolver.types.cr_resource_status

        out["status"] = (
            aws_sdk_route53globalresolver.types.cr_resource_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdateFirewallRuleOutput.status required")
    if "updatedAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("UpdateFirewallRuleOutput.updated_at required")
    return out
