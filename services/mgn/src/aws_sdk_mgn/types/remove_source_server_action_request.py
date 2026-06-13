"""Generated from Smithy shape ``com.amazonaws.mgn#RemoveSourceServerActionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.action_id
    import aws_sdk_mgn.types.source_server_id


class RemoveSourceServerActionRequest(TypedDict):
    source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID"
    """<p>Source server ID of the post migration custom action to remove.</p>"""
    action_id: "aws_sdk_mgn.types.action_id.ActionID"
    """<p>Source server post migration custom action ID to remove.</p>"""
    account_id: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>Source server post migration account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveSourceServerActionRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    out["actionID"] = value["action_id"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> RemoveSourceServerActionRequest:
    out: RemoveSourceServerActionRequest = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    else:
        raise DeserializationError(
            "RemoveSourceServerActionRequest.source_server_id required"
        )
    if "actionID" in data:
        out["action_id"] = data["actionID"]
    else:
        raise DeserializationError("RemoveSourceServerActionRequest.action_id required")
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
