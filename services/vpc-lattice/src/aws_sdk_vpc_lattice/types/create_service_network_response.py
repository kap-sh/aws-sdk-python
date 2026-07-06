"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateServiceNetworkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.auth_type
    import aws_sdk_vpc_lattice.types.service_network_arn
    import aws_sdk_vpc_lattice.types.service_network_id
    import aws_sdk_vpc_lattice.types.service_network_name
    import aws_sdk_vpc_lattice.types.sharing_config


class CreateServiceNetworkResponse(TypedDict, closed=True):
    id: NotRequired["aws_sdk_vpc_lattice.types.service_network_id.ServiceNetworkId"]
    """<p>The ID of the service network.</p>"""
    name: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_name.ServiceNetworkName"
    ]
    """<p>The name of the service network.</p>"""
    arn: NotRequired["aws_sdk_vpc_lattice.types.service_network_arn.ServiceNetworkArn"]
    """<p>The Amazon Resource Name (ARN) of the service network.</p>"""
    sharing_config: NotRequired[
        "aws_sdk_vpc_lattice.types.sharing_config.SharingConfig"
    ]
    """<p>Specifies if the service network is enabled for sharing.</p>"""
    auth_type: NotRequired["aws_sdk_vpc_lattice.types.auth_type.AuthType"]
    """<p>The type of IAM policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceNetworkResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "sharing_config" in value:
        import aws_sdk_vpc_lattice.types.sharing_config

        out["sharingConfig"] = aws_sdk_vpc_lattice.types.sharing_config.serialize_json(
            value["sharing_config"]
        )
    if "auth_type" in value:
        out["authType"] = value["auth_type"]
    return out


def deserialize_json(data: dict) -> CreateServiceNetworkResponse:
    out: CreateServiceNetworkResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "sharingConfig" in data:
        import aws_sdk_vpc_lattice.types.sharing_config

        out["sharing_config"] = (
            aws_sdk_vpc_lattice.types.sharing_config.deserialize_json(
                data["sharingConfig"]
            )
        )
    if "authType" in data:
        out["auth_type"] = data["authType"]
    return out
