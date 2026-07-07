"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FailoverRouterInputIndexedStreamDetails``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError


class FailoverRouterInputIndexedStreamDetails(TypedDict, closed=True):
    source_index: "int"
    """<p>The index number (0 or 1) assigned to this source in the failover configuration.</p>"""
    source_ip_address: NotRequired["str"]
    """<p>The IP address of the source for this indexed stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailoverRouterInputIndexedStreamDetails) -> dict:
    out: dict = {}
    out["sourceIndex"] = value["source_index"]
    if "source_ip_address" in value:
        out["sourceIpAddress"] = value["source_ip_address"]
    return out


def deserialize_json(data: dict) -> FailoverRouterInputIndexedStreamDetails:
    out: FailoverRouterInputIndexedStreamDetails = {}  # type: ignore[typeddict-item]
    if "sourceIndex" in data:
        out["source_index"] = data["sourceIndex"]
    else:
        raise DeserializationError(
            "FailoverRouterInputIndexedStreamDetails.source_index required"
        )
    if "sourceIpAddress" in data:
        out["source_ip_address"] = data["sourceIpAddress"]
    return out
