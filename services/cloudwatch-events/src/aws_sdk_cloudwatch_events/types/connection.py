"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#Connection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.connection_arn
    import aws_sdk_cloudwatch_events.types.connection_authorization_type
    import aws_sdk_cloudwatch_events.types.connection_name
    import aws_sdk_cloudwatch_events.types.connection_state
    import aws_sdk_cloudwatch_events.types.connection_state_reason
    import aws_sdk_cloudwatch_events.types.timestamp


class Connection(TypedDict):
    connection_arn: NotRequired[
        "aws_sdk_cloudwatch_events.types.connection_arn.ConnectionArn"
    ]
    """<p>The ARN of the connection.</p>"""
    name: NotRequired["aws_sdk_cloudwatch_events.types.connection_name.ConnectionName"]
    """<p>The name of the connection.</p>"""
    connection_state: NotRequired[
        "aws_sdk_cloudwatch_events.types.connection_state.ConnectionState"
    ]
    """<p>The state of the connection.</p>"""
    state_reason: NotRequired[
        "aws_sdk_cloudwatch_events.types.connection_state_reason.ConnectionStateReason"
    ]
    """<p>The reason that the connection is in the connection state.</p>"""
    authorization_type: NotRequired[
        "aws_sdk_cloudwatch_events.types.connection_authorization_type.ConnectionAuthorizationType"
    ]
    """<p>The authorization type specified for the connection.</p>"""
    creation_time: NotRequired["aws_sdk_cloudwatch_events.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the connection was created.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_cloudwatch_events.types.timestamp.Timestamp"
    ]
    """<p>A time stamp for the time that the connection was last modified.</p>"""
    last_authorized_time: NotRequired[
        "aws_sdk_cloudwatch_events.types.timestamp.Timestamp"
    ]
    """<p>A time stamp for the time that the connection was last authorized.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Connection) -> dict:
    out: dict = {}
    if "connection_arn" in value:
        out["ConnectionArn"] = value["connection_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "connection_state" in value:
        import aws_sdk_cloudwatch_events.types.connection_state

        out["ConnectionState"] = (
            aws_sdk_cloudwatch_events.types.connection_state.serialize_aws_json_1_1(
                value["connection_state"]
            )
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "authorization_type" in value:
        import aws_sdk_cloudwatch_events.types.connection_authorization_type

        out["AuthorizationType"] = (
            aws_sdk_cloudwatch_events.types.connection_authorization_type.serialize_aws_json_1_1(
                value["authorization_type"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_cloudwatch_events.types.timestamp

        out["CreationTime"] = (
            aws_sdk_cloudwatch_events.types.timestamp.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_cloudwatch_events.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_cloudwatch_events.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "last_authorized_time" in value:
        import aws_sdk_cloudwatch_events.types.timestamp

        out["LastAuthorizedTime"] = (
            aws_sdk_cloudwatch_events.types.timestamp.serialize_aws_json_1_1(
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
        import aws_sdk_cloudwatch_events.types.connection_state

        out["connection_state"] = (
            aws_sdk_cloudwatch_events.types.connection_state.deserialize_aws_json_1_1(
                data["ConnectionState"]
            )
        )
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    if "AuthorizationType" in data:
        import aws_sdk_cloudwatch_events.types.connection_authorization_type

        out["authorization_type"] = (
            aws_sdk_cloudwatch_events.types.connection_authorization_type.deserialize_aws_json_1_1(
                data["AuthorizationType"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_cloudwatch_events.types.timestamp

        out["creation_time"] = (
            aws_sdk_cloudwatch_events.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_cloudwatch_events.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_cloudwatch_events.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastAuthorizedTime" in data:
        import aws_sdk_cloudwatch_events.types.timestamp

        out["last_authorized_time"] = (
            aws_sdk_cloudwatch_events.types.timestamp.deserialize_aws_json_1_1(
                data["LastAuthorizedTime"]
            )
        )
    return out
