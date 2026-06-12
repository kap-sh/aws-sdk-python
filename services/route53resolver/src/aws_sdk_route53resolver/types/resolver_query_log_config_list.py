"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverQueryLogConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resolver_query_log_config

ResolverQueryLogConfigList: TypeAlias = list[
    "aws_sdk_route53resolver.types.resolver_query_log_config.ResolverQueryLogConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverQueryLogConfigList) -> list:
    import aws_sdk_route53resolver.types.resolver_query_log_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53resolver.types.resolver_query_log_config.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResolverQueryLogConfigList:
    import aws_sdk_route53resolver.types.resolver_query_log_config

    out: ResolverQueryLogConfigList = []
    for item in data:
        out.append(
            aws_sdk_route53resolver.types.resolver_query_log_config.deserialize_aws_json_1_1(
                item
            )
        )
    return out
