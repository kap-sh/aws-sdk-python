"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#DeauthorizeConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.connection_arn
    import capo_cloudwatch_events.types.connection_state
    import capo_cloudwatch_events.types.timestamp


class DeauthorizeConnectionResponse(TypedDict, closed=True):
    connection_arn: NotRequired[
        "capo_cloudwatch_events.types.connection_arn.ConnectionArn"
    ]
    """<p>The ARN of the connection that authorization was removed from.</p>"""
    connection_state: NotRequired[
        "capo_cloudwatch_events.types.connection_state.ConnectionState"
    ]
    """<p>The state of the connection.</p>"""
    creation_time: NotRequired["capo_cloudwatch_events.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the connection was created.</p>"""
    last_modified_time: NotRequired["capo_cloudwatch_events.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the connection was last updated.</p>"""
    last_authorized_time: NotRequired[
        "capo_cloudwatch_events.types.timestamp.Timestamp"
    ]
    """<p>A time stamp for the time that the connection was last authorized.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeauthorizeConnectionResponse) -> dict:
    out: dict = {}
    if "connection_arn" in value:
        out["ConnectionArn"] = value["connection_arn"]
    if "connection_state" in value:
        import capo_cloudwatch_events.types.connection_state

        out["ConnectionState"] = (
            capo_cloudwatch_events.types.connection_state.serialize_aws_json_1_1(
                value["connection_state"]
            )
        )
    if "creation_time" in value:
        import capo_cloudwatch_events.types.timestamp

        out["CreationTime"] = (
            capo_cloudwatch_events.types.timestamp.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import capo_cloudwatch_events.types.timestamp

        out["LastModifiedTime"] = (
            capo_cloudwatch_events.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "last_authorized_time" in value:
        import capo_cloudwatch_events.types.timestamp

        out["LastAuthorizedTime"] = (
            capo_cloudwatch_events.types.timestamp.serialize_aws_json_1_1(
                value["last_authorized_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeauthorizeConnectionResponse:
    out: DeauthorizeConnectionResponse = {}  # type: ignore[typeddict-item]
    if "ConnectionArn" in data:
        out["connection_arn"] = data["ConnectionArn"]
    if "ConnectionState" in data:
        import capo_cloudwatch_events.types.connection_state

        out["connection_state"] = (
            capo_cloudwatch_events.types.connection_state.deserialize_aws_json_1_1(
                data["ConnectionState"]
            )
        )
    if "CreationTime" in data:
        import capo_cloudwatch_events.types.timestamp

        out["creation_time"] = (
            capo_cloudwatch_events.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_cloudwatch_events.types.timestamp

        out["last_modified_time"] = (
            capo_cloudwatch_events.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastAuthorizedTime" in data:
        import capo_cloudwatch_events.types.timestamp

        out["last_authorized_time"] = (
            capo_cloudwatch_events.types.timestamp.deserialize_aws_json_1_1(
                data["LastAuthorizedTime"]
            )
        )
    return out
