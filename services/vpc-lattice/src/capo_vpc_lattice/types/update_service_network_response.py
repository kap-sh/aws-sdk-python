"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateServiceNetworkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.auth_type
    import capo_vpc_lattice.types.service_network_arn
    import capo_vpc_lattice.types.service_network_id
    import capo_vpc_lattice.types.service_network_name


class UpdateServiceNetworkResponse(TypedDict, closed=True):
    id: NotRequired["capo_vpc_lattice.types.service_network_id.ServiceNetworkId"]
    """<p>The ID of the service network.</p>"""
    name: NotRequired["capo_vpc_lattice.types.service_network_name.ServiceNetworkName"]
    """<p>The name of the service network.</p>"""
    arn: NotRequired["capo_vpc_lattice.types.service_network_arn.ServiceNetworkArn"]
    """<p>The Amazon Resource Name (ARN) of the service network.</p>"""
    auth_type: NotRequired["capo_vpc_lattice.types.auth_type.AuthType"]
    """<p>The type of IAM policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceNetworkResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "auth_type" in value:
        out["authType"] = value["auth_type"]
    return out


def deserialize_json(data: dict) -> UpdateServiceNetworkResponse:
    out: UpdateServiceNetworkResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "authType" in data:
        out["auth_type"] = data["authType"]
    return out
