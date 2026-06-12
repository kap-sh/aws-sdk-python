"""Generated from Smithy shape ``com.amazonaws.finspace#UpdateKxEnvironmentNetworkRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.client_token
    import aws_sdk_finspace.types.custom_dns_configuration
    import aws_sdk_finspace.types.id_type
    import aws_sdk_finspace.types.transit_gateway_configuration


class UpdateKxEnvironmentNetworkRequest(TypedDict):
    environment_id: "aws_sdk_finspace.types.id_type.IdType"
    """<p>A unique identifier for the kdb environment.</p>"""
    transit_gateway_configuration: NotRequired[
        "aws_sdk_finspace.types.transit_gateway_configuration.TransitGatewayConfiguration"
    ]
    """<p>Specifies the transit gateway and network configuration to connect the kdb environment to an internal network.</p>"""
    custom_dns_configuration: NotRequired[
        "aws_sdk_finspace.types.custom_dns_configuration.CustomDNSConfiguration"
    ]
    """<p>A list of DNS server name and server IP. This is used to set up Route-53 outbound resolvers.</p>"""
    client_token: NotRequired["aws_sdk_finspace.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKxEnvironmentNetworkRequest) -> dict:
    out: dict = {}
    if "transit_gateway_configuration" in value:
        import aws_sdk_finspace.types.transit_gateway_configuration

        out["transitGatewayConfiguration"] = (
            aws_sdk_finspace.types.transit_gateway_configuration.serialize_json(
                value["transit_gateway_configuration"]
            )
        )
    if "custom_dns_configuration" in value:
        import aws_sdk_finspace.types.custom_dns_configuration

        out["customDNSConfiguration"] = (
            aws_sdk_finspace.types.custom_dns_configuration.serialize_json(
                value["custom_dns_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateKxEnvironmentNetworkRequest:
    out: UpdateKxEnvironmentNetworkRequest = {}  # type: ignore[typeddict-item]
    if "transitGatewayConfiguration" in data:
        import aws_sdk_finspace.types.transit_gateway_configuration

        out["transit_gateway_configuration"] = (
            aws_sdk_finspace.types.transit_gateway_configuration.deserialize_json(
                data["transitGatewayConfiguration"]
            )
        )
    if "customDNSConfiguration" in data:
        import aws_sdk_finspace.types.custom_dns_configuration

        out["custom_dns_configuration"] = (
            aws_sdk_finspace.types.custom_dns_configuration.deserialize_json(
                data["customDNSConfiguration"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
