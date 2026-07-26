"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RistRouterOutputConfiguration``."""

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError


class RistRouterOutputConfiguration(TypedDict, closed=True):
    destination_address: "str"
    """<p>The destination IP address for the RIST protocol in the router output configuration.</p>"""
    destination_port: "int"
    """<p>The destination port number for the RIST protocol in the router output configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RistRouterOutputConfiguration) -> dict:
    out: dict = {}
    out["destinationAddress"] = value["destination_address"]
    out["destinationPort"] = value["destination_port"]
    return out


def deserialize_json(data: dict) -> RistRouterOutputConfiguration:
    out: RistRouterOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "destinationAddress" in data:
        out["destination_address"] = data["destinationAddress"]
    else:
        raise DeserializationError(
            "RistRouterOutputConfiguration.destination_address required"
        )
    if "destinationPort" in data:
        out["destination_port"] = data["destinationPort"]
    else:
        raise DeserializationError(
            "RistRouterOutputConfiguration.destination_port required"
        )
    return out
