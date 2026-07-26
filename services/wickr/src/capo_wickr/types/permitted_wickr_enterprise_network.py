"""Generated from Smithy shape ``com.amazonaws.wickr#PermittedWickrEnterpriseNetwork``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.network_id


class PermittedWickrEnterpriseNetwork(TypedDict, closed=True):
    domain: "capo_wickr.types.generic_string.GenericString"
    """<p>The domain identifier for the permitted Wickr enterprise network.</p>"""
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The network ID of the permitted Wickr enterprise network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermittedWickrEnterpriseNetwork) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    out["networkId"] = value["network_id"]
    return out


def deserialize_json(data: dict) -> PermittedWickrEnterpriseNetwork:
    out: PermittedWickrEnterpriseNetwork = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("PermittedWickrEnterpriseNetwork.domain required")
    if "networkId" in data:
        out["network_id"] = data["networkId"]
    else:
        raise DeserializationError(
            "PermittedWickrEnterpriseNetwork.network_id required"
        )
    return out
