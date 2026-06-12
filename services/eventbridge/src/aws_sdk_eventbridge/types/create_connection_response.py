"""Generated from Smithy shape ``com.amazonaws.eventbridge#CreateConnectionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.connection_arn
    import aws_sdk_eventbridge.types.connection_state
    import aws_sdk_eventbridge.types.timestamp


class CreateConnectionResponse(TypedDict):
    connection_arn: NotRequired[
        "aws_sdk_eventbridge.types.connection_arn.ConnectionArn"
    ]
    """<p>The ARN of the connection that was created by the request.</p>"""
    connection_state: NotRequired[
        "aws_sdk_eventbridge.types.connection_state.ConnectionState"
    ]
    """<p>The state of the connection that was created by the request.</p>"""
    creation_time: NotRequired["aws_sdk_eventbridge.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the connection was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_eventbridge.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the connection was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectionResponse) -> dict:
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
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConnectionResponse:
    out: CreateConnectionResponse = {}  # type: ignore[typeddict-item]
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
    return out
