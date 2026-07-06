"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#StreamSessionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_gameliftstreams.types.arn
    import aws_sdk_gameliftstreams.types.export_files_metadata
    import aws_sdk_gameliftstreams.types.location_name
    import aws_sdk_gameliftstreams.types.protocol
    import aws_sdk_gameliftstreams.types.stream_session_status
    import aws_sdk_gameliftstreams.types.stream_session_status_reason
    import aws_sdk_gameliftstreams.types.user_id


class StreamSessionSummary(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_gameliftstreams.types.arn.Arn"]
    r"""<p>An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> that uniquely identifies the stream session resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamsession/sg-1AB2C3De4/ABC123def4567</code>. </p>"""
    user_id: NotRequired["aws_sdk_gameliftstreams.types.user_id.UserId"]
    """<p> An opaque, unique identifier for an end-user, defined by the developer. </p>"""
    status: NotRequired[
        "aws_sdk_gameliftstreams.types.stream_session_status.StreamSessionStatus"
    ]
    """<p>The current status of the stream session resource.</p> <ul> <li> <p> <code>ACTIVATING</code>: The stream session is starting and preparing to stream.</p> </li> <li> <p> <code>ACTIVE</code>: The stream session is ready and waiting for a client connection. A client has <code>ConnectionTimeoutSeconds</code> (specified in <code>StartStreamSession</code>) from when the session reaches <code>ACTIVE</code> state to establish a connection. If no client connects within this timeframe, the session automatically terminates.</p> </li> <li> <p> <code>CONNECTED</code>: The stream session has a connected client. A session will automatically terminate if there is no user input for 60 minutes, or if the maximum length of a session specified by <code>SessionLengthSeconds</code> in <code>StartStreamSession</code> is exceeded.</p> </li> <li> <p> <code>ERROR</code>: The stream session failed to activate. See <code>StatusReason</code> (returned by <code>GetStreamSession</code> and <code>StartStreamSession</code>) for more information.</p> </li> <li> <p> <code>PENDING_CLIENT_RECONNECTION</code>: A client has recently disconnected and the stream session is waiting for the client to reconnect. A client has <code>ConnectionTimeoutSeconds</code> (specified in <code>StartStreamSession</code>) from when the session reaches <code>PENDING_CLIENT_RECONNECTION</code> state to re-establish a connection. If no client connects within this timeframe, the session automatically terminates.</p> </li> <li> <p> <code>RECONNECTING</code>: A client has initiated a reconnect to a session that was in <code>PENDING_CLIENT_RECONNECTION</code> state.</p> </li> <li> <p> <code>TERMINATING</code>: The stream session is ending.</p> </li> <li> <p> <code>TERMINATED</code>: The stream session has ended.</p> </li> </ul>"""
    status_reason: NotRequired[
        "aws_sdk_gameliftstreams.types.stream_session_status_reason.StreamSessionStatusReason"
    ]
    r"""<p>A short description of the reason the stream session is in <code>ERROR</code> status or <code>TERMINATED</code> status.</p> <p> <code>ERROR</code> status reasons:</p> <ul> <li> <p> <code>applicationLogS3DestinationError</code>: Could not write the application log to the Amazon S3 bucket that is configured for the streaming application. Make sure the bucket still exists.</p> </li> <li> <p> <code>internalError</code>: An internal service error occurred. Start a new stream session to continue streaming.</p> </li> <li> <p> <code>invalidSignalRequest</code>: The WebRTC signal request that was sent is not valid. When starting or reconnecting to a stream session, use <code>generateSignalRequest</code> in the Amazon GameLift Streams Web SDK to generate a new signal request.</p> </li> <li> <p> <code>placementTimeout</code>: Amazon GameLift Streams could not find available stream capacity to start a stream session. Increase the stream capacity in the stream group or wait until capacity becomes available.</p> </li> </ul> <p> <code>TERMINATED</code> status reasons:</p> <ul> <li> <p> <code>apiTerminated</code>: The stream session was terminated by an API call to <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TerminateStreamSession.html\">TerminateStreamSession</a>.</p> </li> <li> <p> <code>applicationExit</code>: The streaming application exited or crashed. The stream session was terminated because the application is no longer running.</p> </li> <li> <p> <code>connectionTimeout</code>: The stream session was terminated because the client failed to connect within the connection timeout period specified by <code>ConnectionTimeoutSeconds</code>.</p> </li> <li> <p> <code>maxSessionLengthTimeout</code>: The stream session was terminated because it exceeded the maximum session length timeout period specified by <code>SessionLengthSeconds</code>.</p> </li> <li> <p> <code>reconnectionTimeout</code>: The stream session was terminated because the client failed to reconnect within the reconnection timeout period specified by <code>ConnectionTimeoutSeconds</code> after losing connection.</p> </li> </ul>"""
    protocol: NotRequired["aws_sdk_gameliftstreams.types.protocol.Protocol"]
    """<p>The data transfer protocol in use with the stream session.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>A timestamp that indicates when this resource was last updated. Timestamps are expressed using in ISO8601 format, such as: <code>2022-12-27T22:29:40+00:00</code> (UTC).</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: <code>2022-12-27T22:29:40+00:00</code> (UTC).</p>"""
    application_arn: NotRequired["aws_sdk_gameliftstreams.types.arn.Arn"]
    r"""<p>An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. </p>"""
    export_files_metadata: NotRequired[
        "aws_sdk_gameliftstreams.types.export_files_metadata.ExportFilesMetadata"
    ]
    """<p>Provides details about the stream session's exported files. </p>"""
    location: NotRequired["aws_sdk_gameliftstreams.types.location_name.LocationName"]
    r"""<p>The location where Amazon GameLift Streams hosts and streams your application. For example, <code>us-east-1</code>. For a complete list of locations that Amazon GameLift Streams supports, refer to <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html\">Regions, quotas, and limitations</a> in the <i>Amazon GameLift Streams Developer Guide</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamSessionSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "status" in value:
        import aws_sdk_gameliftstreams.types.stream_session_status

        out["Status"] = (
            aws_sdk_gameliftstreams.types.stream_session_status.serialize_json(
                value["status"]
            )
        )
    if "status_reason" in value:
        import aws_sdk_gameliftstreams.types.stream_session_status_reason

        out["StatusReason"] = (
            aws_sdk_gameliftstreams.types.stream_session_status_reason.serialize_json(
                value["status_reason"]
            )
        )
    if "protocol" in value:
        import aws_sdk_gameliftstreams.types.protocol

        out["Protocol"] = aws_sdk_gameliftstreams.types.protocol.serialize_json(
            value["protocol"]
        )
    if "last_updated_at" in value:
        import aws_sdk_gameliftstreams.types._prelude.timestamp

        out["LastUpdatedAt"] = (
            aws_sdk_gameliftstreams.types._prelude.timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    if "created_at" in value:
        import aws_sdk_gameliftstreams.types._prelude.timestamp

        out["CreatedAt"] = (
            aws_sdk_gameliftstreams.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    if "export_files_metadata" in value:
        import aws_sdk_gameliftstreams.types.export_files_metadata

        out["ExportFilesMetadata"] = (
            aws_sdk_gameliftstreams.types.export_files_metadata.serialize_json(
                value["export_files_metadata"]
            )
        )
    if "location" in value:
        out["Location"] = value["location"]
    return out


def deserialize_json(data: dict) -> StreamSessionSummary:
    out: StreamSessionSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "Status" in data:
        import aws_sdk_gameliftstreams.types.stream_session_status

        out["status"] = (
            aws_sdk_gameliftstreams.types.stream_session_status.deserialize_json(
                data["Status"]
            )
        )
    if "StatusReason" in data:
        import aws_sdk_gameliftstreams.types.stream_session_status_reason

        out["status_reason"] = (
            aws_sdk_gameliftstreams.types.stream_session_status_reason.deserialize_json(
                data["StatusReason"]
            )
        )
    if "Protocol" in data:
        import aws_sdk_gameliftstreams.types.protocol

        out["protocol"] = aws_sdk_gameliftstreams.types.protocol.deserialize_json(
            data["Protocol"]
        )
    if "LastUpdatedAt" in data:
        import aws_sdk_gameliftstreams.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_gameliftstreams.types._prelude.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_gameliftstreams.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_gameliftstreams.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    if "ExportFilesMetadata" in data:
        import aws_sdk_gameliftstreams.types.export_files_metadata

        out["export_files_metadata"] = (
            aws_sdk_gameliftstreams.types.export_files_metadata.deserialize_json(
                data["ExportFilesMetadata"]
            )
        )
    if "Location" in data:
        out["location"] = data["Location"]
    return out
