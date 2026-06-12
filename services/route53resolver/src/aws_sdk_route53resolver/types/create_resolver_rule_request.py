"""Generated from Smithy shape ``com.amazonaws.route53resolver#CreateResolverRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.creator_request_id
    import aws_sdk_route53resolver.types.delegation_record
    import aws_sdk_route53resolver.types.domain_name
    import aws_sdk_route53resolver.types.name
    import aws_sdk_route53resolver.types.resource_id
    import aws_sdk_route53resolver.types.rule_type_option
    import aws_sdk_route53resolver.types.tag_list
    import aws_sdk_route53resolver.types.target_list


class CreateResolverRuleRequest(TypedDict):
    creator_request_id: (
        "aws_sdk_route53resolver.types.creator_request_id.CreatorRequestId"
    )
    """<p>A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice. <code>CreatorRequestId</code> can be any unique string, for example, a date/time stamp. </p>"""
    name: NotRequired["aws_sdk_route53resolver.types.name.Name"]
    """<p>A friendly name that lets you easily find a rule in the Resolver dashboard in the Route 53 console.</p> <p>The name can be up to 64 characters long and can contain letters (a-z, A-Z), numbers (0-9), hyphens (-), underscores (_), and spaces. The name cannot consist of only numbers.</p>"""
    rule_type: "aws_sdk_route53resolver.types.rule_type_option.RuleTypeOption"
    """<p>When you want to forward DNS queries for specified domain name to resolvers on your network, specify <code>FORWARD</code> or <code>DELEGATE</code>.</p> <p>When you have a forwarding rule to forward DNS queries for a domain to your network and you want Resolver to process queries for a subdomain of that domain, specify <code>SYSTEM</code>.</p> <p>For example, to forward DNS queries for example.com to resolvers on your network, you create a rule and specify <code>FORWARD</code> for <code>RuleType</code>. To then have Resolver process queries for apex.example.com, you create a rule and specify <code>SYSTEM</code> for <code>RuleType</code>.</p> <p>Currently, only Resolver can create rules that have a value of <code>RECURSIVE</code> for <code>RuleType</code>.</p>"""
    domain_name: NotRequired["aws_sdk_route53resolver.types.domain_name.DomainName"]
    """<p>DNS queries for this domain name are forwarded to the IP addresses that you specify in <code>TargetIps</code>. If a query matches multiple Resolver rules (example.com and www.example.com), outbound DNS queries are routed using the Resolver rule that contains the most specific domain name (www.example.com).</p>"""
    target_ips: NotRequired["aws_sdk_route53resolver.types.target_list.TargetList"]
    """<p>The IPs that you want Resolver to forward DNS queries to. You can specify either Ipv4 or Ipv6 addresses but not both in the same rule. Separate IP addresses with a space.</p> <p> <code>TargetIps</code> is available only when the value of <code>Rule type</code> is <code>FORWARD</code>. You should not provide TargetIps when the Rule type is <code>DELEGATE</code>.</p> <note> <p>when creating a DELEGATE rule, you must not provide the <code>TargetIps</code> parameter. If you provide the <code>TargetIps</code>, you may receive an ERROR message similar to \"Delegate resolver rules need to specify a nameserver name\". This error means you should not provide <code>TargetIps</code>.</p> </note>"""
    resolver_endpoint_id: NotRequired[
        "aws_sdk_route53resolver.types.resource_id.ResourceId"
    ]
    """<p>The ID of the outbound Resolver endpoint that you want to use to route DNS queries to the IP addresses that you specify in <code>TargetIps</code>.</p>"""
    tags: NotRequired["aws_sdk_route53resolver.types.tag_list.TagList"]
    """<p>A list of the tag keys and values that you want to associate with the endpoint.</p>"""
    delegation_record: NotRequired[
        "aws_sdk_route53resolver.types.delegation_record.DelegationRecord"
    ]
    """<p> DNS queries with the delegation records that match this domain name are forwarded to the resolvers on your network. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateResolverRuleRequest) -> dict:
    out: dict = {}
    out["CreatorRequestId"] = value["creator_request_id"]
    if "name" in value:
        out["Name"] = value["name"]
    import aws_sdk_route53resolver.types.rule_type_option

    out["RuleType"] = (
        aws_sdk_route53resolver.types.rule_type_option.serialize_aws_json_1_1(
            value["rule_type"]
        )
    )
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "target_ips" in value:
        import aws_sdk_route53resolver.types.target_list

        out["TargetIps"] = (
            aws_sdk_route53resolver.types.target_list.serialize_aws_json_1_1(
                value["target_ips"]
            )
        )
    if "resolver_endpoint_id" in value:
        out["ResolverEndpointId"] = value["resolver_endpoint_id"]
    if "tags" in value:
        import aws_sdk_route53resolver.types.tag_list

        out["Tags"] = aws_sdk_route53resolver.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "delegation_record" in value:
        out["DelegationRecord"] = value["delegation_record"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateResolverRuleRequest:
    out: CreateResolverRuleRequest = {}  # type: ignore[typeddict-item]
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    else:
        raise DeserializationError(
            "CreateResolverRuleRequest.creator_request_id required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "RuleType" in data:
        import aws_sdk_route53resolver.types.rule_type_option

        out["rule_type"] = (
            aws_sdk_route53resolver.types.rule_type_option.deserialize_aws_json_1_1(
                data["RuleType"]
            )
        )
    else:
        raise DeserializationError("CreateResolverRuleRequest.rule_type required")
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "TargetIps" in data:
        import aws_sdk_route53resolver.types.target_list

        out["target_ips"] = (
            aws_sdk_route53resolver.types.target_list.deserialize_aws_json_1_1(
                data["TargetIps"]
            )
        )
    if "ResolverEndpointId" in data:
        out["resolver_endpoint_id"] = data["ResolverEndpointId"]
    if "Tags" in data:
        import aws_sdk_route53resolver.types.tag_list

        out["tags"] = aws_sdk_route53resolver.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "DelegationRecord" in data:
        out["delegation_record"] = data["DelegationRecord"]
    return out
