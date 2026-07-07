"""Generated from Smithy shape ``com.amazonaws.route53resolver#DisassociateResolverEndpointIpAddressResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resolver_endpoint


class DisassociateResolverEndpointIpAddressResponse(TypedDict, closed=True):
    resolver_endpoint: NotRequired[
        "aws_sdk_route53resolver.types.resolver_endpoint.ResolverEndpoint"
    ]
    """<p>The response to an <code>DisassociateResolverEndpointIpAddress</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DisassociateResolverEndpointIpAddressResponse,
) -> dict:
    out: dict = {}
    if "resolver_endpoint" in value:
        import aws_sdk_route53resolver.types.resolver_endpoint

        out["ResolverEndpoint"] = (
            aws_sdk_route53resolver.types.resolver_endpoint.serialize_aws_json_1_1(
                value["resolver_endpoint"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DisassociateResolverEndpointIpAddressResponse:
    out: DisassociateResolverEndpointIpAddressResponse = {}  # type: ignore[typeddict-item]
    if "ResolverEndpoint" in data:
        import aws_sdk_route53resolver.types.resolver_endpoint

        out["resolver_endpoint"] = (
            aws_sdk_route53resolver.types.resolver_endpoint.deserialize_aws_json_1_1(
                data["ResolverEndpoint"]
            )
        )
    return out
