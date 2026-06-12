"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#CreateFirewallRuleInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.block_override_dns_query_type
    import aws_sdk_route53globalresolver.types.block_override_ttl
    import aws_sdk_route53globalresolver.types.client_token
    import aws_sdk_route53globalresolver.types.confidence_threshold
    import aws_sdk_route53globalresolver.types.dns_advanced_protection
    import aws_sdk_route53globalresolver.types.dns_query_type
    import aws_sdk_route53globalresolver.types.domain
    import aws_sdk_route53globalresolver.types.firewall_block_response
    import aws_sdk_route53globalresolver.types.firewall_rule_action
    import aws_sdk_route53globalresolver.types.firewall_rule_priority
    import aws_sdk_route53globalresolver.types.resource_description
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name


class CreateFirewallRuleInput(TypedDict):
    action: (
        "aws_sdk_route53globalresolver.types.firewall_rule_action.FirewallRuleAction"
    )
    """<p>The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list:</p> <ul> <li> <p> <code>ALLOW</code> - Permit the request to go through.</p> </li> <li> <p> <code>ALERT</code> - Permit the request and send metrics and logs to CloudWatch.</p> </li> <li> <p> <code>BLOCK</code> - Disallow the request. This option requires additional details in the rule's <code>BlockResponse</code>.</p> </li> </ul>"""
    block_override_dns_type: NotRequired[
        "aws_sdk_route53globalresolver.types.block_override_dns_query_type.BlockOverrideDnsQueryType"
    ]
    """<p>The DNS record's type. This determines the format of the record value that you provided in <code>BlockOverrideDomain</code>. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>"""
    block_override_domain: NotRequired[
        "aws_sdk_route53globalresolver.types.domain.Domain"
    ]
    """<p>The custom DNS record to send back in response to the query. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>"""
    block_override_ttl: NotRequired[
        "aws_sdk_route53globalresolver.types.block_override_ttl.BlockOverrideTtl"
    ]
    """<p>The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>"""
    block_response: NotRequired[
        "aws_sdk_route53globalresolver.types.firewall_block_response.FirewallBlockResponse"
    ]
    """<p>The response to return when the action is BLOCK. Valid values are NXDOMAIN (domain does not exist), NODATA (domain exists but no records), or OVERRIDE (return custom response).</p>"""
    client_token: NotRequired[
        "aws_sdk_route53globalresolver.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>"""
    confidence_threshold: NotRequired[
        "aws_sdk_route53globalresolver.types.confidence_threshold.ConfidenceThreshold"
    ]
    """<p>The confidence threshold for advanced threat detection. Valid values are HIGH, MEDIUM, or LOW, indicating the accuracy level required for threat detection.</p>"""
    description: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>An optional description for the firewall rule.</p>"""
    dns_advanced_protection: NotRequired[
        "aws_sdk_route53globalresolver.types.dns_advanced_protection.DnsAdvancedProtection"
    ]
    """<p>Whether to enable advanced DNS threat protection for this rule. Advanced protection can detect and block DNS tunneling and Domain Generation Algorithm (DGA) threats.</p>"""
    firewall_domain_list_id: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    ]
    """<p>The ID of the firewall domain list to use in this rule.</p>"""
    name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
    """<p>A descriptive name for the firewall rule.</p>"""
    priority: NotRequired[
        "aws_sdk_route53globalresolver.types.firewall_rule_priority.FirewallRulePriority"
    ]
    """<p>The priority of this rule. Rules are evaluated in priority order, with lower numbers having higher priority. When a DNS query matches multiple rules, the rule with the highest priority (lowest number) is applied.</p>"""
    dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the DNS view to associate with this firewall rule.</p>"""
    q_type: NotRequired[
        "aws_sdk_route53globalresolver.types.dns_query_type.DnsQueryType"
    ]
    """<p>The DNS query type to match for this rule. Examples include A (IPv4 address), AAAA (IPv6 address), MX (mail exchange), or TXT (text record).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFirewallRuleInput) -> dict:
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
    if "client_token" in value:
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
    if "firewall_domain_list_id" in value:
        out["firewallDomainListId"] = value["firewall_domain_list_id"]
    out["name"] = value["name"]
    if "priority" in value:
        out["priority"] = value["priority"]
    out["dnsViewId"] = value["dns_view_id"]
    if "q_type" in value:
        out["qType"] = value["q_type"]
    return out


def deserialize_json(data: dict) -> CreateFirewallRuleInput:
    out: CreateFirewallRuleInput = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import aws_sdk_route53globalresolver.types.firewall_rule_action

        out["action"] = (
            aws_sdk_route53globalresolver.types.firewall_rule_action.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("CreateFirewallRuleInput.action required")
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
    if "firewallDomainListId" in data:
        out["firewall_domain_list_id"] = data["firewallDomainListId"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateFirewallRuleInput.name required")
    if "priority" in data:
        out["priority"] = data["priority"]
    if "dnsViewId" in data:
        out["dns_view_id"] = data["dnsViewId"]
    else:
        raise DeserializationError("CreateFirewallRuleInput.dns_view_id required")
    if "qType" in data:
        out["q_type"] = data["qType"]
    return out
