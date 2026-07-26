"""Generated from Smithy shape ``com.amazonaws.mgn#UpdateSourceServerReplicationTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.replication_type
    import capo_mgn.types.source_server_id


class UpdateSourceServerReplicationTypeRequest(TypedDict, closed=True):
    source_server_id: "capo_mgn.types.source_server_id.SourceServerID"
    """<p>ID of source server on which to update replication type.</p>"""
    replication_type: "capo_mgn.types.replication_type.ReplicationType"
    """<p>Replication type to which to update source server.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Account ID on which to update replication type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSourceServerReplicationTypeRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    out["replicationType"] = value["replication_type"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> UpdateSourceServerReplicationTypeRequest:
    out: UpdateSourceServerReplicationTypeRequest = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    else:
        raise DeserializationError(
            "UpdateSourceServerReplicationTypeRequest.source_server_id required"
        )
    if "replicationType" in data:
        out["replication_type"] = data["replicationType"]
    else:
        raise DeserializationError(
            "UpdateSourceServerReplicationTypeRequest.replication_type required"
        )
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
