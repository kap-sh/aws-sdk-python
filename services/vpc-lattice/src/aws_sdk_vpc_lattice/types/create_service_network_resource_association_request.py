"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateServiceNetworkResourceAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.boolean
    import aws_sdk_vpc_lattice.types.client_token
    import aws_sdk_vpc_lattice.types.resource_configuration_identifier
    import aws_sdk_vpc_lattice.types.service_network_identifier_without_regex
    import aws_sdk_vpc_lattice.types.tag_map


class CreateServiceNetworkResourceAssociationRequest(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_vpc_lattice.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>"""
    resource_configuration_identifier: "aws_sdk_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
    """<p>The ID of the resource configuration to associate with the service network.</p>"""
    service_network_identifier: "aws_sdk_vpc_lattice.types.service_network_identifier_without_regex.ServiceNetworkIdentifierWithoutRegex"
    """<p>The ID of the service network to associate with the resource configuration.</p>"""
    private_dns_enabled: NotRequired["aws_sdk_vpc_lattice.types.boolean.Boolean"]
    """<p> Indicates if private DNS is enabled for the service network resource association. </p>"""
    tags: NotRequired["aws_sdk_vpc_lattice.types.tag_map.TagMap"]
    """<p>A key-value pair to associate with a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceNetworkResourceAssociationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["resourceConfigurationIdentifier"] = value["resource_configuration_identifier"]
    out["serviceNetworkIdentifier"] = value["service_network_identifier"]
    if "private_dns_enabled" in value:
        out["privateDnsEnabled"] = value["private_dns_enabled"]
    if "tags" in value:
        import aws_sdk_vpc_lattice.types.tag_map

        out["tags"] = aws_sdk_vpc_lattice.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateServiceNetworkResourceAssociationRequest:
    out: CreateServiceNetworkResourceAssociationRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "resourceConfigurationIdentifier" in data:
        out["resource_configuration_identifier"] = data[
            "resourceConfigurationIdentifier"
        ]
    else:
        raise DeserializationError(
            "CreateServiceNetworkResourceAssociationRequest.resource_configuration_identifier required"
        )
    if "serviceNetworkIdentifier" in data:
        out["service_network_identifier"] = data["serviceNetworkIdentifier"]
    else:
        raise DeserializationError(
            "CreateServiceNetworkResourceAssociationRequest.service_network_identifier required"
        )
    if "privateDnsEnabled" in data:
        out["private_dns_enabled"] = data["privateDnsEnabled"]
    if "tags" in data:
        import aws_sdk_vpc_lattice.types.tag_map

        out["tags"] = aws_sdk_vpc_lattice.types.tag_map.deserialize_json(data["tags"])
    return out
