"""Generated from Smithy shape ``com.amazonaws.mgn#DeleteSourceServerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.source_server_id


class DeleteSourceServerRequest(TypedDict):
    source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID"
    """<p>Request to delete Source Server from service by Server ID.</p>"""
    account_id: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>Request to delete Source Server from service by Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSourceServerRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> DeleteSourceServerRequest:
    out: DeleteSourceServerRequest = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    else:
        raise DeserializationError(
            "DeleteSourceServerRequest.source_server_id required"
        )
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
