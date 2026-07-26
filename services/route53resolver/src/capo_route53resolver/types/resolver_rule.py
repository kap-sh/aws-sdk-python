"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.account_id
    import capo_route53resolver.types.arn
    import capo_route53resolver.types.creator_request_id
    import capo_route53resolver.types.delegation_record
    import capo_route53resolver.types.domain_name
    import capo_route53resolver.types.name
    import capo_route53resolver.types.resolver_rule_status
    import capo_route53resolver.types.resource_id
    import capo_route53resolver.types.rfc3339_time_string
    import capo_route53resolver.types.rule_type_option
    import capo_route53resolver.types.share_status
    import capo_route53resolver.types.status_message
    import capo_route53resolver.types.target_list


class ResolverRule(TypedDict, closed=True):
    id: NotRequired["capo_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID that Resolver assigned to the Resolver rule when you created it.</p>"""
    creator_request_id: NotRequired[
        "capo_route53resolver.types.creator_request_id.CreatorRequestId"
    ]
    """<p>A unique string that you specified when you created the Resolver rule. <code>CreatorRequestId</code> identifies the request and allows failed requests to be retried without the risk of running the operation twice. </p>"""
    arn: NotRequired["capo_route53resolver.types.arn.Arn"]
    """<p>The ARN (Amazon Resource Name) for the Resolver rule specified by <code>Id</code>.</p>"""
    domain_name: NotRequired["capo_route53resolver.types.domain_name.DomainName"]
    """<p>DNS queries for this domain name are forwarded to the IP addresses that are specified in <code>TargetIps</code>. If a query matches multiple Resolver rules (example.com and www.example.com), the query is routed using the Resolver rule that contains the most specific domain name (www.example.com).</p>"""
    status: NotRequired[
        "capo_route53resolver.types.resolver_rule_status.ResolverRuleStatus"
    ]
    """<p>A code that specifies the current status of the Resolver rule.</p>"""
    status_message: NotRequired[
        "capo_route53resolver.types.status_message.StatusMessage"
    ]
    """<p>A detailed description of the status of a Resolver rule.</p>"""
    rule_type: NotRequired["capo_route53resolver.types.rule_type_option.RuleTypeOption"]
    """<p>When you want to forward DNS queries for specified domain name to resolvers on your network, specify <code>FORWARD</code> or <code>DELEGATE</code>. If a query matches multiple Resolver rules (example.com and www.example.com), outbound DNS queries are routed using the Resolver rule that contains the most specific domain name (www.example.com).</p> <p>When you have a forwarding rule to forward DNS queries for a domain to your network and you want Resolver to process queries for a subdomain of that domain, specify <code>SYSTEM</code>.</p> <p>For example, to forward DNS queries for example.com to resolvers on your network, you create a rule and specify <code>FORWARD</code> for <code>RuleType</code>. To then have Resolver process queries for apex.example.com, you create a rule and specify <code>SYSTEM</code> for <code>RuleType</code>.</p> <p>Currently, only Resolver can create rules that have a value of <code>RECURSIVE</code> for <code>RuleType</code>.</p>"""
    name: NotRequired["capo_route53resolver.types.name.Name"]
    """<p>The name for the Resolver rule, which you specified when you created the Resolver rule.</p> <p>The name can be up to 64 characters long and can contain letters (a-z, A-Z), numbers (0-9), hyphens (-), underscores (_), and spaces. The name cannot consist of only numbers.</p>"""
    target_ips: NotRequired["capo_route53resolver.types.target_list.TargetList"]
    """<p>An array that contains the IP addresses and ports that an outbound endpoint forwards DNS queries to. Typically, these are the IP addresses of DNS resolvers on your network. </p>"""
    resolver_endpoint_id: NotRequired[
        "capo_route53resolver.types.resource_id.ResourceId"
    ]
    """<p>The ID of the endpoint that the rule is associated with.</p>"""
    owner_id: NotRequired["capo_route53resolver.types.account_id.AccountId"]
    """<p>When a rule is shared with another Amazon Web Services account, the account ID of the account that the rule is shared with.</p>"""
    share_status: NotRequired["capo_route53resolver.types.share_status.ShareStatus"]
    """<p>Whether the rule is shared and, if so, whether the current account is sharing the rule with another account, or another account is sharing the rule with the current account.</p>"""
    creation_time: NotRequired[
        "capo_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the Resolver rule was created, in Unix time format and Coordinated Universal Time (UTC).</p>"""
    modification_time: NotRequired[
        "capo_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the Resolver rule was last updated, in Unix time format and Coordinated Universal Time (UTC).</p>"""
    delegation_record: NotRequired[
        "capo_route53resolver.types.delegation_record.DelegationRecord"
    ]
    """<p> DNS queries with delegation records that point to this domain name are forwarded to resolvers on your network. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverRule) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "status" in value:
        import capo_route53resolver.types.resolver_rule_status

        out["Status"] = (
            capo_route53resolver.types.resolver_rule_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "rule_type" in value:
        import capo_route53resolver.types.rule_type_option

        out["RuleType"] = (
            capo_route53resolver.types.rule_type_option.serialize_aws_json_1_1(
                value["rule_type"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "target_ips" in value:
        import capo_route53resolver.types.target_list

        out["TargetIps"] = (
            capo_route53resolver.types.target_list.serialize_aws_json_1_1(
                value["target_ips"]
            )
        )
    if "resolver_endpoint_id" in value:
        out["ResolverEndpointId"] = value["resolver_endpoint_id"]
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "share_status" in value:
        import capo_route53resolver.types.share_status

        out["ShareStatus"] = (
            capo_route53resolver.types.share_status.serialize_aws_json_1_1(
                value["share_status"]
            )
        )
    if "creation_time" in value:
        out["CreationTime"] = value["creation_time"]
    if "modification_time" in value:
        out["ModificationTime"] = value["modification_time"]
    if "delegation_record" in value:
        out["DelegationRecord"] = value["delegation_record"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolverRule:
    out: ResolverRule = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "Status" in data:
        import capo_route53resolver.types.resolver_rule_status

        out["status"] = (
            capo_route53resolver.types.resolver_rule_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "RuleType" in data:
        import capo_route53resolver.types.rule_type_option

        out["rule_type"] = (
            capo_route53resolver.types.rule_type_option.deserialize_aws_json_1_1(
                data["RuleType"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "TargetIps" in data:
        import capo_route53resolver.types.target_list

        out["target_ips"] = (
            capo_route53resolver.types.target_list.deserialize_aws_json_1_1(
                data["TargetIps"]
            )
        )
    if "ResolverEndpointId" in data:
        out["resolver_endpoint_id"] = data["ResolverEndpointId"]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "ShareStatus" in data:
        import capo_route53resolver.types.share_status

        out["share_status"] = (
            capo_route53resolver.types.share_status.deserialize_aws_json_1_1(
                data["ShareStatus"]
            )
        )
    if "CreationTime" in data:
        out["creation_time"] = data["CreationTime"]
    if "ModificationTime" in data:
        out["modification_time"] = data["ModificationTime"]
    if "DelegationRecord" in data:
        out["delegation_record"] = data["DelegationRecord"]
    return out
