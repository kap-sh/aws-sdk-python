"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#StartLiveTailResponseStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_cloudwatch_logs.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.live_tail_session_start
    import aws_sdk_cloudwatch_logs.errors.session_streaming_exception
    import aws_sdk_cloudwatch_logs.errors.session_timeout_exception
    import aws_sdk_cloudwatch_logs.types.live_tail_session_update


class _StartLiveTailResponseStream_sessionStart(TypedDict):
    sessionStart: (
        "aws_sdk_cloudwatch_logs.types.live_tail_session_start.LiveTailSessionStart"
    )


class _StartLiveTailResponseStream_sessionUpdate(TypedDict):
    sessionUpdate: (
        "aws_sdk_cloudwatch_logs.types.live_tail_session_update.LiveTailSessionUpdate"
    )


class _StartLiveTailResponseStream_SessionTimeoutException(TypedDict):
    SessionTimeoutException: "aws_sdk_cloudwatch_logs.errors.session_timeout_exception.SessionTimeoutException"


class _StartLiveTailResponseStream_SessionStreamingException(TypedDict):
    SessionStreamingException: "aws_sdk_cloudwatch_logs.errors.session_streaming_exception.SessionStreamingException"


StartLiveTailResponseStream: TypeAlias = (
    _StartLiveTailResponseStream_sessionStart
    | _StartLiveTailResponseStream_sessionUpdate
    | _StartLiveTailResponseStream_SessionTimeoutException
    | _StartLiveTailResponseStream_SessionStreamingException
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartLiveTailResponseStream) -> dict:
    if "sessionStart" in value:
        import aws_sdk_cloudwatch_logs.types.live_tail_session_start

        return {
            "sessionStart": aws_sdk_cloudwatch_logs.types.live_tail_session_start.serialize_aws_json_1_1(
                value["sessionStart"]
            )
        }
    elif "sessionUpdate" in value:
        import aws_sdk_cloudwatch_logs.types.live_tail_session_update

        return {
            "sessionUpdate": aws_sdk_cloudwatch_logs.types.live_tail_session_update.serialize_aws_json_1_1(
                value["sessionUpdate"]
            )
        }
    elif "SessionTimeoutException" in value:
        import aws_sdk_cloudwatch_logs.errors.session_timeout_exception

        return {
            "SessionTimeoutException": aws_sdk_cloudwatch_logs.errors.session_timeout_exception.serialize_aws_json_1_1(
                value["SessionTimeoutException"]
            )
        }
    elif "SessionStreamingException" in value:
        import aws_sdk_cloudwatch_logs.errors.session_streaming_exception

        return {
            "SessionStreamingException": aws_sdk_cloudwatch_logs.errors.session_streaming_exception.serialize_aws_json_1_1(
                value["SessionStreamingException"]
            )
        }
    else:
        raise SerializationError("StartLiveTailResponseStream: no variant present")


def deserialize_aws_json_1_1(data: dict) -> StartLiveTailResponseStream:
    if "sessionStart" in data:
        import aws_sdk_cloudwatch_logs.types.live_tail_session_start

        return {
            "sessionStart": aws_sdk_cloudwatch_logs.types.live_tail_session_start.deserialize_aws_json_1_1(
                data["sessionStart"]
            )
        }
    elif "sessionUpdate" in data:
        import aws_sdk_cloudwatch_logs.types.live_tail_session_update

        return {
            "sessionUpdate": aws_sdk_cloudwatch_logs.types.live_tail_session_update.deserialize_aws_json_1_1(
                data["sessionUpdate"]
            )
        }
    elif "SessionTimeoutException" in data:
        import aws_sdk_cloudwatch_logs.errors.session_timeout_exception

        return {
            "SessionTimeoutException": aws_sdk_cloudwatch_logs.errors.session_timeout_exception.deserialize_aws_json_1_1(
                data["SessionTimeoutException"]
            )
        }
    elif "SessionStreamingException" in data:
        import aws_sdk_cloudwatch_logs.errors.session_streaming_exception

        return {
            "SessionStreamingException": aws_sdk_cloudwatch_logs.errors.session_streaming_exception.deserialize_aws_json_1_1(
                data["SessionStreamingException"]
            )
        }
    else:
        raise DeserializationError(
            "StartLiveTailResponseStream: no recognized variant key"
        )
