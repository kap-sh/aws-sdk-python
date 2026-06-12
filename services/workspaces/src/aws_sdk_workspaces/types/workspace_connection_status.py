"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceConnectionStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.connection_state
    import aws_sdk_workspaces.types.timestamp
    import aws_sdk_workspaces.types.workspace_id


class WorkspaceConnectionStatus(TypedDict):
    workspace_id: NotRequired["aws_sdk_workspaces.types.workspace_id.WorkspaceId"]
    """<p>The identifier of the WorkSpace.</p>"""
    connection_state: NotRequired[
        "aws_sdk_workspaces.types.connection_state.ConnectionState"
    ]
    """<p>The connection state of the WorkSpace. The connection state is unknown if the WorkSpace is stopped.</p>"""
    connection_state_check_timestamp: NotRequired[
        "aws_sdk_workspaces.types.timestamp.Timestamp"
    ]
    """<p>The timestamp of the connection status check.</p>"""
    last_known_user_connection_timestamp: NotRequired[
        "aws_sdk_workspaces.types.timestamp.Timestamp"
    ]
    """<p>The timestamp of the last known user connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceConnectionStatus) -> dict:
    out: dict = {}
    if "workspace_id" in value:
        out["WorkspaceId"] = value["workspace_id"]
    if "connection_state" in value:
        import aws_sdk_workspaces.types.connection_state

        out["ConnectionState"] = (
            aws_sdk_workspaces.types.connection_state.serialize_aws_json_1_1(
                value["connection_state"]
            )
        )
    if "connection_state_check_timestamp" in value:
        import aws_sdk_workspaces.types.timestamp

        out["ConnectionStateCheckTimestamp"] = (
            aws_sdk_workspaces.types.timestamp.serialize_aws_json_1_1(
                value["connection_state_check_timestamp"]
            )
        )
    if "last_known_user_connection_timestamp" in value:
        import aws_sdk_workspaces.types.timestamp

        out["LastKnownUserConnectionTimestamp"] = (
            aws_sdk_workspaces.types.timestamp.serialize_aws_json_1_1(
                value["last_known_user_connection_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspaceConnectionStatus:
    out: WorkspaceConnectionStatus = {}  # type: ignore[typeddict-item]
    if "WorkspaceId" in data:
        out["workspace_id"] = data["WorkspaceId"]
    if "ConnectionState" in data:
        import aws_sdk_workspaces.types.connection_state

        out["connection_state"] = (
            aws_sdk_workspaces.types.connection_state.deserialize_aws_json_1_1(
                data["ConnectionState"]
            )
        )
    if "ConnectionStateCheckTimestamp" in data:
        import aws_sdk_workspaces.types.timestamp

        out["connection_state_check_timestamp"] = (
            aws_sdk_workspaces.types.timestamp.deserialize_aws_json_1_1(
                data["ConnectionStateCheckTimestamp"]
            )
        )
    if "LastKnownUserConnectionTimestamp" in data:
        import aws_sdk_workspaces.types.timestamp

        out["last_known_user_connection_timestamp"] = (
            aws_sdk_workspaces.types.timestamp.deserialize_aws_json_1_1(
                data["LastKnownUserConnectionTimestamp"]
            )
        )
    return out
