"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLogObjectResponseStream``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_cloudwatch_logs._iter import AnyIterator
from aws_sdk_cloudwatch_logs._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.errors.internal_streaming_exception
    import aws_sdk_cloudwatch_logs.types.fields_data


class _GetLogObjectResponseStream_fields(TypedDict, closed=True):
    fields: "aws_sdk_cloudwatch_logs.types.fields_data.FieldsData"


class _GetLogObjectResponseStream_InternalStreamingException(TypedDict, closed=True):
    InternalStreamingException: "aws_sdk_cloudwatch_logs.errors.internal_streaming_exception.InternalStreamingException_"


_GetLogObjectResponseStream: TypeAlias = (
    _GetLogObjectResponseStream_fields
    | _GetLogObjectResponseStream_InternalStreamingException
)
GetLogObjectResponseStream: TypeAlias = AnyIterator[_GetLogObjectResponseStream]


def serialize_event_aws_json_1_1(value: _GetLogObjectResponseStream) -> bytes:
    match value:
        case {"fields": payload}:
            import aws_sdk_cloudwatch_logs.types.fields_data

            return (
                aws_sdk_cloudwatch_logs.types.fields_data.serialize_event_aws_json_1_1(
                    payload
                )
            )
        case {"InternalStreamingException": payload}:
            import aws_sdk_cloudwatch_logs.errors.internal_streaming_exception

            return aws_sdk_cloudwatch_logs.errors.internal_streaming_exception.serialize_event_aws_json_1_1(
                payload
            )
        case _:
            raise ValueError(
                f"GetLogObjectResponseStream: unrecognized variant {value!r}"
            )


def deserialize_event_aws_json_1_1(message: Message) -> _GetLogObjectResponseStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    if message_type == "error":
        error_type = headers.get(":error-type")
        match error_type:
            case "InternalStreamingException":
                import aws_sdk_cloudwatch_logs.errors.internal_streaming_exception

                raise aws_sdk_cloudwatch_logs.errors.internal_streaming_exception.InternalStreamingException(
                    aws_sdk_cloudwatch_logs.errors.internal_streaming_exception.deserialize_event_aws_json_1_1(
                        message
                    )
                )
        raise ValueError(
            f"GetLogObjectResponseStream: unrecognized error-type {error_type!r}"
        )
    event_type = headers.get(":event-type")
    match event_type:
        case "fields":
            import aws_sdk_cloudwatch_logs.types.fields_data

            return {
                "fields": aws_sdk_cloudwatch_logs.types.fields_data.deserialize_event_aws_json_1_1(
                    message
                )
            }
        case _:
            raise ValueError(
                f"GetLogObjectResponseStream: unrecognized event-type {event_type!r}"
            )
