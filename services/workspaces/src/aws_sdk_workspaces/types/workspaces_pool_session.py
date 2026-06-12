"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesPoolSession``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.amazon_uuid
    import aws_sdk_workspaces.types.authentication_type
    import aws_sdk_workspaces.types.network_access_configuration
    import aws_sdk_workspaces.types.session_connection_state
    import aws_sdk_workspaces.types.session_instance_id
    import aws_sdk_workspaces.types.timestamp
    import aws_sdk_workspaces.types.workspaces_pool_id
    import aws_sdk_workspaces.types.workspaces_pool_user_id


class WorkspacesPoolSession(TypedDict):
    authentication_type: NotRequired[
        "aws_sdk_workspaces.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication method. The user is authenticated using a WorkSpaces Pools URL (API) or SAML 2.0 federation (SAML).</p>"""
    connection_state: NotRequired[
        "aws_sdk_workspaces.types.session_connection_state.SessionConnectionState"
    ]
    """<p>Specifies whether a user is connected to the pool session.</p>"""
    session_id: "aws_sdk_workspaces.types.amazon_uuid.AmazonUuid"
    """<p>The identifier of the session.</p>"""
    instance_id: NotRequired[
        "aws_sdk_workspaces.types.session_instance_id.SessionInstanceId"
    ]
    """<p>The identifier for the instance hosting the session.</p>"""
    pool_id: "aws_sdk_workspaces.types.workspaces_pool_id.WorkspacesPoolId"
    """<p>The identifier of the pool.</p>"""
    expiration_time: NotRequired["aws_sdk_workspaces.types.timestamp.Timestamp"]
    """<p>The time that the pool session ended.</p>"""
    network_access_configuration: NotRequired[
        "aws_sdk_workspaces.types.network_access_configuration.NetworkAccessConfiguration"
    ]
    """<p>Describes the network details of the pool.</p>"""
    start_time: NotRequired["aws_sdk_workspaces.types.timestamp.Timestamp"]
    """<p>The time that the pool sission started.</p>"""
    user_id: "aws_sdk_workspaces.types.workspaces_pool_user_id.WorkspacesPoolUserId"
    """<p>The identifier of the user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspacesPoolSession) -> dict:
    out: dict = {}
    if "authentication_type" in value:
        import aws_sdk_workspaces.types.authentication_type

        out["AuthenticationType"] = (
            aws_sdk_workspaces.types.authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    if "connection_state" in value:
        import aws_sdk_workspaces.types.session_connection_state

        out["ConnectionState"] = (
            aws_sdk_workspaces.types.session_connection_state.serialize_aws_json_1_1(
                value["connection_state"]
            )
        )
    out["SessionId"] = value["session_id"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    out["PoolId"] = value["pool_id"]
    if "expiration_time" in value:
        import aws_sdk_workspaces.types.timestamp

        out["ExpirationTime"] = (
            aws_sdk_workspaces.types.timestamp.serialize_aws_json_1_1(
                value["expiration_time"]
            )
        )
    if "network_access_configuration" in value:
        import aws_sdk_workspaces.types.network_access_configuration

        out["NetworkAccessConfiguration"] = (
            aws_sdk_workspaces.types.network_access_configuration.serialize_aws_json_1_1(
                value["network_access_configuration"]
            )
        )
    if "start_time" in value:
        import aws_sdk_workspaces.types.timestamp

        out["StartTime"] = aws_sdk_workspaces.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    out["UserId"] = value["user_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspacesPoolSession:
    out: WorkspacesPoolSession = {}  # type: ignore[typeddict-item]
    if "AuthenticationType" in data:
        import aws_sdk_workspaces.types.authentication_type

        out["authentication_type"] = (
            aws_sdk_workspaces.types.authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    if "ConnectionState" in data:
        import aws_sdk_workspaces.types.session_connection_state

        out["connection_state"] = (
            aws_sdk_workspaces.types.session_connection_state.deserialize_aws_json_1_1(
                data["ConnectionState"]
            )
        )
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    else:
        raise DeserializationError("WorkspacesPoolSession.session_id required")
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "PoolId" in data:
        out["pool_id"] = data["PoolId"]
    else:
        raise DeserializationError("WorkspacesPoolSession.pool_id required")
    if "ExpirationTime" in data:
        import aws_sdk_workspaces.types.timestamp

        out["expiration_time"] = (
            aws_sdk_workspaces.types.timestamp.deserialize_aws_json_1_1(
                data["ExpirationTime"]
            )
        )
    if "NetworkAccessConfiguration" in data:
        import aws_sdk_workspaces.types.network_access_configuration

        out["network_access_configuration"] = (
            aws_sdk_workspaces.types.network_access_configuration.deserialize_aws_json_1_1(
                data["NetworkAccessConfiguration"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_workspaces.types.timestamp

        out["start_time"] = aws_sdk_workspaces.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("WorkspacesPoolSession.user_id required")
    return out
