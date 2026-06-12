"""Generated from Smithy shape ``com.amazonaws.drs#DeleteSourceNetworkRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_drs.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_drs.types.source_network_id

class DeleteSourceNetworkRequest(TypedDict):
    source_network_id: "aws_sdk_drs.types.source_network_id.SourceNetworkID"
    """<p>ID of the Source Network to delete.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteSourceNetworkRequest) -> dict:
    out: dict = {}
    out["sourceNetworkID"] = value["source_network_id"]
    return out


def deserialize_json(data: dict) -> DeleteSourceNetworkRequest:
    out: DeleteSourceNetworkRequest = {}  # type: ignore[typeddict-item]
    if "sourceNetworkID" in data:
        out["source_network_id"] = data["sourceNetworkID"]
    else:
        raise DeserializationError("DeleteSourceNetworkRequest.source_network_id required")
    return out