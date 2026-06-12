"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverEndpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resolver_endpoint

ResolverEndpoints: TypeAlias = list[
    "aws_sdk_route53resolver.types.resolver_endpoint.ResolverEndpoint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverEndpoints) -> list:
    import aws_sdk_route53resolver.types.resolver_endpoint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53resolver.types.resolver_endpoint.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResolverEndpoints:
    import aws_sdk_route53resolver.types.resolver_endpoint

    out: ResolverEndpoints = []
    for item in data:
        out.append(
            aws_sdk_route53resolver.types.resolver_endpoint.deserialize_aws_json_1_1(
                item
            )
        )
    return out
