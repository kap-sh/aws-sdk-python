"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DeleteFirewallRuleOutput``."""

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


class DeleteFirewallRuleOutput(TypedDict):
    action: (
        "aws_sdk_route53globalresolver.types.firewall_rule_action.FirewallRuleAction"
    )
    """<p>The action that was configured for the deleted firewall rule.</p>"""
    block_override_dns_type: NotRequired[
        "aws_sdk_route53globalresolver.types.block_override_dns_query_type.BlockOverrideDnsQueryType"
    ]
    """<p>The DNS record type that was configured for the deleted firewall rule's custom response.</p>"""
    block_override_domain: NotRequired[
        "aws_sdk_route53globalresolver.types.domain.Domain"
    ]
    """<p>The custom domain that was configured for the deleted firewall rule's BLOCK response.</p>"""
    block_override_ttl: NotRequired[
        "aws_sdk_route53globalresolver.types.block_override_ttl.BlockOverrideTtl"
    ]
    """<p>The TTL value that was configured for the deleted firewall rule's custom response.</p>"""
    block_response: NotRequired[
        "aws_sdk_route53globalresolver.types.firewall_block_response.FirewallBlockResponse"
    ]
    """<p>The block response type that was configured for the deleted firewall rule.</p>"""
    confidence_threshold: NotRequired[
        "aws_sdk_route53globalresolver.types.confidence_threshold.ConfidenceThreshold"
    ]
    """<p>The confidence threshold that was configured for the deleted firewall rule's advanced threat detection.</p>"""
    created_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time when the firewall rule was originally created.</p>"""
    description: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the deleted firewall rule.</p>"""
    dns_advanced_protection: NotRequired[
        "aws_sdk_route53globalresolver.types.dns_advanced_protection.DnsAdvancedProtection"
    ]
    """<p>Whether advanced DNS threat protection was enabled for the deleted firewall rule.</p>"""
    firewall_domain_list_id: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    ]
    """<p>The ID of the firewall domain list that was associated with the deleted firewall rule.</p>"""
    id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the deleted firewall rule.</p>"""
    name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
    """<p>The name of the deleted firewall rule.</p>"""
    priority: "aws_sdk_route53globalresolver.types.firewall_rule_priority.FirewallRulePriority"
    """<p>The priority that was configured for the deleted firewall rule.</p>"""
    dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the DNS view that was associated with the deleted firewall rule.</p>"""
    query_type: NotRequired[
        "aws_sdk_route53globalresolver.types.dns_query_type.DnsQueryType"
    ]
    """<p>The DNS query type that the deleted firewall rule was configured to match.</p>"""
    status: "aws_sdk_route53globalresolver.types.cr_resource_status.CRResourceStatus"
    """<p>The final status of the deleted firewall rule.</p>"""
    updated_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time when the firewall rule was last updated before deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFirewallRuleOutput) -> dict:
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


def deserialize_json(data: dict) -> DeleteFirewallRuleOutput:
    out: DeleteFirewallRuleOutput = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import aws_sdk_route53globalresolver.types.firewall_rule_action

        out["action"] = (
            aws_sdk_route53globalresolver.types.firewall_rule_action.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("DeleteFirewallRuleOutput.action required")
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
        raise DeserializationError("DeleteFirewallRuleOutput.created_at required")
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
        raise DeserializationError("DeleteFirewallRuleOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteFirewallRuleOutput.name required")
    if "priority" in data:
        out["priority"] = data["priority"]
    else:
        raise DeserializationError("DeleteFirewallRuleOutput.priority required")
    if "dnsViewId" in data:
        out["dns_view_id"] = data["dnsViewId"]
    else:
        raise DeserializationError("DeleteFirewallRuleOutput.dns_view_id required")
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
        raise DeserializationError("DeleteFirewallRuleOutput.status required")
    if "updatedAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("DeleteFirewallRuleOutput.updated_at required")
    return out
