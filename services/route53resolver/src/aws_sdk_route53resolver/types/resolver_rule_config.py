"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverRuleConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.name
    import aws_sdk_route53resolver.types.resource_id
    import aws_sdk_route53resolver.types.target_list


class ResolverRuleConfig(TypedDict):
    name: NotRequired["aws_sdk_route53resolver.types.name.Name"]
    """<p>The new name for the Resolver rule. The name that you specify appears in the Resolver dashboard in the Route 53 console. </p> <p>The name can be up to 64 characters long and can contain letters (a-z, A-Z), numbers (0-9), hyphens (-), underscores (_), and spaces. The name cannot consist of only numbers.</p>"""
    target_ips: NotRequired["aws_sdk_route53resolver.types.target_list.TargetList"]
    """<p>For DNS queries that originate in your VPC, the new IP addresses that you want to route outbound DNS queries to.</p>"""
    resolver_endpoint_id: NotRequired[
        "aws_sdk_route53resolver.types.resource_id.ResourceId"
    ]
    """<p>The ID of the new outbound Resolver endpoint that you want to use to route DNS queries to the IP addresses that you specify in <code>TargetIps</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverRuleConfig) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "target_ips" in value:
        import aws_sdk_route53resolver.types.target_list

        out["TargetIps"] = (
            aws_sdk_route53resolver.types.target_list.serialize_aws_json_1_1(
                value["target_ips"]
            )
        )
    if "resolver_endpoint_id" in value:
        out["ResolverEndpointId"] = value["resolver_endpoint_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolverRuleConfig:
    out: ResolverRuleConfig = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "TargetIps" in data:
        import aws_sdk_route53resolver.types.target_list

        out["target_ips"] = (
            aws_sdk_route53resolver.types.target_list.deserialize_aws_json_1_1(
                data["TargetIps"]
            )
        )
    if "ResolverEndpointId" in data:
        out["resolver_endpoint_id"] = data["ResolverEndpointId"]
    return out
