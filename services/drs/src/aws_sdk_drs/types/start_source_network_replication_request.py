"""Generated from Smithy shape ``com.amazonaws.drs#StartSourceNetworkReplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.source_network_id


class StartSourceNetworkReplicationRequest(TypedDict, closed=True):
    source_network_id: "aws_sdk_drs.types.source_network_id.SourceNetworkID"
    """<p>ID of the Source Network to replicate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSourceNetworkReplicationRequest) -> dict:
    out: dict = {}
    out["sourceNetworkID"] = value["source_network_id"]
    return out


def deserialize_json(data: dict) -> StartSourceNetworkReplicationRequest:
    out: StartSourceNetworkReplicationRequest = {}  # type: ignore[typeddict-item]
    if "sourceNetworkID" in data:
        out["source_network_id"] = data["sourceNetworkID"]
    else:
        raise DeserializationError(
            "StartSourceNetworkReplicationRequest.source_network_id required"
        )
    return out
