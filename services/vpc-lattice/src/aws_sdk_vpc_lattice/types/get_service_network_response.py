"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetServiceNetworkResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.auth_type
    import aws_sdk_vpc_lattice.types.service_network_arn
    import aws_sdk_vpc_lattice.types.service_network_id
    import aws_sdk_vpc_lattice.types.service_network_name
    import aws_sdk_vpc_lattice.types.sharing_config
    import aws_sdk_vpc_lattice.types.timestamp


class GetServiceNetworkResponse(TypedDict):
    id: NotRequired["aws_sdk_vpc_lattice.types.service_network_id.ServiceNetworkId"]
    """<p>The ID of the service network.</p>"""
    name: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_name.ServiceNetworkName"
    ]
    """<p>The name of the service network.</p>"""
    created_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the service network was created, in ISO-8601 format.</p>"""
    last_updated_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time of the last update, in ISO-8601 format.</p>"""
    arn: NotRequired["aws_sdk_vpc_lattice.types.service_network_arn.ServiceNetworkArn"]
    """<p>The Amazon Resource Name (ARN) of the service network.</p>"""
    auth_type: NotRequired["aws_sdk_vpc_lattice.types.auth_type.AuthType"]
    """<p>The type of IAM policy.</p>"""
    sharing_config: NotRequired[
        "aws_sdk_vpc_lattice.types.sharing_config.SharingConfig"
    ]
    """<p>Specifies if the service network is enabled for sharing.</p>"""
    number_of_associated_vp_cs: NotRequired["int"]
    """<p>The number of VPCs associated with the service network.</p>"""
    number_of_associated_services: NotRequired["int"]
    """<p>The number of services associated with the service network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceNetworkResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "created_at" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["createdAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["lastUpdatedAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "auth_type" in value:
        out["authType"] = value["auth_type"]
    if "sharing_config" in value:
        import aws_sdk_vpc_lattice.types.sharing_config

        out["sharingConfig"] = aws_sdk_vpc_lattice.types.sharing_config.serialize_json(
            value["sharing_config"]
        )
    if "number_of_associated_vp_cs" in value:
        out["numberOfAssociatedVPCs"] = value["number_of_associated_vp_cs"]
    if "number_of_associated_services" in value:
        out["numberOfAssociatedServices"] = value["number_of_associated_services"]
    return out


def deserialize_json(data: dict) -> GetServiceNetworkResponse:
    out: GetServiceNetworkResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "createdAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["created_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["last_updated_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    if "authType" in data:
        out["auth_type"] = data["authType"]
    if "sharingConfig" in data:
        import aws_sdk_vpc_lattice.types.sharing_config

        out["sharing_config"] = (
            aws_sdk_vpc_lattice.types.sharing_config.deserialize_json(
                data["sharingConfig"]
            )
        )
    if "numberOfAssociatedVPCs" in data:
        out["number_of_associated_vp_cs"] = data["numberOfAssociatedVPCs"]
    if "numberOfAssociatedServices" in data:
        out["number_of_associated_services"] = data["numberOfAssociatedServices"]
    return out
