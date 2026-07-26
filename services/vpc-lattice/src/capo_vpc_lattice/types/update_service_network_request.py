"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateServiceNetworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_vpc_lattice.types.auth_type
    import capo_vpc_lattice.types.service_network_identifier


class UpdateServiceNetworkRequest(TypedDict, closed=True):
    service_network_identifier: (
        "capo_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier"
    )
    """<p>The ID or ARN of the service network.</p>"""
    auth_type: "capo_vpc_lattice.types.auth_type.AuthType"
    """<p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceNetworkRequest) -> dict:
    out: dict = {}
    out["authType"] = value["auth_type"]
    return out


def deserialize_json(data: dict) -> UpdateServiceNetworkRequest:
    out: UpdateServiceNetworkRequest = {}  # type: ignore[typeddict-item]
    if "authType" in data:
        out["auth_type"] = data["authType"]
    else:
        raise DeserializationError("UpdateServiceNetworkRequest.auth_type required")
    return out
