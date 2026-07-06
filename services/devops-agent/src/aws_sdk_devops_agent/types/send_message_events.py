"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageEvents``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_devops_agent._iter import AnyIterator
from aws_sdk_devops_agent._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.send_message_content_block_delta_event
    import aws_sdk_devops_agent.types.send_message_content_block_start_event
    import aws_sdk_devops_agent.types.send_message_content_block_stop_event
    import aws_sdk_devops_agent.types.send_message_heartbeat_event
    import aws_sdk_devops_agent.types.send_message_response_completed_event
    import aws_sdk_devops_agent.types.send_message_response_created_event
    import aws_sdk_devops_agent.types.send_message_response_failed_event
    import aws_sdk_devops_agent.types.send_message_response_in_progress_event
    import aws_sdk_devops_agent.types.send_message_summary_event


class _SendMessageEvents_responseCreated(TypedDict, closed=True):
    responseCreated: "aws_sdk_devops_agent.types.send_message_response_created_event.SendMessageResponseCreatedEvent"


class _SendMessageEvents_responseInProgress(TypedDict, closed=True):
    responseInProgress: "aws_sdk_devops_agent.types.send_message_response_in_progress_event.SendMessageResponseInProgressEvent"


class _SendMessageEvents_responseCompleted(TypedDict, closed=True):
    responseCompleted: "aws_sdk_devops_agent.types.send_message_response_completed_event.SendMessageResponseCompletedEvent"


class _SendMessageEvents_responseFailed(TypedDict, closed=True):
    responseFailed: "aws_sdk_devops_agent.types.send_message_response_failed_event.SendMessageResponseFailedEvent"


class _SendMessageEvents_summary(TypedDict, closed=True):
    summary: (
        "aws_sdk_devops_agent.types.send_message_summary_event.SendMessageSummaryEvent"
    )


class _SendMessageEvents_heartbeat(TypedDict, closed=True):
    heartbeat: "aws_sdk_devops_agent.types.send_message_heartbeat_event.SendMessageHeartbeatEvent"


class _SendMessageEvents_contentBlockStart(TypedDict, closed=True):
    contentBlockStart: "aws_sdk_devops_agent.types.send_message_content_block_start_event.SendMessageContentBlockStartEvent"


class _SendMessageEvents_contentBlockDelta(TypedDict, closed=True):
    contentBlockDelta: "aws_sdk_devops_agent.types.send_message_content_block_delta_event.SendMessageContentBlockDeltaEvent"


class _SendMessageEvents_contentBlockStop(TypedDict, closed=True):
    contentBlockStop: "aws_sdk_devops_agent.types.send_message_content_block_stop_event.SendMessageContentBlockStopEvent"


_SendMessageEvents: TypeAlias = (
    _SendMessageEvents_responseCreated
    | _SendMessageEvents_responseInProgress
    | _SendMessageEvents_responseCompleted
    | _SendMessageEvents_responseFailed
    | _SendMessageEvents_summary
    | _SendMessageEvents_heartbeat
    | _SendMessageEvents_contentBlockStart
    | _SendMessageEvents_contentBlockDelta
    | _SendMessageEvents_contentBlockStop
)
SendMessageEvents: TypeAlias = AnyIterator[_SendMessageEvents]


def serialize_event_json(value: _SendMessageEvents) -> bytes:
    match value:
        case {"responseCreated": payload}:
            import aws_sdk_devops_agent.types.send_message_response_created_event

            return aws_sdk_devops_agent.types.send_message_response_created_event.serialize_event_json(
                payload
            )
        case {"responseInProgress": payload}:
            import aws_sdk_devops_agent.types.send_message_response_in_progress_event

            return aws_sdk_devops_agent.types.send_message_response_in_progress_event.serialize_event_json(
                payload
            )
        case {"responseCompleted": payload}:
            import aws_sdk_devops_agent.types.send_message_response_completed_event

            return aws_sdk_devops_agent.types.send_message_response_completed_event.serialize_event_json(
                payload
            )
        case {"responseFailed": payload}:
            import aws_sdk_devops_agent.types.send_message_response_failed_event

            return aws_sdk_devops_agent.types.send_message_response_failed_event.serialize_event_json(
                payload
            )
        case {"summary": payload}:
            import aws_sdk_devops_agent.types.send_message_summary_event

            return aws_sdk_devops_agent.types.send_message_summary_event.serialize_event_json(
                payload
            )
        case {"heartbeat": payload}:
            import aws_sdk_devops_agent.types.send_message_heartbeat_event

            return aws_sdk_devops_agent.types.send_message_heartbeat_event.serialize_event_json(
                payload
            )
        case {"contentBlockStart": payload}:
            import aws_sdk_devops_agent.types.send_message_content_block_start_event

            return aws_sdk_devops_agent.types.send_message_content_block_start_event.serialize_event_json(
                payload
            )
        case {"contentBlockDelta": payload}:
            import aws_sdk_devops_agent.types.send_message_content_block_delta_event

            return aws_sdk_devops_agent.types.send_message_content_block_delta_event.serialize_event_json(
                payload
            )
        case {"contentBlockStop": payload}:
            import aws_sdk_devops_agent.types.send_message_content_block_stop_event

            return aws_sdk_devops_agent.types.send_message_content_block_stop_event.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(f"SendMessageEvents: unrecognized variant {value!r}")


def deserialize_event_json(message: Message) -> _SendMessageEvents:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    event_type = headers.get(":event-type")
    match event_type:
        case "responseCreated":
            import aws_sdk_devops_agent.types.send_message_response_created_event

            return {
                "responseCreated": aws_sdk_devops_agent.types.send_message_response_created_event.deserialize_event_json(
                    message
                )
            }
        case "responseInProgress":
            import aws_sdk_devops_agent.types.send_message_response_in_progress_event

            return {
                "responseInProgress": aws_sdk_devops_agent.types.send_message_response_in_progress_event.deserialize_event_json(
                    message
                )
            }
        case "responseCompleted":
            import aws_sdk_devops_agent.types.send_message_response_completed_event

            return {
                "responseCompleted": aws_sdk_devops_agent.types.send_message_response_completed_event.deserialize_event_json(
                    message
                )
            }
        case "responseFailed":
            import aws_sdk_devops_agent.types.send_message_response_failed_event

            return {
                "responseFailed": aws_sdk_devops_agent.types.send_message_response_failed_event.deserialize_event_json(
                    message
                )
            }
        case "summary":
            import aws_sdk_devops_agent.types.send_message_summary_event

            return {
                "summary": aws_sdk_devops_agent.types.send_message_summary_event.deserialize_event_json(
                    message
                )
            }
        case "heartbeat":
            import aws_sdk_devops_agent.types.send_message_heartbeat_event

            return {
                "heartbeat": aws_sdk_devops_agent.types.send_message_heartbeat_event.deserialize_event_json(
                    message
                )
            }
        case "contentBlockStart":
            import aws_sdk_devops_agent.types.send_message_content_block_start_event

            return {
                "contentBlockStart": aws_sdk_devops_agent.types.send_message_content_block_start_event.deserialize_event_json(
                    message
                )
            }
        case "contentBlockDelta":
            import aws_sdk_devops_agent.types.send_message_content_block_delta_event

            return {
                "contentBlockDelta": aws_sdk_devops_agent.types.send_message_content_block_delta_event.deserialize_event_json(
                    message
                )
            }
        case "contentBlockStop":
            import aws_sdk_devops_agent.types.send_message_content_block_stop_event

            return {
                "contentBlockStop": aws_sdk_devops_agent.types.send_message_content_block_stop_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"SendMessageEvents: unrecognized event-type {event_type!r}"
            )
