"""Generated from Smithy shape ``com.amazonaws.medialive#MulticastSourceCreateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class MulticastSourceCreateRequest(TypedDict, closed=True):
    source_ip: NotRequired["capo_medialive.types.__string.__string"]
    """This represents the ip address of the device sending the multicast stream."""
    url: NotRequired["capo_medialive.types.__string.__string"]
    """This represents the customer's source URL where multicast stream is pulled from."""


# --- restJson1 ser/de ---
def serialize_json(value: MulticastSourceCreateRequest) -> dict:
    out: dict = {}
    if "source_ip" in value:
        out["sourceIp"] = value["source_ip"]
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> MulticastSourceCreateRequest:
    out: MulticastSourceCreateRequest = {}  # type: ignore[typeddict-item]
    if "sourceIp" in data:
        out["source_ip"] = data["sourceIp"]
    if "url" in data:
        out["url"] = data["url"]
    return out
