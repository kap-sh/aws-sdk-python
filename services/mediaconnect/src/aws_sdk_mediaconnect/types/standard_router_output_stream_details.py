"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StandardRouterOutputStreamDetails``."""

from typing import TypedDict

from typing_extensions import NotRequired


class StandardRouterOutputStreamDetails(TypedDict):
    destination_ip_address: NotRequired["str"]
    """<p>The IP address where the output stream will be sent. This is the destination address that will receive the routed media content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StandardRouterOutputStreamDetails) -> dict:
    out: dict = {}
    if "destination_ip_address" in value:
        out["destinationIpAddress"] = value["destination_ip_address"]
    return out


def deserialize_json(data: dict) -> StandardRouterOutputStreamDetails:
    out: StandardRouterOutputStreamDetails = {}  # type: ignore[typeddict-item]
    if "destinationIpAddress" in data:
        out["destination_ip_address"] = data["destinationIpAddress"]
    return out
