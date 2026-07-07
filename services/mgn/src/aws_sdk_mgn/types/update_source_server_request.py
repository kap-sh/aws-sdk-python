"""Generated from Smithy shape ``com.amazonaws.mgn#UpdateSourceServerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.source_server_connector_action
    import aws_sdk_mgn.types.source_server_id


class UpdateSourceServerRequest(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>Update Source Server request account ID.</p>"""
    source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID"
    """<p>Update Source Server request source server ID.</p>"""
    connector_action: NotRequired[
        "aws_sdk_mgn.types.source_server_connector_action.SourceServerConnectorAction"
    ]
    """<p>Update Source Server request connector action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSourceServerRequest) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    out["sourceServerID"] = value["source_server_id"]
    if "connector_action" in value:
        import aws_sdk_mgn.types.source_server_connector_action

        out["connectorAction"] = (
            aws_sdk_mgn.types.source_server_connector_action.serialize_json(
                value["connector_action"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSourceServerRequest:
    out: UpdateSourceServerRequest = {}  # type: ignore[typeddict-item]
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    else:
        raise DeserializationError(
            "UpdateSourceServerRequest.source_server_id required"
        )
    if "connectorAction" in data:
        import aws_sdk_mgn.types.source_server_connector_action

        out["connector_action"] = (
            aws_sdk_mgn.types.source_server_connector_action.deserialize_json(
                data["connectorAction"]
            )
        )
    return out
