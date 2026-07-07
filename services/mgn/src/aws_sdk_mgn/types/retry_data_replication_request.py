"""Generated from Smithy shape ``com.amazonaws.mgn#RetryDataReplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.source_server_id


class RetryDataReplicationRequest(TypedDict, closed=True):
    source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID"
    """<p>Retry data replication for Source Server ID.</p>"""
    account_id: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>Retry data replication for Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetryDataReplicationRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> RetryDataReplicationRequest:
    out: RetryDataReplicationRequest = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    else:
        raise DeserializationError(
            "RetryDataReplicationRequest.source_server_id required"
        )
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
