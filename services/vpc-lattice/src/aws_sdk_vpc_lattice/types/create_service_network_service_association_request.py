"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateServiceNetworkServiceAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.client_token
    import aws_sdk_vpc_lattice.types.service_identifier
    import aws_sdk_vpc_lattice.types.service_network_identifier
    import aws_sdk_vpc_lattice.types.tag_map


class CreateServiceNetworkServiceAssociationRequest(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_vpc_lattice.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>"""
    service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier"
    """<p>The ID or ARN of the service.</p>"""
    service_network_identifier: (
        "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier"
    )
    """<p>The ID or ARN of the service network. You must use an ARN if the resources are in different accounts.</p>"""
    tags: NotRequired["aws_sdk_vpc_lattice.types.tag_map.TagMap"]
    """<p>The tags for the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceNetworkServiceAssociationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["serviceIdentifier"] = value["service_identifier"]
    out["serviceNetworkIdentifier"] = value["service_network_identifier"]
    if "tags" in value:
        import aws_sdk_vpc_lattice.types.tag_map

        out["tags"] = aws_sdk_vpc_lattice.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateServiceNetworkServiceAssociationRequest:
    out: CreateServiceNetworkServiceAssociationRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "serviceIdentifier" in data:
        out["service_identifier"] = data["serviceIdentifier"]
    else:
        raise DeserializationError(
            "CreateServiceNetworkServiceAssociationRequest.service_identifier required"
        )
    if "serviceNetworkIdentifier" in data:
        out["service_network_identifier"] = data["serviceNetworkIdentifier"]
    else:
        raise DeserializationError(
            "CreateServiceNetworkServiceAssociationRequest.service_network_identifier required"
        )
    if "tags" in data:
        import aws_sdk_vpc_lattice.types.tag_map

        out["tags"] = aws_sdk_vpc_lattice.types.tag_map.deserialize_json(data["tags"])
    return out
