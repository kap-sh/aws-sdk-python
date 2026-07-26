"""Generated from Smithy shape ``com.amazonaws.route53resolver#DeleteResolverQueryLogConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.resolver_query_log_config


class DeleteResolverQueryLogConfigResponse(TypedDict, closed=True):
    resolver_query_log_config: NotRequired[
        "capo_route53resolver.types.resolver_query_log_config.ResolverQueryLogConfig"
    ]
    """<p>Information about the query logging configuration that you deleted, including the status of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResolverQueryLogConfigResponse) -> dict:
    out: dict = {}
    if "resolver_query_log_config" in value:
        import capo_route53resolver.types.resolver_query_log_config

        out["ResolverQueryLogConfig"] = (
            capo_route53resolver.types.resolver_query_log_config.serialize_aws_json_1_1(
                value["resolver_query_log_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResolverQueryLogConfigResponse:
    out: DeleteResolverQueryLogConfigResponse = {}  # type: ignore[typeddict-item]
    if "ResolverQueryLogConfig" in data:
        import capo_route53resolver.types.resolver_query_log_config

        out["resolver_query_log_config"] = (
            capo_route53resolver.types.resolver_query_log_config.deserialize_aws_json_1_1(
                data["ResolverQueryLogConfig"]
            )
        )
    return out
