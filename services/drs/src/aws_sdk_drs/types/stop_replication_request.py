"""Generated from Smithy shape ``com.amazonaws.drs#StopReplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.source_server_id


class StopReplicationRequest(TypedDict, closed=True):
    source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID"
    """<p>The ID of the Source Server to stop replication for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopReplicationRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    return out


def deserialize_json(data: dict) -> StopReplicationRequest:
    out: StopReplicationRequest = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    else:
        raise DeserializationError("StopReplicationRequest.source_server_id required")
    return out
