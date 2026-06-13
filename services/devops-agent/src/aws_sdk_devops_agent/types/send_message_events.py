"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageEvents``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError, SerializationError

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


class _SendMessageEvents_responseCreated(TypedDict):
    responseCreated: "aws_sdk_devops_agent.types.send_message_response_created_event.SendMessageResponseCreatedEvent"


class _SendMessageEvents_responseInProgress(TypedDict):
    responseInProgress: "aws_sdk_devops_agent.types.send_message_response_in_progress_event.SendMessageResponseInProgressEvent"


class _SendMessageEvents_responseCompleted(TypedDict):
    responseCompleted: "aws_sdk_devops_agent.types.send_message_response_completed_event.SendMessageResponseCompletedEvent"


class _SendMessageEvents_responseFailed(TypedDict):
    responseFailed: "aws_sdk_devops_agent.types.send_message_response_failed_event.SendMessageResponseFailedEvent"


class _SendMessageEvents_summary(TypedDict):
    summary: (
        "aws_sdk_devops_agent.types.send_message_summary_event.SendMessageSummaryEvent"
    )


class _SendMessageEvents_heartbeat(TypedDict):
    heartbeat: "aws_sdk_devops_agent.types.send_message_heartbeat_event.SendMessageHeartbeatEvent"


class _SendMessageEvents_contentBlockStart(TypedDict):
    contentBlockStart: "aws_sdk_devops_agent.types.send_message_content_block_start_event.SendMessageContentBlockStartEvent"


class _SendMessageEvents_contentBlockDelta(TypedDict):
    contentBlockDelta: "aws_sdk_devops_agent.types.send_message_content_block_delta_event.SendMessageContentBlockDeltaEvent"


class _SendMessageEvents_contentBlockStop(TypedDict):
    contentBlockStop: "aws_sdk_devops_agent.types.send_message_content_block_stop_event.SendMessageContentBlockStopEvent"


SendMessageEvents: TypeAlias = (
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


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageEvents) -> dict:
    if "responseCreated" in value:
        import aws_sdk_devops_agent.types.send_message_response_created_event

        return {
            "responseCreated": aws_sdk_devops_agent.types.send_message_response_created_event.serialize_json(
                value["responseCreated"]
            )
        }
    elif "responseInProgress" in value:
        import aws_sdk_devops_agent.types.send_message_response_in_progress_event

        return {
            "responseInProgress": aws_sdk_devops_agent.types.send_message_response_in_progress_event.serialize_json(
                value["responseInProgress"]
            )
        }
    elif "responseCompleted" in value:
        import aws_sdk_devops_agent.types.send_message_response_completed_event

        return {
            "responseCompleted": aws_sdk_devops_agent.types.send_message_response_completed_event.serialize_json(
                value["responseCompleted"]
            )
        }
    elif "responseFailed" in value:
        import aws_sdk_devops_agent.types.send_message_response_failed_event

        return {
            "responseFailed": aws_sdk_devops_agent.types.send_message_response_failed_event.serialize_json(
                value["responseFailed"]
            )
        }
    elif "summary" in value:
        import aws_sdk_devops_agent.types.send_message_summary_event

        return {
            "summary": aws_sdk_devops_agent.types.send_message_summary_event.serialize_json(
                value["summary"]
            )
        }
    elif "heartbeat" in value:
        import aws_sdk_devops_agent.types.send_message_heartbeat_event

        return {
            "heartbeat": aws_sdk_devops_agent.types.send_message_heartbeat_event.serialize_json(
                value["heartbeat"]
            )
        }
    elif "contentBlockStart" in value:
        import aws_sdk_devops_agent.types.send_message_content_block_start_event

        return {
            "contentBlockStart": aws_sdk_devops_agent.types.send_message_content_block_start_event.serialize_json(
                value["contentBlockStart"]
            )
        }
    elif "contentBlockDelta" in value:
        import aws_sdk_devops_agent.types.send_message_content_block_delta_event

        return {
            "contentBlockDelta": aws_sdk_devops_agent.types.send_message_content_block_delta_event.serialize_json(
                value["contentBlockDelta"]
            )
        }
    elif "contentBlockStop" in value:
        import aws_sdk_devops_agent.types.send_message_content_block_stop_event

        return {
            "contentBlockStop": aws_sdk_devops_agent.types.send_message_content_block_stop_event.serialize_json(
                value["contentBlockStop"]
            )
        }
    else:
        raise SerializationError("SendMessageEvents: no variant present")


def deserialize_json(data: dict) -> SendMessageEvents:
    if "responseCreated" in data:
        import aws_sdk_devops_agent.types.send_message_response_created_event

        return {
            "responseCreated": aws_sdk_devops_agent.types.send_message_response_created_event.deserialize_json(
                data["responseCreated"]
            )
        }
    elif "responseInProgress" in data:
        import aws_sdk_devops_agent.types.send_message_response_in_progress_event

        return {
            "responseInProgress": aws_sdk_devops_agent.types.send_message_response_in_progress_event.deserialize_json(
                data["responseInProgress"]
            )
        }
    elif "responseCompleted" in data:
        import aws_sdk_devops_agent.types.send_message_response_completed_event

        return {
            "responseCompleted": aws_sdk_devops_agent.types.send_message_response_completed_event.deserialize_json(
                data["responseCompleted"]
            )
        }
    elif "responseFailed" in data:
        import aws_sdk_devops_agent.types.send_message_response_failed_event

        return {
            "responseFailed": aws_sdk_devops_agent.types.send_message_response_failed_event.deserialize_json(
                data["responseFailed"]
            )
        }
    elif "summary" in data:
        import aws_sdk_devops_agent.types.send_message_summary_event

        return {
            "summary": aws_sdk_devops_agent.types.send_message_summary_event.deserialize_json(
                data["summary"]
            )
        }
    elif "heartbeat" in data:
        import aws_sdk_devops_agent.types.send_message_heartbeat_event

        return {
            "heartbeat": aws_sdk_devops_agent.types.send_message_heartbeat_event.deserialize_json(
                data["heartbeat"]
            )
        }
    elif "contentBlockStart" in data:
        import aws_sdk_devops_agent.types.send_message_content_block_start_event

        return {
            "contentBlockStart": aws_sdk_devops_agent.types.send_message_content_block_start_event.deserialize_json(
                data["contentBlockStart"]
            )
        }
    elif "contentBlockDelta" in data:
        import aws_sdk_devops_agent.types.send_message_content_block_delta_event

        return {
            "contentBlockDelta": aws_sdk_devops_agent.types.send_message_content_block_delta_event.deserialize_json(
                data["contentBlockDelta"]
            )
        }
    elif "contentBlockStop" in data:
        import aws_sdk_devops_agent.types.send_message_content_block_stop_event

        return {
            "contentBlockStop": aws_sdk_devops_agent.types.send_message_content_block_stop_event.deserialize_json(
                data["contentBlockStop"]
            )
        }
    else:
        raise DeserializationError("SendMessageEvents: no recognized variant key")
