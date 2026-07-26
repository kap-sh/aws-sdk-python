"""Generated from Smithy shape ``com.amazonaws.mgn#PauseReplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.source_server_id


class PauseReplicationRequest(TypedDict, closed=True):
    source_server_id: "capo_mgn.types.source_server_id.SourceServerID"
    """<p>Pause Replication Request source server ID.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Pause Replication Request account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PauseReplicationRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> PauseReplicationRequest:
    out: PauseReplicationRequest = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    else:
        raise DeserializationError("PauseReplicationRequest.source_server_id required")
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
