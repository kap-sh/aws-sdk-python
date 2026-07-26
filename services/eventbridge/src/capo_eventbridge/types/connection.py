"""Generated from Smithy shape ``com.amazonaws.eventbridge#Connection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.connection_arn
    import capo_eventbridge.types.connection_authorization_type
    import capo_eventbridge.types.connection_name
    import capo_eventbridge.types.connection_state
    import capo_eventbridge.types.connection_state_reason
    import capo_eventbridge.types.timestamp


class Connection(TypedDict, closed=True):
    connection_arn: NotRequired["capo_eventbridge.types.connection_arn.ConnectionArn"]
    """<p>The ARN of the connection.</p>"""
    name: NotRequired["capo_eventbridge.types.connection_name.ConnectionName"]
    """<p>The name of the connection.</p>"""
    connection_state: NotRequired[
        "capo_eventbridge.types.connection_state.ConnectionState"
    ]
    """<p>The state of the connection.</p>"""
    state_reason: NotRequired[
        "capo_eventbridge.types.connection_state_reason.ConnectionStateReason"
    ]
    """<p>The reason that the connection is in the connection state.</p>"""
    authorization_type: NotRequired[
        "capo_eventbridge.types.connection_authorization_type.ConnectionAuthorizationType"
    ]
    """<p>The authorization type specified for the connection.</p> <note> <p>OAUTH tokens are refreshed when a 401 or 407 response is returned.</p> </note>"""
    creation_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the connection was created.</p>"""
    last_modified_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the connection was last modified.</p>"""
    last_authorized_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the connection was last authorized.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Connection) -> dict:
    out: dict = {}
    if "connection_arn" in value:
        out["ConnectionArn"] = value["connection_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "connection_state" in value:
        import capo_eventbridge.types.connection_state

        out["ConnectionState"] = (
            capo_eventbridge.types.connection_state.serialize_aws_json_1_1(
                value["connection_state"]
            )
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "authorization_type" in value:
        import capo_eventbridge.types.connection_authorization_type

        out["AuthorizationType"] = (
            capo_eventbridge.types.connection_authorization_type.serialize_aws_json_1_1(
                value["authorization_type"]
            )
        )
    if "creation_time" in value:
        import capo_eventbridge.types.timestamp

        out["CreationTime"] = capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_eventbridge.types.timestamp

        out["LastModifiedTime"] = (
            capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "last_authorized_time" in value:
        import capo_eventbridge.types.timestamp

        out["LastAuthorizedTime"] = (
            capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["last_authorized_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Connection:
    out: Connection = {}  # type: ignore[typeddict-item]
    if "ConnectionArn" in data:
        out["connection_arn"] = data["ConnectionArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ConnectionState" in data:
        import capo_eventbridge.types.connection_state

        out["connection_state"] = (
            capo_eventbridge.types.connection_state.deserialize_aws_json_1_1(
                data["ConnectionState"]
            )
        )
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    if "AuthorizationType" in data:
        import capo_eventbridge.types.connection_authorization_type

        out["authorization_type"] = (
            capo_eventbridge.types.connection_authorization_type.deserialize_aws_json_1_1(
                data["AuthorizationType"]
            )
        )
    if "CreationTime" in data:
        import capo_eventbridge.types.timestamp

        out["creation_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_eventbridge.types.timestamp

        out["last_modified_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastAuthorizedTime" in data:
        import capo_eventbridge.types.timestamp

        out["last_authorized_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["LastAuthorizedTime"]
            )
        )
    return out
