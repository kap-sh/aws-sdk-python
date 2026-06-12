"""Generated from Smithy shape ``com.amazonaws.route53resolver#CreateResolverQueryLogConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resolver_query_log_config


class CreateResolverQueryLogConfigResponse(TypedDict):
    resolver_query_log_config: NotRequired[
        "aws_sdk_route53resolver.types.resolver_query_log_config.ResolverQueryLogConfig"
    ]
    """<p>Information about the <code>CreateResolverQueryLogConfig</code> request, including the status of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateResolverQueryLogConfigResponse) -> dict:
    out: dict = {}
    if "resolver_query_log_config" in value:
        import aws_sdk_route53resolver.types.resolver_query_log_config

        out["ResolverQueryLogConfig"] = (
            aws_sdk_route53resolver.types.resolver_query_log_config.serialize_aws_json_1_1(
                value["resolver_query_log_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateResolverQueryLogConfigResponse:
    out: CreateResolverQueryLogConfigResponse = {}  # type: ignore[typeddict-item]
    if "ResolverQueryLogConfig" in data:
        import aws_sdk_route53resolver.types.resolver_query_log_config

        out["resolver_query_log_config"] = (
            aws_sdk_route53resolver.types.resolver_query_log_config.deserialize_aws_json_1_1(
                data["ResolverQueryLogConfig"]
            )
        )
    return out
