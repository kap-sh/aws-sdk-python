"""Generated from Smithy shape ``com.amazonaws.medialive#MulticastInputSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class MulticastInputSettings(TypedDict, closed=True):
    source_ip_address: NotRequired["capo_medialive.types.__string.__string"]
    """Optionally, a source ip address to filter by for Source-specific Multicast (SSM)"""


# --- restJson1 ser/de ---
def serialize_json(value: MulticastInputSettings) -> dict:
    out: dict = {}
    if "source_ip_address" in value:
        out["sourceIpAddress"] = value["source_ip_address"]
    return out


def deserialize_json(data: dict) -> MulticastInputSettings:
    out: MulticastInputSettings = {}  # type: ignore[typeddict-item]
    if "sourceIpAddress" in data:
        out["source_ip_address"] = data["sourceIpAddress"]
    return out
