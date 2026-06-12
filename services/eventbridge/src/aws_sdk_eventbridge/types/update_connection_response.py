"""Generated from Smithy shape ``com.amazonaws.eventbridge#UpdateConnectionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.connection_arn
    import aws_sdk_eventbridge.types.connection_state
    import aws_sdk_eventbridge.types.timestamp


class UpdateConnectionResponse(TypedDict):
    connection_arn: NotRequired[
        "aws_sdk_eventbridge.types.connection_arn.ConnectionArn"
    ]
    """<p>The ARN of the connection that was updated.</p>"""
    connection_state: NotRequired[
        "aws_sdk_eventbridge.types.connection_state.ConnectionState"
    ]
    """<p>The state of the connection that was updated.</p>"""
    creation_time: NotRequired["aws_sdk_eventbridge.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the connection was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_eventbridge.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the connection was last modified.</p>"""
    last_authorized_time: NotRequired["aws_sdk_eventbridge.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the connection was last authorized.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateConnectionResponse) -> dict:
    out: dict = {}
    if "connection_arn" in value:
        out["ConnectionArn"] = value["connection_arn"]
    if "connection_state" in value:
        import aws_sdk_eventbridge.types.connection_state

        out["ConnectionState"] = (
            aws_sdk_eventbridge.types.connection_state.serialize_aws_json_1_1(
                value["connection_state"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_eventbridge.types.timestamp

        out["CreationTime"] = (
            aws_sdk_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_eventbridge.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "last_authorized_time" in value:
        import aws_sdk_eventbridge.types.timestamp

        out["LastAuthorizedTime"] = (
            aws_sdk_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["last_authorized_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateConnectionResponse:
    out: UpdateConnectionResponse = {}  # type: ignore[typeddict-item]
    if "ConnectionArn" in data:
        out["connection_arn"] = data["ConnectionArn"]
    if "ConnectionState" in data:
        import aws_sdk_eventbridge.types.connection_state

        out["connection_state"] = (
            aws_sdk_eventbridge.types.connection_state.deserialize_aws_json_1_1(
                data["ConnectionState"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_eventbridge.types.timestamp

        out["creation_time"] = (
            aws_sdk_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_eventbridge.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastAuthorizedTime" in data:
        import aws_sdk_eventbridge.types.timestamp

        out["last_authorized_time"] = (
            aws_sdk_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["LastAuthorizedTime"]
            )
        )
    return out
