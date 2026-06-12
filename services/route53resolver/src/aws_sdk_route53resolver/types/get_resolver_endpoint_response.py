"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetResolverEndpointResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resolver_endpoint


class GetResolverEndpointResponse(TypedDict):
    resolver_endpoint: NotRequired[
        "aws_sdk_route53resolver.types.resolver_endpoint.ResolverEndpoint"
    ]
    """<p>Information about the Resolver endpoint that you specified in a <code>GetResolverEndpoint</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResolverEndpointResponse) -> dict:
    out: dict = {}
    if "resolver_endpoint" in value:
        import aws_sdk_route53resolver.types.resolver_endpoint

        out["ResolverEndpoint"] = (
            aws_sdk_route53resolver.types.resolver_endpoint.serialize_aws_json_1_1(
                value["resolver_endpoint"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResolverEndpointResponse:
    out: GetResolverEndpointResponse = {}  # type: ignore[typeddict-item]
    if "ResolverEndpoint" in data:
        import aws_sdk_route53resolver.types.resolver_endpoint

        out["resolver_endpoint"] = (
            aws_sdk_route53resolver.types.resolver_endpoint.deserialize_aws_json_1_1(
                data["ResolverEndpoint"]
            )
        )
    return out
