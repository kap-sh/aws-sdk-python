"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resolver_config

ResolverConfigList: TypeAlias = list[
    "aws_sdk_route53resolver.types.resolver_config.ResolverConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverConfigList) -> list:
    import aws_sdk_route53resolver.types.resolver_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53resolver.types.resolver_config.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResolverConfigList:
    import aws_sdk_route53resolver.types.resolver_config

    out: ResolverConfigList = []
    for item in data:
        out.append(
            aws_sdk_route53resolver.types.resolver_config.deserialize_aws_json_1_1(item)
        )
    return out
