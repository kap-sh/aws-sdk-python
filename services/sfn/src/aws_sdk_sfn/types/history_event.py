"""Generated from Smithy shape ``com.amazonaws.sfn#HistoryEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.activity_failed_event_details
    import aws_sdk_sfn.types.activity_schedule_failed_event_details
    import aws_sdk_sfn.types.activity_scheduled_event_details
    import aws_sdk_sfn.types.activity_started_event_details
    import aws_sdk_sfn.types.activity_succeeded_event_details
    import aws_sdk_sfn.types.activity_timed_out_event_details
    import aws_sdk_sfn.types.evaluation_failed_event_details
    import aws_sdk_sfn.types.event_id
    import aws_sdk_sfn.types.execution_aborted_event_details
    import aws_sdk_sfn.types.execution_failed_event_details
    import aws_sdk_sfn.types.execution_redriven_event_details
    import aws_sdk_sfn.types.execution_started_event_details
    import aws_sdk_sfn.types.execution_succeeded_event_details
    import aws_sdk_sfn.types.execution_timed_out_event_details
    import aws_sdk_sfn.types.history_event_type
    import aws_sdk_sfn.types.lambda_function_failed_event_details
    import aws_sdk_sfn.types.lambda_function_schedule_failed_event_details
    import aws_sdk_sfn.types.lambda_function_scheduled_event_details
    import aws_sdk_sfn.types.lambda_function_start_failed_event_details
    import aws_sdk_sfn.types.lambda_function_succeeded_event_details
    import aws_sdk_sfn.types.lambda_function_timed_out_event_details
    import aws_sdk_sfn.types.map_iteration_event_details
    import aws_sdk_sfn.types.map_run_failed_event_details
    import aws_sdk_sfn.types.map_run_redriven_event_details
    import aws_sdk_sfn.types.map_run_started_event_details
    import aws_sdk_sfn.types.map_state_started_event_details
    import aws_sdk_sfn.types.state_entered_event_details
    import aws_sdk_sfn.types.state_exited_event_details
    import aws_sdk_sfn.types.task_failed_event_details
    import aws_sdk_sfn.types.task_scheduled_event_details
    import aws_sdk_sfn.types.task_start_failed_event_details
    import aws_sdk_sfn.types.task_started_event_details
    import aws_sdk_sfn.types.task_submit_failed_event_details
    import aws_sdk_sfn.types.task_submitted_event_details
    import aws_sdk_sfn.types.task_succeeded_event_details
    import aws_sdk_sfn.types.task_timed_out_event_details
    import aws_sdk_sfn.types.timestamp


class HistoryEvent(TypedDict, closed=True):
    timestamp: "aws_sdk_sfn.types.timestamp.Timestamp"
    """<p>The date and time the event occurred, expressed in seconds and fractional milliseconds since the Unix epoch, which is defined as January 1, 1970, at 00:00:00 Coordinated Universal Time (UTC).</p>"""
    type: "aws_sdk_sfn.types.history_event_type.HistoryEventType"
    """<p>The type of the event.</p>"""
    id: "aws_sdk_sfn.types.event_id.EventId"
    """<p>The id of the event. Events are numbered sequentially, starting at one.</p>"""
    previous_event_id: "aws_sdk_sfn.types.event_id.EventId"
    """<p>The id of the previous event.</p>"""
    activity_failed_event_details: NotRequired[
        "aws_sdk_sfn.types.activity_failed_event_details.ActivityFailedEventDetails"
    ]
    activity_schedule_failed_event_details: NotRequired[
        "aws_sdk_sfn.types.activity_schedule_failed_event_details.ActivityScheduleFailedEventDetails"
    ]
    """<p>Contains details about an activity schedule event that failed during an execution.</p>"""
    activity_scheduled_event_details: NotRequired[
        "aws_sdk_sfn.types.activity_scheduled_event_details.ActivityScheduledEventDetails"
    ]
    activity_started_event_details: NotRequired[
        "aws_sdk_sfn.types.activity_started_event_details.ActivityStartedEventDetails"
    ]
    activity_succeeded_event_details: NotRequired[
        "aws_sdk_sfn.types.activity_succeeded_event_details.ActivitySucceededEventDetails"
    ]
    activity_timed_out_event_details: NotRequired[
        "aws_sdk_sfn.types.activity_timed_out_event_details.ActivityTimedOutEventDetails"
    ]
    task_failed_event_details: NotRequired[
        "aws_sdk_sfn.types.task_failed_event_details.TaskFailedEventDetails"
    ]
    """<p>Contains details about the failure of a task.</p>"""
    task_scheduled_event_details: NotRequired[
        "aws_sdk_sfn.types.task_scheduled_event_details.TaskScheduledEventDetails"
    ]
    """<p>Contains details about a task that was scheduled.</p>"""
    task_start_failed_event_details: NotRequired[
        "aws_sdk_sfn.types.task_start_failed_event_details.TaskStartFailedEventDetails"
    ]
    """<p>Contains details about a task that failed to start.</p>"""
    task_started_event_details: NotRequired[
        "aws_sdk_sfn.types.task_started_event_details.TaskStartedEventDetails"
    ]
    """<p>Contains details about a task that was started.</p>"""
    task_submit_failed_event_details: NotRequired[
        "aws_sdk_sfn.types.task_submit_failed_event_details.TaskSubmitFailedEventDetails"
    ]
    """<p>Contains details about a task that where the submit failed.</p>"""
    task_submitted_event_details: NotRequired[
        "aws_sdk_sfn.types.task_submitted_event_details.TaskSubmittedEventDetails"
    ]
    """<p>Contains details about a submitted task.</p>"""
    task_succeeded_event_details: NotRequired[
        "aws_sdk_sfn.types.task_succeeded_event_details.TaskSucceededEventDetails"
    ]
    """<p>Contains details about a task that succeeded.</p>"""
    task_timed_out_event_details: NotRequired[
        "aws_sdk_sfn.types.task_timed_out_event_details.TaskTimedOutEventDetails"
    ]
    """<p>Contains details about a task that timed out.</p>"""
    execution_failed_event_details: NotRequired[
        "aws_sdk_sfn.types.execution_failed_event_details.ExecutionFailedEventDetails"
    ]
    execution_started_event_details: NotRequired[
        "aws_sdk_sfn.types.execution_started_event_details.ExecutionStartedEventDetails"
    ]
    execution_succeeded_event_details: NotRequired[
        "aws_sdk_sfn.types.execution_succeeded_event_details.ExecutionSucceededEventDetails"
    ]
    execution_aborted_event_details: NotRequired[
        "aws_sdk_sfn.types.execution_aborted_event_details.ExecutionAbortedEventDetails"
    ]
    execution_timed_out_event_details: NotRequired[
        "aws_sdk_sfn.types.execution_timed_out_event_details.ExecutionTimedOutEventDetails"
    ]
    execution_redriven_event_details: NotRequired[
        "aws_sdk_sfn.types.execution_redriven_event_details.ExecutionRedrivenEventDetails"
    ]
    """<p>Contains details about the redrive attempt of an execution.</p>"""
    map_state_started_event_details: NotRequired[
        "aws_sdk_sfn.types.map_state_started_event_details.MapStateStartedEventDetails"
    ]
    """<p>Contains details about Map state that was started.</p>"""
    map_iteration_started_event_details: NotRequired[
        "aws_sdk_sfn.types.map_iteration_event_details.MapIterationEventDetails"
    ]
    """<p>Contains details about an iteration of a Map state that was started.</p>"""
    map_iteration_succeeded_event_details: NotRequired[
        "aws_sdk_sfn.types.map_iteration_event_details.MapIterationEventDetails"
    ]
    """<p>Contains details about an iteration of a Map state that succeeded.</p>"""
    map_iteration_failed_event_details: NotRequired[
        "aws_sdk_sfn.types.map_iteration_event_details.MapIterationEventDetails"
    ]
    """<p>Contains details about an iteration of a Map state that failed.</p>"""
    map_iteration_aborted_event_details: NotRequired[
        "aws_sdk_sfn.types.map_iteration_event_details.MapIterationEventDetails"
    ]
    """<p>Contains details about an iteration of a Map state that was aborted.</p>"""
    lambda_function_failed_event_details: NotRequired[
        "aws_sdk_sfn.types.lambda_function_failed_event_details.LambdaFunctionFailedEventDetails"
    ]
    lambda_function_schedule_failed_event_details: NotRequired[
        "aws_sdk_sfn.types.lambda_function_schedule_failed_event_details.LambdaFunctionScheduleFailedEventDetails"
    ]
    lambda_function_scheduled_event_details: NotRequired[
        "aws_sdk_sfn.types.lambda_function_scheduled_event_details.LambdaFunctionScheduledEventDetails"
    ]
    lambda_function_start_failed_event_details: NotRequired[
        "aws_sdk_sfn.types.lambda_function_start_failed_event_details.LambdaFunctionStartFailedEventDetails"
    ]
    """<p>Contains details about a lambda function that failed to start during an execution.</p>"""
    lambda_function_succeeded_event_details: NotRequired[
        "aws_sdk_sfn.types.lambda_function_succeeded_event_details.LambdaFunctionSucceededEventDetails"
    ]
    """<p>Contains details about a Lambda function that terminated successfully during an execution.</p>"""
    lambda_function_timed_out_event_details: NotRequired[
        "aws_sdk_sfn.types.lambda_function_timed_out_event_details.LambdaFunctionTimedOutEventDetails"
    ]
    state_entered_event_details: NotRequired[
        "aws_sdk_sfn.types.state_entered_event_details.StateEnteredEventDetails"
    ]
    state_exited_event_details: NotRequired[
        "aws_sdk_sfn.types.state_exited_event_details.StateExitedEventDetails"
    ]
    map_run_started_event_details: NotRequired[
        "aws_sdk_sfn.types.map_run_started_event_details.MapRunStartedEventDetails"
    ]
    """<p>Contains details, such as <code>mapRunArn</code>, and the start date and time of a Map Run. <code>mapRunArn</code> is the Amazon Resource Name (ARN) of the Map Run that was started.</p>"""
    map_run_failed_event_details: NotRequired[
        "aws_sdk_sfn.types.map_run_failed_event_details.MapRunFailedEventDetails"
    ]
    """<p>Contains error and cause details about a Map Run that failed.</p>"""
    map_run_redriven_event_details: NotRequired[
        "aws_sdk_sfn.types.map_run_redriven_event_details.MapRunRedrivenEventDetails"
    ]
    """<p>Contains details about the redrive attempt of a Map Run.</p>"""
    evaluation_failed_event_details: NotRequired[
        "aws_sdk_sfn.types.evaluation_failed_event_details.EvaluationFailedEventDetails"
    ]
    """<p>Contains details about an evaluation failure that occurred while processing a state.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HistoryEvent) -> dict:
    out: dict = {}
    import aws_sdk_sfn.types.timestamp

    out["timestamp"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
        value["timestamp"]
    )
    import aws_sdk_sfn.types.history_event_type

    out["type"] = aws_sdk_sfn.types.history_event_type.serialize_aws_json_1_0(
        value["type"]
    )
    out["id"] = value.get("id", 0)
    out["previousEventId"] = value.get("previous_event_id", 0)
    if "activity_failed_event_details" in value:
        import aws_sdk_sfn.types.activity_failed_event_details

        out["activityFailedEventDetails"] = (
            aws_sdk_sfn.types.activity_failed_event_details.serialize_aws_json_1_0(
                value["activity_failed_event_details"]
            )
        )
    if "activity_schedule_failed_event_details" in value:
        import aws_sdk_sfn.types.activity_schedule_failed_event_details

        out["activityScheduleFailedEventDetails"] = (
            aws_sdk_sfn.types.activity_schedule_failed_event_details.serialize_aws_json_1_0(
                value["activity_schedule_failed_event_details"]
            )
        )
    if "activity_scheduled_event_details" in value:
        import aws_sdk_sfn.types.activity_scheduled_event_details

        out["activityScheduledEventDetails"] = (
            aws_sdk_sfn.types.activity_scheduled_event_details.serialize_aws_json_1_0(
                value["activity_scheduled_event_details"]
            )
        )
    if "activity_started_event_details" in value:
        import aws_sdk_sfn.types.activity_started_event_details

        out["activityStartedEventDetails"] = (
            aws_sdk_sfn.types.activity_started_event_details.serialize_aws_json_1_0(
                value["activity_started_event_details"]
            )
        )
    if "activity_succeeded_event_details" in value:
        import aws_sdk_sfn.types.activity_succeeded_event_details

        out["activitySucceededEventDetails"] = (
            aws_sdk_sfn.types.activity_succeeded_event_details.serialize_aws_json_1_0(
                value["activity_succeeded_event_details"]
            )
        )
    if "activity_timed_out_event_details" in value:
        import aws_sdk_sfn.types.activity_timed_out_event_details

        out["activityTimedOutEventDetails"] = (
            aws_sdk_sfn.types.activity_timed_out_event_details.serialize_aws_json_1_0(
                value["activity_timed_out_event_details"]
            )
        )
    if "task_failed_event_details" in value:
        import aws_sdk_sfn.types.task_failed_event_details

        out["taskFailedEventDetails"] = (
            aws_sdk_sfn.types.task_failed_event_details.serialize_aws_json_1_0(
                value["task_failed_event_details"]
            )
        )
    if "task_scheduled_event_details" in value:
        import aws_sdk_sfn.types.task_scheduled_event_details

        out["taskScheduledEventDetails"] = (
            aws_sdk_sfn.types.task_scheduled_event_details.serialize_aws_json_1_0(
                value["task_scheduled_event_details"]
            )
        )
    if "task_start_failed_event_details" in value:
        import aws_sdk_sfn.types.task_start_failed_event_details

        out["taskStartFailedEventDetails"] = (
            aws_sdk_sfn.types.task_start_failed_event_details.serialize_aws_json_1_0(
                value["task_start_failed_event_details"]
            )
        )
    if "task_started_event_details" in value:
        import aws_sdk_sfn.types.task_started_event_details

        out["taskStartedEventDetails"] = (
            aws_sdk_sfn.types.task_started_event_details.serialize_aws_json_1_0(
                value["task_started_event_details"]
            )
        )
    if "task_submit_failed_event_details" in value:
        import aws_sdk_sfn.types.task_submit_failed_event_details

        out["taskSubmitFailedEventDetails"] = (
            aws_sdk_sfn.types.task_submit_failed_event_details.serialize_aws_json_1_0(
                value["task_submit_failed_event_details"]
            )
        )
    if "task_submitted_event_details" in value:
        import aws_sdk_sfn.types.task_submitted_event_details

        out["taskSubmittedEventDetails"] = (
            aws_sdk_sfn.types.task_submitted_event_details.serialize_aws_json_1_0(
                value["task_submitted_event_details"]
            )
        )
    if "task_succeeded_event_details" in value:
        import aws_sdk_sfn.types.task_succeeded_event_details

        out["taskSucceededEventDetails"] = (
            aws_sdk_sfn.types.task_succeeded_event_details.serialize_aws_json_1_0(
                value["task_succeeded_event_details"]
            )
        )
    if "task_timed_out_event_details" in value:
        import aws_sdk_sfn.types.task_timed_out_event_details

        out["taskTimedOutEventDetails"] = (
            aws_sdk_sfn.types.task_timed_out_event_details.serialize_aws_json_1_0(
                value["task_timed_out_event_details"]
            )
        )
    if "execution_failed_event_details" in value:
        import aws_sdk_sfn.types.execution_failed_event_details

        out["executionFailedEventDetails"] = (
            aws_sdk_sfn.types.execution_failed_event_details.serialize_aws_json_1_0(
                value["execution_failed_event_details"]
            )
        )
    if "execution_started_event_details" in value:
        import aws_sdk_sfn.types.execution_started_event_details

        out["executionStartedEventDetails"] = (
            aws_sdk_sfn.types.execution_started_event_details.serialize_aws_json_1_0(
                value["execution_started_event_details"]
            )
        )
    if "execution_succeeded_event_details" in value:
        import aws_sdk_sfn.types.execution_succeeded_event_details

        out["executionSucceededEventDetails"] = (
            aws_sdk_sfn.types.execution_succeeded_event_details.serialize_aws_json_1_0(
                value["execution_succeeded_event_details"]
            )
        )
    if "execution_aborted_event_details" in value:
        import aws_sdk_sfn.types.execution_aborted_event_details

        out["executionAbortedEventDetails"] = (
            aws_sdk_sfn.types.execution_aborted_event_details.serialize_aws_json_1_0(
                value["execution_aborted_event_details"]
            )
        )
    if "execution_timed_out_event_details" in value:
        import aws_sdk_sfn.types.execution_timed_out_event_details

        out["executionTimedOutEventDetails"] = (
            aws_sdk_sfn.types.execution_timed_out_event_details.serialize_aws_json_1_0(
                value["execution_timed_out_event_details"]
            )
        )
    if "execution_redriven_event_details" in value:
        import aws_sdk_sfn.types.execution_redriven_event_details

        out["executionRedrivenEventDetails"] = (
            aws_sdk_sfn.types.execution_redriven_event_details.serialize_aws_json_1_0(
                value["execution_redriven_event_details"]
            )
        )
    if "map_state_started_event_details" in value:
        import aws_sdk_sfn.types.map_state_started_event_details

        out["mapStateStartedEventDetails"] = (
            aws_sdk_sfn.types.map_state_started_event_details.serialize_aws_json_1_0(
                value["map_state_started_event_details"]
            )
        )
    if "map_iteration_started_event_details" in value:
        import aws_sdk_sfn.types.map_iteration_event_details

        out["mapIterationStartedEventDetails"] = (
            aws_sdk_sfn.types.map_iteration_event_details.serialize_aws_json_1_0(
                value["map_iteration_started_event_details"]
            )
        )
    if "map_iteration_succeeded_event_details" in value:
        import aws_sdk_sfn.types.map_iteration_event_details

        out["mapIterationSucceededEventDetails"] = (
            aws_sdk_sfn.types.map_iteration_event_details.serialize_aws_json_1_0(
                value["map_iteration_succeeded_event_details"]
            )
        )
    if "map_iteration_failed_event_details" in value:
        import aws_sdk_sfn.types.map_iteration_event_details

        out["mapIterationFailedEventDetails"] = (
            aws_sdk_sfn.types.map_iteration_event_details.serialize_aws_json_1_0(
                value["map_iteration_failed_event_details"]
            )
        )
    if "map_iteration_aborted_event_details" in value:
        import aws_sdk_sfn.types.map_iteration_event_details

        out["mapIterationAbortedEventDetails"] = (
            aws_sdk_sfn.types.map_iteration_event_details.serialize_aws_json_1_0(
                value["map_iteration_aborted_event_details"]
            )
        )
    if "lambda_function_failed_event_details" in value:
        import aws_sdk_sfn.types.lambda_function_failed_event_details

        out["lambdaFunctionFailedEventDetails"] = (
            aws_sdk_sfn.types.lambda_function_failed_event_details.serialize_aws_json_1_0(
                value["lambda_function_failed_event_details"]
            )
        )
    if "lambda_function_schedule_failed_event_details" in value:
        import aws_sdk_sfn.types.lambda_function_schedule_failed_event_details

        out["lambdaFunctionScheduleFailedEventDetails"] = (
            aws_sdk_sfn.types.lambda_function_schedule_failed_event_details.serialize_aws_json_1_0(
                value["lambda_function_schedule_failed_event_details"]
            )
        )
    if "lambda_function_scheduled_event_details" in value:
        import aws_sdk_sfn.types.lambda_function_scheduled_event_details

        out["lambdaFunctionScheduledEventDetails"] = (
            aws_sdk_sfn.types.lambda_function_scheduled_event_details.serialize_aws_json_1_0(
                value["lambda_function_scheduled_event_details"]
            )
        )
    if "lambda_function_start_failed_event_details" in value:
        import aws_sdk_sfn.types.lambda_function_start_failed_event_details

        out["lambdaFunctionStartFailedEventDetails"] = (
            aws_sdk_sfn.types.lambda_function_start_failed_event_details.serialize_aws_json_1_0(
                value["lambda_function_start_failed_event_details"]
            )
        )
    if "lambda_function_succeeded_event_details" in value:
        import aws_sdk_sfn.types.lambda_function_succeeded_event_details

        out["lambdaFunctionSucceededEventDetails"] = (
            aws_sdk_sfn.types.lambda_function_succeeded_event_details.serialize_aws_json_1_0(
                value["lambda_function_succeeded_event_details"]
            )
        )
    if "lambda_function_timed_out_event_details" in value:
        import aws_sdk_sfn.types.lambda_function_timed_out_event_details

        out["lambdaFunctionTimedOutEventDetails"] = (
            aws_sdk_sfn.types.lambda_function_timed_out_event_details.serialize_aws_json_1_0(
                value["lambda_function_timed_out_event_details"]
            )
        )
    if "state_entered_event_details" in value:
        import aws_sdk_sfn.types.state_entered_event_details

        out["stateEnteredEventDetails"] = (
            aws_sdk_sfn.types.state_entered_event_details.serialize_aws_json_1_0(
                value["state_entered_event_details"]
            )
        )
    if "state_exited_event_details" in value:
        import aws_sdk_sfn.types.state_exited_event_details

        out["stateExitedEventDetails"] = (
            aws_sdk_sfn.types.state_exited_event_details.serialize_aws_json_1_0(
                value["state_exited_event_details"]
            )
        )
    if "map_run_started_event_details" in value:
        import aws_sdk_sfn.types.map_run_started_event_details

        out["mapRunStartedEventDetails"] = (
            aws_sdk_sfn.types.map_run_started_event_details.serialize_aws_json_1_0(
                value["map_run_started_event_details"]
            )
        )
    if "map_run_failed_event_details" in value:
        import aws_sdk_sfn.types.map_run_failed_event_details

        out["mapRunFailedEventDetails"] = (
            aws_sdk_sfn.types.map_run_failed_event_details.serialize_aws_json_1_0(
                value["map_run_failed_event_details"]
            )
        )
    if "map_run_redriven_event_details" in value:
        import aws_sdk_sfn.types.map_run_redriven_event_details

        out["mapRunRedrivenEventDetails"] = (
            aws_sdk_sfn.types.map_run_redriven_event_details.serialize_aws_json_1_0(
                value["map_run_redriven_event_details"]
            )
        )
    if "evaluation_failed_event_details" in value:
        import aws_sdk_sfn.types.evaluation_failed_event_details

        out["evaluationFailedEventDetails"] = (
            aws_sdk_sfn.types.evaluation_failed_event_details.serialize_aws_json_1_0(
                value["evaluation_failed_event_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> HistoryEvent:
    out: HistoryEvent = {}  # type: ignore[typeddict-item]
    if "timestamp" in data:
        import aws_sdk_sfn.types.timestamp

        out["timestamp"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["timestamp"]
        )
    else:
        raise DeserializationError("HistoryEvent.timestamp required")
    if "type" in data:
        import aws_sdk_sfn.types.history_event_type

        out["type"] = aws_sdk_sfn.types.history_event_type.deserialize_aws_json_1_0(
            data["type"]
        )
    else:
        raise DeserializationError("HistoryEvent.type required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        out["id"] = 0
    if "previousEventId" in data:
        out["previous_event_id"] = data["previousEventId"]
    else:
        out["previous_event_id"] = 0
    if "activityFailedEventDetails" in data:
        import aws_sdk_sfn.types.activity_failed_event_details

        out["activity_failed_event_details"] = (
            aws_sdk_sfn.types.activity_failed_event_details.deserialize_aws_json_1_0(
                data["activityFailedEventDetails"]
            )
        )
    if "activityScheduleFailedEventDetails" in data:
        import aws_sdk_sfn.types.activity_schedule_failed_event_details

        out["activity_schedule_failed_event_details"] = (
            aws_sdk_sfn.types.activity_schedule_failed_event_details.deserialize_aws_json_1_0(
                data["activityScheduleFailedEventDetails"]
            )
        )
    if "activityScheduledEventDetails" in data:
        import aws_sdk_sfn.types.activity_scheduled_event_details

        out["activity_scheduled_event_details"] = (
            aws_sdk_sfn.types.activity_scheduled_event_details.deserialize_aws_json_1_0(
                data["activityScheduledEventDetails"]
            )
        )
    if "activityStartedEventDetails" in data:
        import aws_sdk_sfn.types.activity_started_event_details

        out["activity_started_event_details"] = (
            aws_sdk_sfn.types.activity_started_event_details.deserialize_aws_json_1_0(
                data["activityStartedEventDetails"]
            )
        )
    if "activitySucceededEventDetails" in data:
        import aws_sdk_sfn.types.activity_succeeded_event_details

        out["activity_succeeded_event_details"] = (
            aws_sdk_sfn.types.activity_succeeded_event_details.deserialize_aws_json_1_0(
                data["activitySucceededEventDetails"]
            )
        )
    if "activityTimedOutEventDetails" in data:
        import aws_sdk_sfn.types.activity_timed_out_event_details

        out["activity_timed_out_event_details"] = (
            aws_sdk_sfn.types.activity_timed_out_event_details.deserialize_aws_json_1_0(
                data["activityTimedOutEventDetails"]
            )
        )
    if "taskFailedEventDetails" in data:
        import aws_sdk_sfn.types.task_failed_event_details

        out["task_failed_event_details"] = (
            aws_sdk_sfn.types.task_failed_event_details.deserialize_aws_json_1_0(
                data["taskFailedEventDetails"]
            )
        )
    if "taskScheduledEventDetails" in data:
        import aws_sdk_sfn.types.task_scheduled_event_details

        out["task_scheduled_event_details"] = (
            aws_sdk_sfn.types.task_scheduled_event_details.deserialize_aws_json_1_0(
                data["taskScheduledEventDetails"]
            )
        )
    if "taskStartFailedEventDetails" in data:
        import aws_sdk_sfn.types.task_start_failed_event_details

        out["task_start_failed_event_details"] = (
            aws_sdk_sfn.types.task_start_failed_event_details.deserialize_aws_json_1_0(
                data["taskStartFailedEventDetails"]
            )
        )
    if "taskStartedEventDetails" in data:
        import aws_sdk_sfn.types.task_started_event_details

        out["task_started_event_details"] = (
            aws_sdk_sfn.types.task_started_event_details.deserialize_aws_json_1_0(
                data["taskStartedEventDetails"]
            )
        )
    if "taskSubmitFailedEventDetails" in data:
        import aws_sdk_sfn.types.task_submit_failed_event_details

        out["task_submit_failed_event_details"] = (
            aws_sdk_sfn.types.task_submit_failed_event_details.deserialize_aws_json_1_0(
                data["taskSubmitFailedEventDetails"]
            )
        )
    if "taskSubmittedEventDetails" in data:
        import aws_sdk_sfn.types.task_submitted_event_details

        out["task_submitted_event_details"] = (
            aws_sdk_sfn.types.task_submitted_event_details.deserialize_aws_json_1_0(
                data["taskSubmittedEventDetails"]
            )
        )
    if "taskSucceededEventDetails" in data:
        import aws_sdk_sfn.types.task_succeeded_event_details

        out["task_succeeded_event_details"] = (
            aws_sdk_sfn.types.task_succeeded_event_details.deserialize_aws_json_1_0(
                data["taskSucceededEventDetails"]
            )
        )
    if "taskTimedOutEventDetails" in data:
        import aws_sdk_sfn.types.task_timed_out_event_details

        out["task_timed_out_event_details"] = (
            aws_sdk_sfn.types.task_timed_out_event_details.deserialize_aws_json_1_0(
                data["taskTimedOutEventDetails"]
            )
        )
    if "executionFailedEventDetails" in data:
        import aws_sdk_sfn.types.execution_failed_event_details

        out["execution_failed_event_details"] = (
            aws_sdk_sfn.types.execution_failed_event_details.deserialize_aws_json_1_0(
                data["executionFailedEventDetails"]
            )
        )
    if "executionStartedEventDetails" in data:
        import aws_sdk_sfn.types.execution_started_event_details

        out["execution_started_event_details"] = (
            aws_sdk_sfn.types.execution_started_event_details.deserialize_aws_json_1_0(
                data["executionStartedEventDetails"]
            )
        )
    if "executionSucceededEventDetails" in data:
        import aws_sdk_sfn.types.execution_succeeded_event_details

        out["execution_succeeded_event_details"] = (
            aws_sdk_sfn.types.execution_succeeded_event_details.deserialize_aws_json_1_0(
                data["executionSucceededEventDetails"]
            )
        )
    if "executionAbortedEventDetails" in data:
        import aws_sdk_sfn.types.execution_aborted_event_details

        out["execution_aborted_event_details"] = (
            aws_sdk_sfn.types.execution_aborted_event_details.deserialize_aws_json_1_0(
                data["executionAbortedEventDetails"]
            )
        )
    if "executionTimedOutEventDetails" in data:
        import aws_sdk_sfn.types.execution_timed_out_event_details

        out["execution_timed_out_event_details"] = (
            aws_sdk_sfn.types.execution_timed_out_event_details.deserialize_aws_json_1_0(
                data["executionTimedOutEventDetails"]
            )
        )
    if "executionRedrivenEventDetails" in data:
        import aws_sdk_sfn.types.execution_redriven_event_details

        out["execution_redriven_event_details"] = (
            aws_sdk_sfn.types.execution_redriven_event_details.deserialize_aws_json_1_0(
                data["executionRedrivenEventDetails"]
            )
        )
    if "mapStateStartedEventDetails" in data:
        import aws_sdk_sfn.types.map_state_started_event_details

        out["map_state_started_event_details"] = (
            aws_sdk_sfn.types.map_state_started_event_details.deserialize_aws_json_1_0(
                data["mapStateStartedEventDetails"]
            )
        )
    if "mapIterationStartedEventDetails" in data:
        import aws_sdk_sfn.types.map_iteration_event_details

        out["map_iteration_started_event_details"] = (
            aws_sdk_sfn.types.map_iteration_event_details.deserialize_aws_json_1_0(
                data["mapIterationStartedEventDetails"]
            )
        )
    if "mapIterationSucceededEventDetails" in data:
        import aws_sdk_sfn.types.map_iteration_event_details

        out["map_iteration_succeeded_event_details"] = (
            aws_sdk_sfn.types.map_iteration_event_details.deserialize_aws_json_1_0(
                data["mapIterationSucceededEventDetails"]
            )
        )
    if "mapIterationFailedEventDetails" in data:
        import aws_sdk_sfn.types.map_iteration_event_details

        out["map_iteration_failed_event_details"] = (
            aws_sdk_sfn.types.map_iteration_event_details.deserialize_aws_json_1_0(
                data["mapIterationFailedEventDetails"]
            )
        )
    if "mapIterationAbortedEventDetails" in data:
        import aws_sdk_sfn.types.map_iteration_event_details

        out["map_iteration_aborted_event_details"] = (
            aws_sdk_sfn.types.map_iteration_event_details.deserialize_aws_json_1_0(
                data["mapIterationAbortedEventDetails"]
            )
        )
    if "lambdaFunctionFailedEventDetails" in data:
        import aws_sdk_sfn.types.lambda_function_failed_event_details

        out["lambda_function_failed_event_details"] = (
            aws_sdk_sfn.types.lambda_function_failed_event_details.deserialize_aws_json_1_0(
                data["lambdaFunctionFailedEventDetails"]
            )
        )
    if "lambdaFunctionScheduleFailedEventDetails" in data:
        import aws_sdk_sfn.types.lambda_function_schedule_failed_event_details

        out["lambda_function_schedule_failed_event_details"] = (
            aws_sdk_sfn.types.lambda_function_schedule_failed_event_details.deserialize_aws_json_1_0(
                data["lambdaFunctionScheduleFailedEventDetails"]
            )
        )
    if "lambdaFunctionScheduledEventDetails" in data:
        import aws_sdk_sfn.types.lambda_function_scheduled_event_details

        out["lambda_function_scheduled_event_details"] = (
            aws_sdk_sfn.types.lambda_function_scheduled_event_details.deserialize_aws_json_1_0(
                data["lambdaFunctionScheduledEventDetails"]
            )
        )
    if "lambdaFunctionStartFailedEventDetails" in data:
        import aws_sdk_sfn.types.lambda_function_start_failed_event_details

        out["lambda_function_start_failed_event_details"] = (
            aws_sdk_sfn.types.lambda_function_start_failed_event_details.deserialize_aws_json_1_0(
                data["lambdaFunctionStartFailedEventDetails"]
            )
        )
    if "lambdaFunctionSucceededEventDetails" in data:
        import aws_sdk_sfn.types.lambda_function_succeeded_event_details

        out["lambda_function_succeeded_event_details"] = (
            aws_sdk_sfn.types.lambda_function_succeeded_event_details.deserialize_aws_json_1_0(
                data["lambdaFunctionSucceededEventDetails"]
            )
        )
    if "lambdaFunctionTimedOutEventDetails" in data:
        import aws_sdk_sfn.types.lambda_function_timed_out_event_details

        out["lambda_function_timed_out_event_details"] = (
            aws_sdk_sfn.types.lambda_function_timed_out_event_details.deserialize_aws_json_1_0(
                data["lambdaFunctionTimedOutEventDetails"]
            )
        )
    if "stateEnteredEventDetails" in data:
        import aws_sdk_sfn.types.state_entered_event_details

        out["state_entered_event_details"] = (
            aws_sdk_sfn.types.state_entered_event_details.deserialize_aws_json_1_0(
                data["stateEnteredEventDetails"]
            )
        )
    if "stateExitedEventDetails" in data:
        import aws_sdk_sfn.types.state_exited_event_details

        out["state_exited_event_details"] = (
            aws_sdk_sfn.types.state_exited_event_details.deserialize_aws_json_1_0(
                data["stateExitedEventDetails"]
            )
        )
    if "mapRunStartedEventDetails" in data:
        import aws_sdk_sfn.types.map_run_started_event_details

        out["map_run_started_event_details"] = (
            aws_sdk_sfn.types.map_run_started_event_details.deserialize_aws_json_1_0(
                data["mapRunStartedEventDetails"]
            )
        )
    if "mapRunFailedEventDetails" in data:
        import aws_sdk_sfn.types.map_run_failed_event_details

        out["map_run_failed_event_details"] = (
            aws_sdk_sfn.types.map_run_failed_event_details.deserialize_aws_json_1_0(
                data["mapRunFailedEventDetails"]
            )
        )
    if "mapRunRedrivenEventDetails" in data:
        import aws_sdk_sfn.types.map_run_redriven_event_details

        out["map_run_redriven_event_details"] = (
            aws_sdk_sfn.types.map_run_redriven_event_details.deserialize_aws_json_1_0(
                data["mapRunRedrivenEventDetails"]
            )
        )
    if "evaluationFailedEventDetails" in data:
        import aws_sdk_sfn.types.evaluation_failed_event_details

        out["evaluation_failed_event_details"] = (
            aws_sdk_sfn.types.evaluation_failed_event_details.deserialize_aws_json_1_0(
                data["evaluationFailedEventDetails"]
            )
        )
    return out
