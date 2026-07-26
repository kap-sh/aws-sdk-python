"""Generated from Smithy shape ``com.amazonaws.route53resolver#AssociateResolverEndpointIpAddressResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.resolver_endpoint


class AssociateResolverEndpointIpAddressResponse(TypedDict, closed=True):
    resolver_endpoint: NotRequired[
        "capo_route53resolver.types.resolver_endpoint.ResolverEndpoint"
    ]
    """<p>The response to an <code>AssociateResolverEndpointIpAddress</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateResolverEndpointIpAddressResponse) -> dict:
    out: dict = {}
    if "resolver_endpoint" in value:
        import capo_route53resolver.types.resolver_endpoint

        out["ResolverEndpoint"] = (
            capo_route53resolver.types.resolver_endpoint.serialize_aws_json_1_1(
                value["resolver_endpoint"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateResolverEndpointIpAddressResponse:
    out: AssociateResolverEndpointIpAddressResponse = {}  # type: ignore[typeddict-item]
    if "ResolverEndpoint" in data:
        import capo_route53resolver.types.resolver_endpoint

        out["resolver_endpoint"] = (
            capo_route53resolver.types.resolver_endpoint.deserialize_aws_json_1_1(
                data["ResolverEndpoint"]
            )
        )
    return out
