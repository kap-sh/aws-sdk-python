"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#GetStreamSessionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_gameliftstreams.types.arn
    import aws_sdk_gameliftstreams.types.connection_timeout_seconds
    import aws_sdk_gameliftstreams.types.description
    import aws_sdk_gameliftstreams.types.environment_variables
    import aws_sdk_gameliftstreams.types.export_files_metadata
    import aws_sdk_gameliftstreams.types.file_location_uri
    import aws_sdk_gameliftstreams.types.game_launch_arg_list
    import aws_sdk_gameliftstreams.types.id
    import aws_sdk_gameliftstreams.types.location_name
    import aws_sdk_gameliftstreams.types.performance_stats_configuration
    import aws_sdk_gameliftstreams.types.protocol
    import aws_sdk_gameliftstreams.types.session_length_seconds
    import aws_sdk_gameliftstreams.types.signal_request
    import aws_sdk_gameliftstreams.types.signal_response
    import aws_sdk_gameliftstreams.types.stream_session_status
    import aws_sdk_gameliftstreams.types.stream_session_status_reason
    import aws_sdk_gameliftstreams.types.user_id
    import aws_sdk_gameliftstreams.types.web_sdk_protocol_url


class GetStreamSessionOutput(TypedDict):
    arn: NotRequired["aws_sdk_gameliftstreams.types.arn.Arn"]
    """<p>The <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> that's assigned to a stream session resource. When combined with the stream group resource ID, this value uniquely identifies the stream session across all Amazon Web Services Regions. Format is <code>arn:aws:gameliftstreams:[AWS Region]:[AWS account]:streamsession/[stream group resource ID]/[stream session resource ID]</code>.</p>"""
    description: NotRequired["aws_sdk_gameliftstreams.types.description.Description"]
    """<p>A human-readable label for the stream session. You can update this value at any time.</p>"""
    stream_group_id: NotRequired["aws_sdk_gameliftstreams.types.id.Id"]
    """<p>The unique identifier for the Amazon GameLift Streams stream group that is hosting the stream session. Format example: <code>sg-1AB2C3De4</code>.</p>"""
    user_id: NotRequired["aws_sdk_gameliftstreams.types.user_id.UserId"]
    """<p> An opaque, unique identifier for an end-user, defined by the developer. </p>"""
    status: NotRequired[
        "aws_sdk_gameliftstreams.types.stream_session_status.StreamSessionStatus"
    ]
    """<p>The current status of the stream session. A stream session is ready for a client to connect when in <code>ACTIVE</code> status.</p> <ul> <li> <p> <code>ACTIVATING</code>: The stream session is starting and preparing to stream.</p> </li> <li> <p> <code>ACTIVE</code>: The stream session is ready and waiting for a client connection. A client has <code>ConnectionTimeoutSeconds</code> (specified in <code>StartStreamSession</code>) from when the session reaches <code>ACTIVE</code> state to establish a connection. If no client connects within this timeframe, the session automatically terminates.</p> </li> <li> <p> <code>CONNECTED</code>: The stream session has a connected client. A session will automatically terminate if there is no user input for 60 minutes, or if the maximum length of a session specified by <code>SessionLengthSeconds</code> in <code>StartStreamSession</code> is exceeded.</p> </li> <li> <p> <code>ERROR</code>: The stream session failed to activate. See <code>StatusReason</code> (returned by <code>GetStreamSession</code> and <code>StartStreamSession</code>) for more information.</p> </li> <li> <p> <code>PENDING_CLIENT_RECONNECTION</code>: A client has recently disconnected and the stream session is waiting for the client to reconnect. A client has <code>ConnectionTimeoutSeconds</code> (specified in <code>StartStreamSession</code>) from when the session reaches <code>PENDING_CLIENT_RECONNECTION</code> state to re-establish a connection. If no client connects within this timeframe, the session automatically terminates.</p> </li> <li> <p> <code>RECONNECTING</code>: A client has initiated a reconnect to a session that was in <code>PENDING_CLIENT_RECONNECTION</code> state.</p> </li> <li> <p> <code>TERMINATING</code>: The stream session is ending.</p> </li> <li> <p> <code>TERMINATED</code>: The stream session has ended.</p> </li> </ul>"""
    status_reason: NotRequired[
        "aws_sdk_gameliftstreams.types.stream_session_status_reason.StreamSessionStatusReason"
    ]
    """<p>A short description of the reason the stream session is in <code>ERROR</code> status or <code>TERMINATED</code> status.</p> <p> <code>ERROR</code> status reasons:</p> <ul> <li> <p> <code>applicationLogS3DestinationError</code>: Could not write the application log to the Amazon S3 bucket that is configured for the streaming application. Make sure the bucket still exists.</p> </li> <li> <p> <code>internalError</code>: An internal service error occurred. Start a new stream session to continue streaming.</p> </li> <li> <p> <code>invalidSignalRequest</code>: The WebRTC signal request that was sent is not valid. When starting or reconnecting to a stream session, use <code>generateSignalRequest</code> in the Amazon GameLift Streams Web SDK to generate a new signal request.</p> </li> <li> <p> <code>placementTimeout</code>: Amazon GameLift Streams could not find available stream capacity to start a stream session. Increase the stream capacity in the stream group or wait until capacity becomes available.</p> </li> </ul> <p> <code>TERMINATED</code> status reasons:</p> <ul> <li> <p> <code>apiTerminated</code>: The stream session was terminated by an API call to <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TerminateStreamSession.html\">TerminateStreamSession</a>.</p> </li> <li> <p> <code>applicationExit</code>: The streaming application exited or crashed. The stream session was terminated because the application is no longer running.</p> </li> <li> <p> <code>connectionTimeout</code>: The stream session was terminated because the client failed to connect within the connection timeout period specified by <code>ConnectionTimeoutSeconds</code>.</p> </li> <li> <p> <code>maxSessionLengthTimeout</code>: The stream session was terminated because it exceeded the maximum session length timeout period specified by <code>SessionLengthSeconds</code>.</p> </li> <li> <p> <code>reconnectionTimeout</code>: The stream session was terminated because the client failed to reconnect within the reconnection timeout period specified by <code>ConnectionTimeoutSeconds</code> after losing connection.</p> </li> </ul>"""
    protocol: NotRequired["aws_sdk_gameliftstreams.types.protocol.Protocol"]
    """<p>The data transfer protocol in use with the stream session.</p>"""
    location: NotRequired["aws_sdk_gameliftstreams.types.location_name.LocationName"]
    """<p>The location where Amazon GameLift Streams hosts and streams your application. For example, <code>us-east-1</code>. For a complete list of locations that Amazon GameLift Streams supports, refer to <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html\">Regions, quotas, and limitations</a> in the <i>Amazon GameLift Streams Developer Guide</i>. </p>"""
    signal_request: NotRequired[
        "aws_sdk_gameliftstreams.types.signal_request.SignalRequest"
    ]
    """<p>The WebRTC ICE offer string that a client generates to initiate a connection to the stream session.</p>"""
    signal_response: NotRequired[
        "aws_sdk_gameliftstreams.types.signal_response.SignalResponse"
    ]
    """<p>The WebRTC answer string that the stream server generates in response to the <code>SignalRequest</code>.</p>"""
    connection_timeout_seconds: NotRequired[
        "aws_sdk_gameliftstreams.types.connection_timeout_seconds.ConnectionTimeoutSeconds"
    ]
    """<p>The length of time that Amazon GameLift Streams should wait for a client to connect or reconnect to the stream session. This time span starts when the stream session reaches <code>ACTIVE</code> or <code>PENDING_CLIENT_RECONNECTION</code> state. If no client connects (or reconnects) before the timeout, Amazon GameLift Streams terminates the stream session.</p>"""
    session_length_seconds: NotRequired[
        "aws_sdk_gameliftstreams.types.session_length_seconds.SessionLengthSeconds"
    ]
    """<p>The maximum duration of a session. Amazon GameLift Streams will automatically terminate a session after this amount of time has elapsed, regardless of any existing client connections.</p>"""
    additional_launch_args: NotRequired[
        "aws_sdk_gameliftstreams.types.game_launch_arg_list.GameLaunchArgList"
    ]
    """<p>A list of CLI arguments that are sent to the streaming server when a stream session launches. You can use this to configure the application or stream session details. You can also provide custom arguments that Amazon GameLift Streams passes to your game client.</p> <p> <code>AdditionalEnvironmentVariables</code> and <code>AdditionalLaunchArgs</code> have similar purposes. <code>AdditionalEnvironmentVariables</code> passes data using environment variables; while <code>AdditionalLaunchArgs</code> passes data using command-line arguments.</p>"""
    additional_environment_variables: NotRequired[
        "aws_sdk_gameliftstreams.types.environment_variables.EnvironmentVariables"
    ]
    """<p>A set of options that you can use to control the stream session runtime environment, expressed as a set of key-value pairs. You can use this to configure the application or stream session details. You can also provide custom environment variables that Amazon GameLift Streams passes to your game client.</p> <note> <p>If you want to debug your application with environment variables, we recommend that you do so in a local environment outside of Amazon GameLift Streams. For more information, refer to the Compatibility Guidance in the troubleshooting section of the Developer Guide.</p> </note> <p> <code>AdditionalEnvironmentVariables</code> and <code>AdditionalLaunchArgs</code> have similar purposes. <code>AdditionalEnvironmentVariables</code> passes data using environment variables; while <code>AdditionalLaunchArgs</code> passes data using command-line arguments.</p>"""
    performance_stats_configuration: NotRequired[
        "aws_sdk_gameliftstreams.types.performance_stats_configuration.PerformanceStatsConfiguration"
    ]
    """<p>The performance stats configuration for the stream session</p>"""
    log_file_location_uri: NotRequired[
        "aws_sdk_gameliftstreams.types.file_location_uri.FileLocationUri"
    ]
    """<p>Access location for log files that your content generates during a stream session. These log files are uploaded to cloud storage location at the end of a stream session. The Amazon GameLift Streams application resource defines which log files to upload.</p>"""
    web_sdk_protocol_url: NotRequired[
        "aws_sdk_gameliftstreams.types.web_sdk_protocol_url.WebSdkProtocolUrl"
    ]
    """<p>The URL of an S3 bucket that stores Amazon GameLift Streams WebSDK files. The URL is used to establish connection with the client.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>A timestamp that indicates when this resource was last updated. Timestamps are expressed using in ISO8601 format, such as: <code>2022-12-27T22:29:40+00:00</code> (UTC).</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: <code>2022-12-27T22:29:40+00:00</code> (UTC).</p>"""
    application_arn: NotRequired["aws_sdk_gameliftstreams.types.arn.Arn"]
    """<p>The application streaming in this session.</p> <p>This value is an <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. </p>"""
    export_files_metadata: NotRequired[
        "aws_sdk_gameliftstreams.types.export_files_metadata.ExportFilesMetadata"
    ]
    """<p>Provides details about the stream session's exported files. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStreamSessionOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "stream_group_id" in value:
        out["StreamGroupId"] = value["stream_group_id"]
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
    if "location" in value:
        out["Location"] = value["location"]
    if "signal_request" in value:
        out["SignalRequest"] = value["signal_request"]
    if "signal_response" in value:
        out["SignalResponse"] = value["signal_response"]
    if "connection_timeout_seconds" in value:
        out["ConnectionTimeoutSeconds"] = value["connection_timeout_seconds"]
    if "session_length_seconds" in value:
        out["SessionLengthSeconds"] = value["session_length_seconds"]
    if "additional_launch_args" in value:
        import aws_sdk_gameliftstreams.types.game_launch_arg_list

        out["AdditionalLaunchArgs"] = (
            aws_sdk_gameliftstreams.types.game_launch_arg_list.serialize_json(
                value["additional_launch_args"]
            )
        )
    if "additional_environment_variables" in value:
        import aws_sdk_gameliftstreams.types.environment_variables

        out["AdditionalEnvironmentVariables"] = (
            aws_sdk_gameliftstreams.types.environment_variables.serialize_json(
                value["additional_environment_variables"]
            )
        )
    if "performance_stats_configuration" in value:
        import aws_sdk_gameliftstreams.types.performance_stats_configuration

        out["PerformanceStatsConfiguration"] = (
            aws_sdk_gameliftstreams.types.performance_stats_configuration.serialize_json(
                value["performance_stats_configuration"]
            )
        )
    if "log_file_location_uri" in value:
        out["LogFileLocationUri"] = value["log_file_location_uri"]
    if "web_sdk_protocol_url" in value:
        out["WebSdkProtocolUrl"] = value["web_sdk_protocol_url"]
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
    return out


def deserialize_json(data: dict) -> GetStreamSessionOutput:
    out: GetStreamSessionOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "StreamGroupId" in data:
        out["stream_group_id"] = data["StreamGroupId"]
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
    if "Location" in data:
        out["location"] = data["Location"]
    if "SignalRequest" in data:
        out["signal_request"] = data["SignalRequest"]
    if "SignalResponse" in data:
        out["signal_response"] = data["SignalResponse"]
    if "ConnectionTimeoutSeconds" in data:
        out["connection_timeout_seconds"] = data["ConnectionTimeoutSeconds"]
    if "SessionLengthSeconds" in data:
        out["session_length_seconds"] = data["SessionLengthSeconds"]
    if "AdditionalLaunchArgs" in data:
        import aws_sdk_gameliftstreams.types.game_launch_arg_list

        out["additional_launch_args"] = (
            aws_sdk_gameliftstreams.types.game_launch_arg_list.deserialize_json(
                data["AdditionalLaunchArgs"]
            )
        )
    if "AdditionalEnvironmentVariables" in data:
        import aws_sdk_gameliftstreams.types.environment_variables

        out["additional_environment_variables"] = (
            aws_sdk_gameliftstreams.types.environment_variables.deserialize_json(
                data["AdditionalEnvironmentVariables"]
            )
        )
    if "PerformanceStatsConfiguration" in data:
        import aws_sdk_gameliftstreams.types.performance_stats_configuration

        out["performance_stats_configuration"] = (
            aws_sdk_gameliftstreams.types.performance_stats_configuration.deserialize_json(
                data["PerformanceStatsConfiguration"]
            )
        )
    if "LogFileLocationUri" in data:
        out["log_file_location_uri"] = data["LogFileLocationUri"]
    if "WebSdkProtocolUrl" in data:
        out["web_sdk_protocol_url"] = data["WebSdkProtocolUrl"]
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
    return out
