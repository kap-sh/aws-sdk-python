"""Generated from Smithy shape ``com.amazonaws.appstream#Session``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.authentication_type
    import aws_sdk_appstream.types.instance_drain_status
    import aws_sdk_appstream.types.network_access_configuration
    import aws_sdk_appstream.types.session_connection_state
    import aws_sdk_appstream.types.session_state
    import aws_sdk_appstream.types.string
    import aws_sdk_appstream.types.timestamp
    import aws_sdk_appstream.types.user_id


class Session(TypedDict):
    id: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The identifier of the streaming session.</p>"""
    user_id: NotRequired["aws_sdk_appstream.types.user_id.UserId"]
    """<p>The identifier of the user for whom the session was created.</p>"""
    stack_name: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The name of the stack for the streaming session.</p>"""
    fleet_name: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The name of the fleet for the streaming session.</p>"""
    state: NotRequired["aws_sdk_appstream.types.session_state.SessionState"]
    """<p>The current state of the streaming session.</p>"""
    connection_state: NotRequired[
        "aws_sdk_appstream.types.session_connection_state.SessionConnectionState"
    ]
    """<p>Specifies whether a user is connected to the streaming session.</p>"""
    start_time: NotRequired["aws_sdk_appstream.types.timestamp.Timestamp"]
    """<p>The time when a streaming instance is dedicated for the user.</p>"""
    max_expiration_time: NotRequired["aws_sdk_appstream.types.timestamp.Timestamp"]
    """<p>The time when the streaming session is set to expire. This time is based on the <code>MaxUserDurationinSeconds</code> value, which determines the maximum length of time that a streaming session can run. A streaming session might end earlier than the time specified in <code>SessionMaxExpirationTime</code>, when the <code>DisconnectTimeOutInSeconds</code> elapses or the user chooses to end his or her session. If the <code>DisconnectTimeOutInSeconds</code> elapses, or the user chooses to end his or her session, the streaming instance is terminated and the streaming session ends.</p>"""
    authentication_type: NotRequired[
        "aws_sdk_appstream.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication method. The user is authenticated using a streaming URL (<code>API</code>) or SAML 2.0 federation (<code>SAML</code>).</p>"""
    network_access_configuration: NotRequired[
        "aws_sdk_appstream.types.network_access_configuration.NetworkAccessConfiguration"
    ]
    """<p>The network details for the streaming session.</p>"""
    instance_id: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The identifier for the instance hosting the session.</p>"""
    instance_drain_status: NotRequired[
        "aws_sdk_appstream.types.instance_drain_status.InstanceDrainStatus"
    ]
    """<p>The drain status of the instance hosting the streaming session. This only applies to multi-session fleets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Session) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    if "fleet_name" in value:
        out["FleetName"] = value["fleet_name"]
    if "state" in value:
        import aws_sdk_appstream.types.session_state

        out["State"] = aws_sdk_appstream.types.session_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "connection_state" in value:
        import aws_sdk_appstream.types.session_connection_state

        out["ConnectionState"] = (
            aws_sdk_appstream.types.session_connection_state.serialize_aws_json_1_1(
                value["connection_state"]
            )
        )
    if "start_time" in value:
        import aws_sdk_appstream.types.timestamp

        out["StartTime"] = aws_sdk_appstream.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "max_expiration_time" in value:
        import aws_sdk_appstream.types.timestamp

        out["MaxExpirationTime"] = (
            aws_sdk_appstream.types.timestamp.serialize_aws_json_1_1(
                value["max_expiration_time"]
            )
        )
    if "authentication_type" in value:
        import aws_sdk_appstream.types.authentication_type

        out["AuthenticationType"] = (
            aws_sdk_appstream.types.authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    if "network_access_configuration" in value:
        import aws_sdk_appstream.types.network_access_configuration

        out["NetworkAccessConfiguration"] = (
            aws_sdk_appstream.types.network_access_configuration.serialize_aws_json_1_1(
                value["network_access_configuration"]
            )
        )
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "instance_drain_status" in value:
        import aws_sdk_appstream.types.instance_drain_status

        out["InstanceDrainStatus"] = (
            aws_sdk_appstream.types.instance_drain_status.serialize_aws_json_1_1(
                value["instance_drain_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Session:
    out: Session = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "StackName" in data:
        out["stack_name"] = data["StackName"]
    if "FleetName" in data:
        out["fleet_name"] = data["FleetName"]
    if "State" in data:
        import aws_sdk_appstream.types.session_state

        out["state"] = aws_sdk_appstream.types.session_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "ConnectionState" in data:
        import aws_sdk_appstream.types.session_connection_state

        out["connection_state"] = (
            aws_sdk_appstream.types.session_connection_state.deserialize_aws_json_1_1(
                data["ConnectionState"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_appstream.types.timestamp

        out["start_time"] = aws_sdk_appstream.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "MaxExpirationTime" in data:
        import aws_sdk_appstream.types.timestamp

        out["max_expiration_time"] = (
            aws_sdk_appstream.types.timestamp.deserialize_aws_json_1_1(
                data["MaxExpirationTime"]
            )
        )
    if "AuthenticationType" in data:
        import aws_sdk_appstream.types.authentication_type

        out["authentication_type"] = (
            aws_sdk_appstream.types.authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    if "NetworkAccessConfiguration" in data:
        import aws_sdk_appstream.types.network_access_configuration

        out["network_access_configuration"] = (
            aws_sdk_appstream.types.network_access_configuration.deserialize_aws_json_1_1(
                data["NetworkAccessConfiguration"]
            )
        )
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "InstanceDrainStatus" in data:
        import aws_sdk_appstream.types.instance_drain_status

        out["instance_drain_status"] = (
            aws_sdk_appstream.types.instance_drain_status.deserialize_aws_json_1_1(
                data["InstanceDrainStatus"]
            )
        )
    return out
