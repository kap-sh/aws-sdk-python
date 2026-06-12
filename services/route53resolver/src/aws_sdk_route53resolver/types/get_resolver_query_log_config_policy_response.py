"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetResolverQueryLogConfigPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resolver_query_log_config_policy


class GetResolverQueryLogConfigPolicyResponse(TypedDict):
    resolver_query_log_config_policy: NotRequired[
        "aws_sdk_route53resolver.types.resolver_query_log_config_policy.ResolverQueryLogConfigPolicy"
    ]
    """<p>Information about the query logging policy for the query logging configuration that you specified in a <code>GetResolverQueryLogConfigPolicy</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResolverQueryLogConfigPolicyResponse) -> dict:
    out: dict = {}
    if "resolver_query_log_config_policy" in value:
        out["ResolverQueryLogConfigPolicy"] = value["resolver_query_log_config_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResolverQueryLogConfigPolicyResponse:
    out: GetResolverQueryLogConfigPolicyResponse = {}  # type: ignore[typeddict-item]
    if "ResolverQueryLogConfigPolicy" in data:
        out["resolver_query_log_config_policy"] = data["ResolverQueryLogConfigPolicy"]
    return out
