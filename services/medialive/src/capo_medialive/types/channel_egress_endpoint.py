"""Generated from Smithy shape ``com.amazonaws.medialive#ChannelEgressEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class ChannelEgressEndpoint(TypedDict, closed=True):
    source_ip: NotRequired["capo_medialive.types.__string.__string"]
    """Public IP of where a channel's output comes from"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelEgressEndpoint) -> dict:
    out: dict = {}
    if "source_ip" in value:
        out["sourceIp"] = value["source_ip"]
    return out


def deserialize_json(data: dict) -> ChannelEgressEndpoint:
    out: ChannelEgressEndpoint = {}  # type: ignore[typeddict-item]
    if "sourceIp" in data:
        out["source_ip"] = data["sourceIp"]
    return out
