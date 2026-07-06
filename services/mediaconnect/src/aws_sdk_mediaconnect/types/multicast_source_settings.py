"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MulticastSourceSettings``."""

from typing_extensions import NotRequired, TypedDict


class MulticastSourceSettings(TypedDict, closed=True):
    multicast_source_ip: NotRequired["str"]
    """<p> The IP address of the source for source-specific multicast (SSM).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MulticastSourceSettings) -> dict:
    out: dict = {}
    if "multicast_source_ip" in value:
        out["multicastSourceIp"] = value["multicast_source_ip"]
    return out


def deserialize_json(data: dict) -> MulticastSourceSettings:
    out: MulticastSourceSettings = {}  # type: ignore[typeddict-item]
    if "multicastSourceIp" in data:
        out["multicast_source_ip"] = data["multicastSourceIp"]
    return out
