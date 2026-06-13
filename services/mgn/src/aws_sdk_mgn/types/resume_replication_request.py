"""Generated from Smithy shape ``com.amazonaws.mgn#ResumeReplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.source_server_id


class ResumeReplicationRequest(TypedDict):
    source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID"
    """<p>Resume Replication Request source server ID.</p>"""
    account_id: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>Resume Replication Request account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResumeReplicationRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> ResumeReplicationRequest:
    out: ResumeReplicationRequest = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    else:
        raise DeserializationError("ResumeReplicationRequest.source_server_id required")
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
