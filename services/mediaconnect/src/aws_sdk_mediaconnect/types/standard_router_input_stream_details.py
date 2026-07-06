"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StandardRouterInputStreamDetails``."""

from typing_extensions import NotRequired, TypedDict


class StandardRouterInputStreamDetails(TypedDict, closed=True):
    source_ip_address: NotRequired["str"]
    """<p>The source IP address for the standard router input stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StandardRouterInputStreamDetails) -> dict:
    out: dict = {}
    if "source_ip_address" in value:
        out["sourceIpAddress"] = value["source_ip_address"]
    return out


def deserialize_json(data: dict) -> StandardRouterInputStreamDetails:
    out: StandardRouterInputStreamDetails = {}  # type: ignore[typeddict-item]
    if "sourceIpAddress" in data:
        out["source_ip_address"] = data["sourceIpAddress"]
    return out
