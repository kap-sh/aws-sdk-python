"""Generated from Smithy shape ``com.amazonaws.mgn#StartReplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.source_server_id


class StartReplicationRequest(TypedDict):
    source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID"
    """<p>ID of source server on which to start replication.</p>"""
    account_id: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>Account ID on which to start replication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartReplicationRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> StartReplicationRequest:
    out: StartReplicationRequest = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    else:
        raise DeserializationError("StartReplicationRequest.source_server_id required")
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
