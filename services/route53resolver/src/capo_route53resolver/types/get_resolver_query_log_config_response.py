"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetResolverQueryLogConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.resolver_query_log_config


class GetResolverQueryLogConfigResponse(TypedDict, closed=True):
    resolver_query_log_config: NotRequired[
        "capo_route53resolver.types.resolver_query_log_config.ResolverQueryLogConfig"
    ]
    """<p>Information about the Resolver query logging configuration that you specified in a <code>GetQueryLogConfig</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResolverQueryLogConfigResponse) -> dict:
    out: dict = {}
    if "resolver_query_log_config" in value:
        import capo_route53resolver.types.resolver_query_log_config

        out["ResolverQueryLogConfig"] = (
            capo_route53resolver.types.resolver_query_log_config.serialize_aws_json_1_1(
                value["resolver_query_log_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResolverQueryLogConfigResponse:
    out: GetResolverQueryLogConfigResponse = {}  # type: ignore[typeddict-item]
    if "ResolverQueryLogConfig" in data:
        import capo_route53resolver.types.resolver_query_log_config

        out["resolver_query_log_config"] = (
            capo_route53resolver.types.resolver_query_log_config.deserialize_aws_json_1_1(
                data["ResolverQueryLogConfig"]
            )
        )
    return out
