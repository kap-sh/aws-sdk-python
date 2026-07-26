"""Generated from Smithy shape ``com.amazonaws.drs#CreateSourceNetworkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.source_network_id


class CreateSourceNetworkResponse(TypedDict, closed=True):
    source_network_id: NotRequired["capo_drs.types.source_network_id.SourceNetworkID"]
    """<p>ID of the created Source Network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSourceNetworkResponse) -> dict:
    out: dict = {}
    if "source_network_id" in value:
        out["sourceNetworkID"] = value["source_network_id"]
    return out


def deserialize_json(data: dict) -> CreateSourceNetworkResponse:
    out: CreateSourceNetworkResponse = {}  # type: ignore[typeddict-item]
    if "sourceNetworkID" in data:
        out["source_network_id"] = data["sourceNetworkID"]
    return out
