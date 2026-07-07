"""Generated from Smithy shape ``com.amazonaws.s3#SelectObjectContentEventStream``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_s3._iter import AnyIterator
from aws_sdk_s3._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_s3.types.continuation_event
    import aws_sdk_s3.types.end_event
    import aws_sdk_s3.types.progress_event
    import aws_sdk_s3.types.records_event
    import aws_sdk_s3.types.stats_event


class _SelectObjectContentEventStream_Records(TypedDict, closed=True):
    Records: "aws_sdk_s3.types.records_event.RecordsEvent"


class _SelectObjectContentEventStream_Stats(TypedDict, closed=True):
    Stats: "aws_sdk_s3.types.stats_event.StatsEvent"


class _SelectObjectContentEventStream_Progress(TypedDict, closed=True):
    Progress: "aws_sdk_s3.types.progress_event.ProgressEvent"


class _SelectObjectContentEventStream_Cont(TypedDict, closed=True):
    Cont: "aws_sdk_s3.types.continuation_event.ContinuationEvent"


class _SelectObjectContentEventStream_End(TypedDict, closed=True):
    End: "aws_sdk_s3.types.end_event.EndEvent"


_SelectObjectContentEventStream: TypeAlias = (
    _SelectObjectContentEventStream_Records
    | _SelectObjectContentEventStream_Stats
    | _SelectObjectContentEventStream_Progress
    | _SelectObjectContentEventStream_Cont
    | _SelectObjectContentEventStream_End
)
SelectObjectContentEventStream: TypeAlias = AnyIterator[_SelectObjectContentEventStream]


def serialize_event_xml(value: _SelectObjectContentEventStream) -> bytes:
    match value:
        case {"Records": payload}:
            import aws_sdk_s3.types.records_event

            return aws_sdk_s3.types.records_event.serialize_event_xml(payload)
        case {"Stats": payload}:
            import aws_sdk_s3.types.stats_event

            return aws_sdk_s3.types.stats_event.serialize_event_xml(payload)
        case {"Progress": payload}:
            import aws_sdk_s3.types.progress_event

            return aws_sdk_s3.types.progress_event.serialize_event_xml(payload)
        case {"Cont": payload}:
            import aws_sdk_s3.types.continuation_event

            return aws_sdk_s3.types.continuation_event.serialize_event_xml(payload)
        case {"End": payload}:
            import aws_sdk_s3.types.end_event

            return aws_sdk_s3.types.end_event.serialize_event_xml(payload)
        case _:
            raise ValueError(
                f"SelectObjectContentEventStream: unrecognized variant {value!r}"
            )


def deserialize_event_xml(message: Message) -> _SelectObjectContentEventStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    event_type = headers.get(":event-type")
    match event_type:
        case "Records":
            import aws_sdk_s3.types.records_event

            return {
                "Records": aws_sdk_s3.types.records_event.deserialize_event_xml(message)
            }
        case "Stats":
            import aws_sdk_s3.types.stats_event

            return {
                "Stats": aws_sdk_s3.types.stats_event.deserialize_event_xml(message)
            }
        case "Progress":
            import aws_sdk_s3.types.progress_event

            return {
                "Progress": aws_sdk_s3.types.progress_event.deserialize_event_xml(
                    message
                )
            }
        case "Cont":
            import aws_sdk_s3.types.continuation_event

            return {
                "Cont": aws_sdk_s3.types.continuation_event.deserialize_event_xml(
                    message
                )
            }
        case "End":
            import aws_sdk_s3.types.end_event

            return {"End": aws_sdk_s3.types.end_event.deserialize_event_xml(message)}
        case _:
            raise ValueError(
                f"SelectObjectContentEventStream: unrecognized event-type {event_type!r}"
            )
