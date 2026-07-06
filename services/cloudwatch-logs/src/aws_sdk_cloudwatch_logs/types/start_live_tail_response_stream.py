"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#StartLiveTailResponseStream``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_cloudwatch_logs._iter import AnyIterator
from aws_sdk_cloudwatch_logs._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.errors.session_streaming_exception
    import aws_sdk_cloudwatch_logs.errors.session_timeout_exception
    import aws_sdk_cloudwatch_logs.types.live_tail_session_start
    import aws_sdk_cloudwatch_logs.types.live_tail_session_update


class _StartLiveTailResponseStream_sessionStart(TypedDict, closed=True):
    sessionStart: (
        "aws_sdk_cloudwatch_logs.types.live_tail_session_start.LiveTailSessionStart"
    )


class _StartLiveTailResponseStream_sessionUpdate(TypedDict, closed=True):
    sessionUpdate: (
        "aws_sdk_cloudwatch_logs.types.live_tail_session_update.LiveTailSessionUpdate"
    )


class _StartLiveTailResponseStream_SessionTimeoutException(TypedDict, closed=True):
    SessionTimeoutException: "aws_sdk_cloudwatch_logs.errors.session_timeout_exception.SessionTimeoutException_"


class _StartLiveTailResponseStream_SessionStreamingException(TypedDict, closed=True):
    SessionStreamingException: "aws_sdk_cloudwatch_logs.errors.session_streaming_exception.SessionStreamingException_"


_StartLiveTailResponseStream: TypeAlias = (
    _StartLiveTailResponseStream_sessionStart
    | _StartLiveTailResponseStream_sessionUpdate
    | _StartLiveTailResponseStream_SessionTimeoutException
    | _StartLiveTailResponseStream_SessionStreamingException
)
StartLiveTailResponseStream: TypeAlias = AnyIterator[_StartLiveTailResponseStream]


def serialize_event_aws_json_1_1(value: _StartLiveTailResponseStream) -> bytes:
    match value:
        case {"sessionStart": payload}:
            import aws_sdk_cloudwatch_logs.types.live_tail_session_start

            return aws_sdk_cloudwatch_logs.types.live_tail_session_start.serialize_event_aws_json_1_1(
                payload
            )
        case {"sessionUpdate": payload}:
            import aws_sdk_cloudwatch_logs.types.live_tail_session_update

            return aws_sdk_cloudwatch_logs.types.live_tail_session_update.serialize_event_aws_json_1_1(
                payload
            )
        case {"SessionTimeoutException": payload}:
            import aws_sdk_cloudwatch_logs.errors.session_timeout_exception

            return aws_sdk_cloudwatch_logs.errors.session_timeout_exception.serialize_event_aws_json_1_1(
                payload
            )
        case {"SessionStreamingException": payload}:
            import aws_sdk_cloudwatch_logs.errors.session_streaming_exception

            return aws_sdk_cloudwatch_logs.errors.session_streaming_exception.serialize_event_aws_json_1_1(
                payload
            )
        case _:
            raise ValueError(
                f"StartLiveTailResponseStream: unrecognized variant {value!r}"
            )


def deserialize_event_aws_json_1_1(message: Message) -> _StartLiveTailResponseStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    if message_type == "error":
        error_type = headers.get(":error-type")
        match error_type:
            case "SessionTimeoutException":
                import aws_sdk_cloudwatch_logs.errors.session_timeout_exception

                raise aws_sdk_cloudwatch_logs.errors.session_timeout_exception.SessionTimeoutException(
                    aws_sdk_cloudwatch_logs.errors.session_timeout_exception.deserialize_event_aws_json_1_1(
                        message
                    )
                )
            case "SessionStreamingException":
                import aws_sdk_cloudwatch_logs.errors.session_streaming_exception

                raise aws_sdk_cloudwatch_logs.errors.session_streaming_exception.SessionStreamingException(
                    aws_sdk_cloudwatch_logs.errors.session_streaming_exception.deserialize_event_aws_json_1_1(
                        message
                    )
                )
        raise ValueError(
            f"StartLiveTailResponseStream: unrecognized error-type {error_type!r}"
        )
    event_type = headers.get(":event-type")
    match event_type:
        case "sessionStart":
            import aws_sdk_cloudwatch_logs.types.live_tail_session_start

            return {
                "sessionStart": aws_sdk_cloudwatch_logs.types.live_tail_session_start.deserialize_event_aws_json_1_1(
                    message
                )
            }
        case "sessionUpdate":
            import aws_sdk_cloudwatch_logs.types.live_tail_session_update

            return {
                "sessionUpdate": aws_sdk_cloudwatch_logs.types.live_tail_session_update.deserialize_event_aws_json_1_1(
                    message
                )
            }
        case _:
            raise ValueError(
                f"StartLiveTailResponseStream: unrecognized event-type {event_type!r}"
            )
