"""Generated from Smithy shape ``com.amazonaws.route53resolver#DisassociateResolverEndpointIpAddressRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.ip_address_update
    import aws_sdk_route53resolver.types.resource_id


class DisassociateResolverEndpointIpAddressRequest(TypedDict):
    resolver_endpoint_id: "aws_sdk_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the Resolver endpoint that you want to disassociate an IP address from.</p>"""
    ip_address: "aws_sdk_route53resolver.types.ip_address_update.IpAddressUpdate"
    """<p>The IPv4 address that you want to remove from a Resolver endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateResolverEndpointIpAddressRequest) -> dict:
    out: dict = {}
    out["ResolverEndpointId"] = value["resolver_endpoint_id"]
    import aws_sdk_route53resolver.types.ip_address_update

    out["IpAddress"] = (
        aws_sdk_route53resolver.types.ip_address_update.serialize_aws_json_1_1(
            value["ip_address"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DisassociateResolverEndpointIpAddressRequest:
    out: DisassociateResolverEndpointIpAddressRequest = {}  # type: ignore[typeddict-item]
    if "ResolverEndpointId" in data:
        out["resolver_endpoint_id"] = data["ResolverEndpointId"]
    else:
        raise DeserializationError(
            "DisassociateResolverEndpointIpAddressRequest.resolver_endpoint_id required"
        )
    if "IpAddress" in data:
        import aws_sdk_route53resolver.types.ip_address_update

        out["ip_address"] = (
            aws_sdk_route53resolver.types.ip_address_update.deserialize_aws_json_1_1(
                data["IpAddress"]
            )
        )
    else:
        raise DeserializationError(
            "DisassociateResolverEndpointIpAddressRequest.ip_address required"
        )
    return out
