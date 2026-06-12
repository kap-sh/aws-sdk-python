"""Generated from Smithy shape ``com.amazonaws.sqs#ListMessageMoveTasksResultEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sqs.types.long
    import aws_sdk_sqs.types.nullable_integer
    import aws_sdk_sqs.types.nullable_long
    import aws_sdk_sqs.types.string


class ListMessageMoveTasksResultEntry(TypedDict):
    task_handle: NotRequired["aws_sdk_sqs.types.string.String"]
    """<p>An identifier associated with a message movement task. When this field is returned in the response of the <code>ListMessageMoveTasks</code> action, it is only populated for tasks that are in RUNNING status.</p>"""
    status: NotRequired["aws_sdk_sqs.types.string.String"]
    """<p>The status of the message movement task. Possible values are: RUNNING, COMPLETED, CANCELLING, CANCELLED, and FAILED.</p>"""
    source_arn: NotRequired["aws_sdk_sqs.types.string.String"]
    """<p>The ARN of the queue that contains the messages to be moved to another queue.</p>"""
    destination_arn: NotRequired["aws_sdk_sqs.types.string.String"]
    """<p>The ARN of the destination queue if it has been specified in the <code>StartMessageMoveTask</code> request. If a <code>DestinationArn</code> has not been specified in the <code>StartMessageMoveTask</code> request, this field value will be NULL.</p>"""
    max_number_of_messages_per_second: NotRequired[
        "aws_sdk_sqs.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of messages to be moved per second (the message movement rate), if it has been specified in the <code>StartMessageMoveTask</code> request. If a <code>MaxNumberOfMessagesPerSecond</code> has not been specified in the <code>StartMessageMoveTask</code> request, this field value will be NULL.</p>"""
    approximate_number_of_messages_moved: "aws_sdk_sqs.types.long.Long"
    """<p>The approximate number of messages already moved to the destination queue.</p>"""
    approximate_number_of_messages_to_move: NotRequired[
        "aws_sdk_sqs.types.nullable_long.NullableLong"
    ]
    """<p>The number of messages to be moved from the source queue. This number is obtained at the time of starting the message movement task and is only included after the message movement task is selected to start.</p>"""
    failure_reason: NotRequired["aws_sdk_sqs.types.string.String"]
    """<p>The task failure reason (only included if the task status is FAILED).</p>"""
    started_timestamp: "aws_sdk_sqs.types.long.Long"
    """<p>The timestamp of starting the message movement task.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListMessageMoveTasksResultEntry) -> dict:
    out: dict = {}
    if "task_handle" in value:
        out["TaskHandle"] = value["task_handle"]
    if "status" in value:
        out["Status"] = value["status"]
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "destination_arn" in value:
        out["DestinationArn"] = value["destination_arn"]
    if "max_number_of_messages_per_second" in value:
        out["MaxNumberOfMessagesPerSecond"] = value["max_number_of_messages_per_second"]
    out["ApproximateNumberOfMessagesMoved"] = value.get(
        "approximate_number_of_messages_moved", 0
    )
    if "approximate_number_of_messages_to_move" in value:
        out["ApproximateNumberOfMessagesToMove"] = value[
            "approximate_number_of_messages_to_move"
        ]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    out["StartedTimestamp"] = value.get("started_timestamp", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> ListMessageMoveTasksResultEntry:
    out: ListMessageMoveTasksResultEntry = {}  # type: ignore[typeddict-item]
    if "TaskHandle" in data:
        out["task_handle"] = data["TaskHandle"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    if "DestinationArn" in data:
        out["destination_arn"] = data["DestinationArn"]
    if "MaxNumberOfMessagesPerSecond" in data:
        out["max_number_of_messages_per_second"] = data["MaxNumberOfMessagesPerSecond"]
    if "ApproximateNumberOfMessagesMoved" in data:
        out["approximate_number_of_messages_moved"] = data[
            "ApproximateNumberOfMessagesMoved"
        ]
    else:
        out["approximate_number_of_messages_moved"] = 0
    if "ApproximateNumberOfMessagesToMove" in data:
        out["approximate_number_of_messages_to_move"] = data[
            "ApproximateNumberOfMessagesToMove"
        ]
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "StartedTimestamp" in data:
        out["started_timestamp"] = data["StartedTimestamp"]
    else:
        out["started_timestamp"] = 0
    return out
