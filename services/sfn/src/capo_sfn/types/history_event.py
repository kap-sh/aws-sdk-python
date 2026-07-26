"""Generated from Smithy shape ``com.amazonaws.sfn#HistoryEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sfn.types.activity_failed_event_details
    import capo_sfn.types.activity_schedule_failed_event_details
    import capo_sfn.types.activity_scheduled_event_details
    import capo_sfn.types.activity_started_event_details
    import capo_sfn.types.activity_succeeded_event_details
    import capo_sfn.types.activity_timed_out_event_details
    import capo_sfn.types.evaluation_failed_event_details
    import capo_sfn.types.event_id
    import capo_sfn.types.execution_aborted_event_details
    import capo_sfn.types.execution_failed_event_details
    import capo_sfn.types.execution_redriven_event_details
    import capo_sfn.types.execution_started_event_details
    import capo_sfn.types.execution_succeeded_event_details
    import capo_sfn.types.execution_timed_out_event_details
    import capo_sfn.types.history_event_type
    import capo_sfn.types.lambda_function_failed_event_details
    import capo_sfn.types.lambda_function_schedule_failed_event_details
    import capo_sfn.types.lambda_function_scheduled_event_details
    import capo_sfn.types.lambda_function_start_failed_event_details
    import capo_sfn.types.lambda_function_succeeded_event_details
    import capo_sfn.types.lambda_function_timed_out_event_details
    import capo_sfn.types.map_iteration_event_details
    import capo_sfn.types.map_run_failed_event_details
    import capo_sfn.types.map_run_redriven_event_details
    import capo_sfn.types.map_run_started_event_details
    import capo_sfn.types.map_state_started_event_details
    import capo_sfn.types.state_entered_event_details
    import capo_sfn.types.state_exited_event_details
    import capo_sfn.types.task_failed_event_details
    import capo_sfn.types.task_scheduled_event_details
    import capo_sfn.types.task_start_failed_event_details
    import capo_sfn.types.task_started_event_details
    import capo_sfn.types.task_submit_failed_event_details
    import capo_sfn.types.task_submitted_event_details
    import capo_sfn.types.task_succeeded_event_details
    import capo_sfn.types.task_timed_out_event_details
    import capo_sfn.types.timestamp


class HistoryEvent(TypedDict, closed=True):
    timestamp: "capo_sfn.types.timestamp.Timestamp"
    """<p>The date and time the event occurred, expressed in seconds and fractional milliseconds since the Unix epoch, which is defined as January 1, 1970, at 00:00:00 Coordinated Universal Time (UTC).</p>"""
    type: "capo_sfn.types.history_event_type.HistoryEventType"
    """<p>The type of the event.</p>"""
    id: "capo_sfn.types.event_id.EventId"
    """<p>The id of the event. Events are numbered sequentially, starting at one.</p>"""
    previous_event_id: "capo_sfn.types.event_id.EventId"
    """<p>The id of the previous event.</p>"""
    activity_failed_event_details: NotRequired[
        "capo_sfn.types.activity_failed_event_details.ActivityFailedEventDetails"
    ]
    activity_schedule_failed_event_details: NotRequired[
        "capo_sfn.types.activity_schedule_failed_event_details.ActivityScheduleFailedEventDetails"
    ]
    """<p>Contains details about an activity schedule event that failed during an execution.</p>"""
    activity_scheduled_event_details: NotRequired[
        "capo_sfn.types.activity_scheduled_event_details.ActivityScheduledEventDetails"
    ]
    activity_started_event_details: NotRequired[
        "capo_sfn.types.activity_started_event_details.ActivityStartedEventDetails"
    ]
    activity_succeeded_event_details: NotRequired[
        "capo_sfn.types.activity_succeeded_event_details.ActivitySucceededEventDetails"
    ]
    activity_timed_out_event_details: NotRequired[
        "capo_sfn.types.activity_timed_out_event_details.ActivityTimedOutEventDetails"
    ]
    task_failed_event_details: NotRequired[
        "capo_sfn.types.task_failed_event_details.TaskFailedEventDetails"
    ]
    """<p>Contains details about the failure of a task.</p>"""
    task_scheduled_event_details: NotRequired[
        "capo_sfn.types.task_scheduled_event_details.TaskScheduledEventDetails"
    ]
    """<p>Contains details about a task that was scheduled.</p>"""
    task_start_failed_event_details: NotRequired[
        "capo_sfn.types.task_start_failed_event_details.TaskStartFailedEventDetails"
    ]
    """<p>Contains details about a task that failed to start.</p>"""
    task_started_event_details: NotRequired[
        "capo_sfn.types.task_started_event_details.TaskStartedEventDetails"
    ]
    """<p>Contains details about a task that was started.</p>"""
    task_submit_failed_event_details: NotRequired[
        "capo_sfn.types.task_submit_failed_event_details.TaskSubmitFailedEventDetails"
    ]
    """<p>Contains details about a task that where the submit failed.</p>"""
    task_submitted_event_details: NotRequired[
        "capo_sfn.types.task_submitted_event_details.TaskSubmittedEventDetails"
    ]
    """<p>Contains details about a submitted task.</p>"""
    task_succeeded_event_details: NotRequired[
        "capo_sfn.types.task_succeeded_event_details.TaskSucceededEventDetails"
    ]
    """<p>Contains details about a task that succeeded.</p>"""
    task_timed_out_event_details: NotRequired[
        "capo_sfn.types.task_timed_out_event_details.TaskTimedOutEventDetails"
    ]
    """<p>Contains details about a task that timed out.</p>"""
    execution_failed_event_details: NotRequired[
        "capo_sfn.types.execution_failed_event_details.ExecutionFailedEventDetails"
    ]
    execution_started_event_details: NotRequired[
        "capo_sfn.types.execution_started_event_details.ExecutionStartedEventDetails"
    ]
    execution_succeeded_event_details: NotRequired[
        "capo_sfn.types.execution_succeeded_event_details.ExecutionSucceededEventDetails"
    ]
    execution_aborted_event_details: NotRequired[
        "capo_sfn.types.execution_aborted_event_details.ExecutionAbortedEventDetails"
    ]
    execution_timed_out_event_details: NotRequired[
        "capo_sfn.types.execution_timed_out_event_details.ExecutionTimedOutEventDetails"
    ]
    execution_redriven_event_details: NotRequired[
        "capo_sfn.types.execution_redriven_event_details.ExecutionRedrivenEventDetails"
    ]
    """<p>Contains details about the redrive attempt of an execution.</p>"""
    map_state_started_event_details: NotRequired[
        "capo_sfn.types.map_state_started_event_details.MapStateStartedEventDetails"
    ]
    """<p>Contains details about Map state that was started.</p>"""
    map_iteration_started_event_details: NotRequired[
        "capo_sfn.types.map_iteration_event_details.MapIterationEventDetails"
    ]
    """<p>Contains details about an iteration of a Map state that was started.</p>"""
    map_iteration_succeeded_event_details: NotRequired[
        "capo_sfn.types.map_iteration_event_details.MapIterationEventDetails"
    ]
    """<p>Contains details about an iteration of a Map state that succeeded.</p>"""
    map_iteration_failed_event_details: NotRequired[
        "capo_sfn.types.map_iteration_event_details.MapIterationEventDetails"
    ]
    """<p>Contains details about an iteration of a Map state that failed.</p>"""
    map_iteration_aborted_event_details: NotRequired[
        "capo_sfn.types.map_iteration_event_details.MapIterationEventDetails"
    ]
    """<p>Contains details about an iteration of a Map state that was aborted.</p>"""
    lambda_function_failed_event_details: NotRequired[
        "capo_sfn.types.lambda_function_failed_event_details.LambdaFunctionFailedEventDetails"
    ]
    lambda_function_schedule_failed_event_details: NotRequired[
        "capo_sfn.types.lambda_function_schedule_failed_event_details.LambdaFunctionScheduleFailedEventDetails"
    ]
    lambda_function_scheduled_event_details: NotRequired[
        "capo_sfn.types.lambda_function_scheduled_event_details.LambdaFunctionScheduledEventDetails"
    ]
    lambda_function_start_failed_event_details: NotRequired[
        "capo_sfn.types.lambda_function_start_failed_event_details.LambdaFunctionStartFailedEventDetails"
    ]
    """<p>Contains details about a lambda function that failed to start during an execution.</p>"""
    lambda_function_succeeded_event_details: NotRequired[
        "capo_sfn.types.lambda_function_succeeded_event_details.LambdaFunctionSucceededEventDetails"
    ]
    """<p>Contains details about a Lambda function that terminated successfully during an execution.</p>"""
    lambda_function_timed_out_event_details: NotRequired[
        "capo_sfn.types.lambda_function_timed_out_event_details.LambdaFunctionTimedOutEventDetails"
    ]
    state_entered_event_details: NotRequired[
        "capo_sfn.types.state_entered_event_details.StateEnteredEventDetails"
    ]
    state_exited_event_details: NotRequired[
        "capo_sfn.types.state_exited_event_details.StateExitedEventDetails"
    ]
    map_run_started_event_details: NotRequired[
        "capo_sfn.types.map_run_started_event_details.MapRunStartedEventDetails"
    ]
    """<p>Contains details, such as <code>mapRunArn</code>, and the start date and time of a Map Run. <code>mapRunArn</code> is the Amazon Resource Name (ARN) of the Map Run that was started.</p>"""
    map_run_failed_event_details: NotRequired[
        "capo_sfn.types.map_run_failed_event_details.MapRunFailedEventDetails"
    ]
    """<p>Contains error and cause details about a Map Run that failed.</p>"""
    map_run_redriven_event_details: NotRequired[
        "capo_sfn.types.map_run_redriven_event_details.MapRunRedrivenEventDetails"
    ]
    """<p>Contains details about the redrive attempt of a Map Run.</p>"""
    evaluation_failed_event_details: NotRequired[
        "capo_sfn.types.evaluation_failed_event_details.EvaluationFailedEventDetails"
    ]
    """<p>Contains details about an evaluation failure that occurred while processing a state.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HistoryEvent) -> dict:
    out: dict = {}
    import capo_sfn.types.timestamp

    out["timestamp"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
        value["timestamp"]
    )
    import capo_sfn.types.history_event_type

    out["type"] = capo_sfn.types.history_event_type.serialize_aws_json_1_0(
        value["type"]
    )
    out["id"] = value.get("id", 0)
    out["previousEventId"] = value.get("previous_event_id", 0)
    if "activity_failed_event_details" in value:
        import capo_sfn.types.activity_failed_event_details

        out["activityFailedEventDetails"] = (
            capo_sfn.types.activity_failed_event_details.serialize_aws_json_1_0(
                value["activity_failed_event_details"]
            )
        )
    if "activity_schedule_failed_event_details" in value:
        import capo_sfn.types.activity_schedule_failed_event_details

        out["activityScheduleFailedEventDetails"] = (
            capo_sfn.types.activity_schedule_failed_event_details.serialize_aws_json_1_0(
                value["activity_schedule_failed_event_details"]
            )
        )
    if "activity_scheduled_event_details" in value:
        import capo_sfn.types.activity_scheduled_event_details

        out["activityScheduledEventDetails"] = (
            capo_sfn.types.activity_scheduled_event_details.serialize_aws_json_1_0(
                value["activity_scheduled_event_details"]
            )
        )
    if "activity_started_event_details" in value:
        import capo_sfn.types.activity_started_event_details

        out["activityStartedEventDetails"] = (
            capo_sfn.types.activity_started_event_details.serialize_aws_json_1_0(
                value["activity_started_event_details"]
            )
        )
    if "activity_succeeded_event_details" in value:
        import capo_sfn.types.activity_succeeded_event_details

        out["activitySucceededEventDetails"] = (
            capo_sfn.types.activity_succeeded_event_details.serialize_aws_json_1_0(
                value["activity_succeeded_event_details"]
            )
        )
    if "activity_timed_out_event_details" in value:
        import capo_sfn.types.activity_timed_out_event_details

        out["activityTimedOutEventDetails"] = (
            capo_sfn.types.activity_timed_out_event_details.serialize_aws_json_1_0(
                value["activity_timed_out_event_details"]
            )
        )
    if "task_failed_event_details" in value:
        import capo_sfn.types.task_failed_event_details

        out["taskFailedEventDetails"] = (
            capo_sfn.types.task_failed_event_details.serialize_aws_json_1_0(
                value["task_failed_event_details"]
            )
        )
    if "task_scheduled_event_details" in value:
        import capo_sfn.types.task_scheduled_event_details

        out["taskScheduledEventDetails"] = (
            capo_sfn.types.task_scheduled_event_details.serialize_aws_json_1_0(
                value["task_scheduled_event_details"]
            )
        )
    if "task_start_failed_event_details" in value:
        import capo_sfn.types.task_start_failed_event_details

        out["taskStartFailedEventDetails"] = (
            capo_sfn.types.task_start_failed_event_details.serialize_aws_json_1_0(
                value["task_start_failed_event_details"]
            )
        )
    if "task_started_event_details" in value:
        import capo_sfn.types.task_started_event_details

        out["taskStartedEventDetails"] = (
            capo_sfn.types.task_started_event_details.serialize_aws_json_1_0(
                value["task_started_event_details"]
            )
        )
    if "task_submit_failed_event_details" in value:
        import capo_sfn.types.task_submit_failed_event_details

        out["taskSubmitFailedEventDetails"] = (
            capo_sfn.types.task_submit_failed_event_details.serialize_aws_json_1_0(
                value["task_submit_failed_event_details"]
            )
        )
    if "task_submitted_event_details" in value:
        import capo_sfn.types.task_submitted_event_details

        out["taskSubmittedEventDetails"] = (
            capo_sfn.types.task_submitted_event_details.serialize_aws_json_1_0(
                value["task_submitted_event_details"]
            )
        )
    if "task_succeeded_event_details" in value:
        import capo_sfn.types.task_succeeded_event_details

        out["taskSucceededEventDetails"] = (
            capo_sfn.types.task_succeeded_event_details.serialize_aws_json_1_0(
                value["task_succeeded_event_details"]
            )
        )
    if "task_timed_out_event_details" in value:
        import capo_sfn.types.task_timed_out_event_details

        out["taskTimedOutEventDetails"] = (
            capo_sfn.types.task_timed_out_event_details.serialize_aws_json_1_0(
                value["task_timed_out_event_details"]
            )
        )
    if "execution_failed_event_details" in value:
        import capo_sfn.types.execution_failed_event_details

        out["executionFailedEventDetails"] = (
            capo_sfn.types.execution_failed_event_details.serialize_aws_json_1_0(
                value["execution_failed_event_details"]
            )
        )
    if "execution_started_event_details" in value:
        import capo_sfn.types.execution_started_event_details

        out["executionStartedEventDetails"] = (
            capo_sfn.types.execution_started_event_details.serialize_aws_json_1_0(
                value["execution_started_event_details"]
            )
        )
    if "execution_succeeded_event_details" in value:
        import capo_sfn.types.execution_succeeded_event_details

        out["executionSucceededEventDetails"] = (
            capo_sfn.types.execution_succeeded_event_details.serialize_aws_json_1_0(
                value["execution_succeeded_event_details"]
            )
        )
    if "execution_aborted_event_details" in value:
        import capo_sfn.types.execution_aborted_event_details

        out["executionAbortedEventDetails"] = (
            capo_sfn.types.execution_aborted_event_details.serialize_aws_json_1_0(
                value["execution_aborted_event_details"]
            )
        )
    if "execution_timed_out_event_details" in value:
        import capo_sfn.types.execution_timed_out_event_details

        out["executionTimedOutEventDetails"] = (
            capo_sfn.types.execution_timed_out_event_details.serialize_aws_json_1_0(
                value["execution_timed_out_event_details"]
            )
        )
    if "execution_redriven_event_details" in value:
        import capo_sfn.types.execution_redriven_event_details

        out["executionRedrivenEventDetails"] = (
            capo_sfn.types.execution_redriven_event_details.serialize_aws_json_1_0(
                value["execution_redriven_event_details"]
            )
        )
    if "map_state_started_event_details" in value:
        import capo_sfn.types.map_state_started_event_details

        out["mapStateStartedEventDetails"] = (
            capo_sfn.types.map_state_started_event_details.serialize_aws_json_1_0(
                value["map_state_started_event_details"]
            )
        )
    if "map_iteration_started_event_details" in value:
        import capo_sfn.types.map_iteration_event_details

        out["mapIterationStartedEventDetails"] = (
            capo_sfn.types.map_iteration_event_details.serialize_aws_json_1_0(
                value["map_iteration_started_event_details"]
            )
        )
    if "map_iteration_succeeded_event_details" in value:
        import capo_sfn.types.map_iteration_event_details

        out["mapIterationSucceededEventDetails"] = (
            capo_sfn.types.map_iteration_event_details.serialize_aws_json_1_0(
                value["map_iteration_succeeded_event_details"]
            )
        )
    if "map_iteration_failed_event_details" in value:
        import capo_sfn.types.map_iteration_event_details

        out["mapIterationFailedEventDetails"] = (
            capo_sfn.types.map_iteration_event_details.serialize_aws_json_1_0(
                value["map_iteration_failed_event_details"]
            )
        )
    if "map_iteration_aborted_event_details" in value:
        import capo_sfn.types.map_iteration_event_details

        out["mapIterationAbortedEventDetails"] = (
            capo_sfn.types.map_iteration_event_details.serialize_aws_json_1_0(
                value["map_iteration_aborted_event_details"]
            )
        )
    if "lambda_function_failed_event_details" in value:
        import capo_sfn.types.lambda_function_failed_event_details

        out["lambdaFunctionFailedEventDetails"] = (
            capo_sfn.types.lambda_function_failed_event_details.serialize_aws_json_1_0(
                value["lambda_function_failed_event_details"]
            )
        )
    if "lambda_function_schedule_failed_event_details" in value:
        import capo_sfn.types.lambda_function_schedule_failed_event_details

        out["lambdaFunctionScheduleFailedEventDetails"] = (
            capo_sfn.types.lambda_function_schedule_failed_event_details.serialize_aws_json_1_0(
                value["lambda_function_schedule_failed_event_details"]
            )
        )
    if "lambda_function_scheduled_event_details" in value:
        import capo_sfn.types.lambda_function_scheduled_event_details

        out["lambdaFunctionScheduledEventDetails"] = (
            capo_sfn.types.lambda_function_scheduled_event_details.serialize_aws_json_1_0(
                value["lambda_function_scheduled_event_details"]
            )
        )
    if "lambda_function_start_failed_event_details" in value:
        import capo_sfn.types.lambda_function_start_failed_event_details

        out["lambdaFunctionStartFailedEventDetails"] = (
            capo_sfn.types.lambda_function_start_failed_event_details.serialize_aws_json_1_0(
                value["lambda_function_start_failed_event_details"]
            )
        )
    if "lambda_function_succeeded_event_details" in value:
        import capo_sfn.types.lambda_function_succeeded_event_details

        out["lambdaFunctionSucceededEventDetails"] = (
            capo_sfn.types.lambda_function_succeeded_event_details.serialize_aws_json_1_0(
                value["lambda_function_succeeded_event_details"]
            )
        )
    if "lambda_function_timed_out_event_details" in value:
        import capo_sfn.types.lambda_function_timed_out_event_details

        out["lambdaFunctionTimedOutEventDetails"] = (
            capo_sfn.types.lambda_function_timed_out_event_details.serialize_aws_json_1_0(
                value["lambda_function_timed_out_event_details"]
            )
        )
    if "state_entered_event_details" in value:
        import capo_sfn.types.state_entered_event_details

        out["stateEnteredEventDetails"] = (
            capo_sfn.types.state_entered_event_details.serialize_aws_json_1_0(
                value["state_entered_event_details"]
            )
        )
    if "state_exited_event_details" in value:
        import capo_sfn.types.state_exited_event_details

        out["stateExitedEventDetails"] = (
            capo_sfn.types.state_exited_event_details.serialize_aws_json_1_0(
                value["state_exited_event_details"]
            )
        )
    if "map_run_started_event_details" in value:
        import capo_sfn.types.map_run_started_event_details

        out["mapRunStartedEventDetails"] = (
            capo_sfn.types.map_run_started_event_details.serialize_aws_json_1_0(
                value["map_run_started_event_details"]
            )
        )
    if "map_run_failed_event_details" in value:
        import capo_sfn.types.map_run_failed_event_details

        out["mapRunFailedEventDetails"] = (
            capo_sfn.types.map_run_failed_event_details.serialize_aws_json_1_0(
                value["map_run_failed_event_details"]
            )
        )
    if "map_run_redriven_event_details" in value:
        import capo_sfn.types.map_run_redriven_event_details

        out["mapRunRedrivenEventDetails"] = (
            capo_sfn.types.map_run_redriven_event_details.serialize_aws_json_1_0(
                value["map_run_redriven_event_details"]
            )
        )
    if "evaluation_failed_event_details" in value:
        import capo_sfn.types.evaluation_failed_event_details

        out["evaluationFailedEventDetails"] = (
            capo_sfn.types.evaluation_failed_event_details.serialize_aws_json_1_0(
                value["evaluation_failed_event_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> HistoryEvent:
    out: HistoryEvent = {}  # type: ignore[typeddict-item]
    if "timestamp" in data:
        import capo_sfn.types.timestamp

        out["timestamp"] = capo_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["timestamp"]
        )
    else:
        raise DeserializationError("HistoryEvent.timestamp required")
    if "type" in data:
        import capo_sfn.types.history_event_type

        out["type"] = capo_sfn.types.history_event_type.deserialize_aws_json_1_0(
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
        import capo_sfn.types.activity_failed_event_details

        out["activity_failed_event_details"] = (
            capo_sfn.types.activity_failed_event_details.deserialize_aws_json_1_0(
                data["activityFailedEventDetails"]
            )
        )
    if "activityScheduleFailedEventDetails" in data:
        import capo_sfn.types.activity_schedule_failed_event_details

        out["activity_schedule_failed_event_details"] = (
            capo_sfn.types.activity_schedule_failed_event_details.deserialize_aws_json_1_0(
                data["activityScheduleFailedEventDetails"]
            )
        )
    if "activityScheduledEventDetails" in data:
        import capo_sfn.types.activity_scheduled_event_details

        out["activity_scheduled_event_details"] = (
            capo_sfn.types.activity_scheduled_event_details.deserialize_aws_json_1_0(
                data["activityScheduledEventDetails"]
            )
        )
    if "activityStartedEventDetails" in data:
        import capo_sfn.types.activity_started_event_details

        out["activity_started_event_details"] = (
            capo_sfn.types.activity_started_event_details.deserialize_aws_json_1_0(
                data["activityStartedEventDetails"]
            )
        )
    if "activitySucceededEventDetails" in data:
        import capo_sfn.types.activity_succeeded_event_details

        out["activity_succeeded_event_details"] = (
            capo_sfn.types.activity_succeeded_event_details.deserialize_aws_json_1_0(
                data["activitySucceededEventDetails"]
            )
        )
    if "activityTimedOutEventDetails" in data:
        import capo_sfn.types.activity_timed_out_event_details

        out["activity_timed_out_event_details"] = (
            capo_sfn.types.activity_timed_out_event_details.deserialize_aws_json_1_0(
                data["activityTimedOutEventDetails"]
            )
        )
    if "taskFailedEventDetails" in data:
        import capo_sfn.types.task_failed_event_details

        out["task_failed_event_details"] = (
            capo_sfn.types.task_failed_event_details.deserialize_aws_json_1_0(
                data["taskFailedEventDetails"]
            )
        )
    if "taskScheduledEventDetails" in data:
        import capo_sfn.types.task_scheduled_event_details

        out["task_scheduled_event_details"] = (
            capo_sfn.types.task_scheduled_event_details.deserialize_aws_json_1_0(
                data["taskScheduledEventDetails"]
            )
        )
    if "taskStartFailedEventDetails" in data:
        import capo_sfn.types.task_start_failed_event_details

        out["task_start_failed_event_details"] = (
            capo_sfn.types.task_start_failed_event_details.deserialize_aws_json_1_0(
                data["taskStartFailedEventDetails"]
            )
        )
    if "taskStartedEventDetails" in data:
        import capo_sfn.types.task_started_event_details

        out["task_started_event_details"] = (
            capo_sfn.types.task_started_event_details.deserialize_aws_json_1_0(
                data["taskStartedEventDetails"]
            )
        )
    if "taskSubmitFailedEventDetails" in data:
        import capo_sfn.types.task_submit_failed_event_details

        out["task_submit_failed_event_details"] = (
            capo_sfn.types.task_submit_failed_event_details.deserialize_aws_json_1_0(
                data["taskSubmitFailedEventDetails"]
            )
        )
    if "taskSubmittedEventDetails" in data:
        import capo_sfn.types.task_submitted_event_details

        out["task_submitted_event_details"] = (
            capo_sfn.types.task_submitted_event_details.deserialize_aws_json_1_0(
                data["taskSubmittedEventDetails"]
            )
        )
    if "taskSucceededEventDetails" in data:
        import capo_sfn.types.task_succeeded_event_details

        out["task_succeeded_event_details"] = (
            capo_sfn.types.task_succeeded_event_details.deserialize_aws_json_1_0(
                data["taskSucceededEventDetails"]
            )
        )
    if "taskTimedOutEventDetails" in data:
        import capo_sfn.types.task_timed_out_event_details

        out["task_timed_out_event_details"] = (
            capo_sfn.types.task_timed_out_event_details.deserialize_aws_json_1_0(
                data["taskTimedOutEventDetails"]
            )
        )
    if "executionFailedEventDetails" in data:
        import capo_sfn.types.execution_failed_event_details

        out["execution_failed_event_details"] = (
            capo_sfn.types.execution_failed_event_details.deserialize_aws_json_1_0(
                data["executionFailedEventDetails"]
            )
        )
    if "executionStartedEventDetails" in data:
        import capo_sfn.types.execution_started_event_details

        out["execution_started_event_details"] = (
            capo_sfn.types.execution_started_event_details.deserialize_aws_json_1_0(
                data["executionStartedEventDetails"]
            )
        )
    if "executionSucceededEventDetails" in data:
        import capo_sfn.types.execution_succeeded_event_details

        out["execution_succeeded_event_details"] = (
            capo_sfn.types.execution_succeeded_event_details.deserialize_aws_json_1_0(
                data["executionSucceededEventDetails"]
            )
        )
    if "executionAbortedEventDetails" in data:
        import capo_sfn.types.execution_aborted_event_details

        out["execution_aborted_event_details"] = (
            capo_sfn.types.execution_aborted_event_details.deserialize_aws_json_1_0(
                data["executionAbortedEventDetails"]
            )
        )
    if "executionTimedOutEventDetails" in data:
        import capo_sfn.types.execution_timed_out_event_details

        out["execution_timed_out_event_details"] = (
            capo_sfn.types.execution_timed_out_event_details.deserialize_aws_json_1_0(
                data["executionTimedOutEventDetails"]
            )
        )
    if "executionRedrivenEventDetails" in data:
        import capo_sfn.types.execution_redriven_event_details

        out["execution_redriven_event_details"] = (
            capo_sfn.types.execution_redriven_event_details.deserialize_aws_json_1_0(
                data["executionRedrivenEventDetails"]
            )
        )
    if "mapStateStartedEventDetails" in data:
        import capo_sfn.types.map_state_started_event_details

        out["map_state_started_event_details"] = (
            capo_sfn.types.map_state_started_event_details.deserialize_aws_json_1_0(
                data["mapStateStartedEventDetails"]
            )
        )
    if "mapIterationStartedEventDetails" in data:
        import capo_sfn.types.map_iteration_event_details

        out["map_iteration_started_event_details"] = (
            capo_sfn.types.map_iteration_event_details.deserialize_aws_json_1_0(
                data["mapIterationStartedEventDetails"]
            )
        )
    if "mapIterationSucceededEventDetails" in data:
        import capo_sfn.types.map_iteration_event_details

        out["map_iteration_succeeded_event_details"] = (
            capo_sfn.types.map_iteration_event_details.deserialize_aws_json_1_0(
                data["mapIterationSucceededEventDetails"]
            )
        )
    if "mapIterationFailedEventDetails" in data:
        import capo_sfn.types.map_iteration_event_details

        out["map_iteration_failed_event_details"] = (
            capo_sfn.types.map_iteration_event_details.deserialize_aws_json_1_0(
                data["mapIterationFailedEventDetails"]
            )
        )
    if "mapIterationAbortedEventDetails" in data:
        import capo_sfn.types.map_iteration_event_details

        out["map_iteration_aborted_event_details"] = (
            capo_sfn.types.map_iteration_event_details.deserialize_aws_json_1_0(
                data["mapIterationAbortedEventDetails"]
            )
        )
    if "lambdaFunctionFailedEventDetails" in data:
        import capo_sfn.types.lambda_function_failed_event_details

        out["lambda_function_failed_event_details"] = (
            capo_sfn.types.lambda_function_failed_event_details.deserialize_aws_json_1_0(
                data["lambdaFunctionFailedEventDetails"]
            )
        )
    if "lambdaFunctionScheduleFailedEventDetails" in data:
        import capo_sfn.types.lambda_function_schedule_failed_event_details

        out["lambda_function_schedule_failed_event_details"] = (
            capo_sfn.types.lambda_function_schedule_failed_event_details.deserialize_aws_json_1_0(
                data["lambdaFunctionScheduleFailedEventDetails"]
            )
        )
    if "lambdaFunctionScheduledEventDetails" in data:
        import capo_sfn.types.lambda_function_scheduled_event_details

        out["lambda_function_scheduled_event_details"] = (
            capo_sfn.types.lambda_function_scheduled_event_details.deserialize_aws_json_1_0(
                data["lambdaFunctionScheduledEventDetails"]
            )
        )
    if "lambdaFunctionStartFailedEventDetails" in data:
        import capo_sfn.types.lambda_function_start_failed_event_details

        out["lambda_function_start_failed_event_details"] = (
            capo_sfn.types.lambda_function_start_failed_event_details.deserialize_aws_json_1_0(
                data["lambdaFunctionStartFailedEventDetails"]
            )
        )
    if "lambdaFunctionSucceededEventDetails" in data:
        import capo_sfn.types.lambda_function_succeeded_event_details

        out["lambda_function_succeeded_event_details"] = (
            capo_sfn.types.lambda_function_succeeded_event_details.deserialize_aws_json_1_0(
                data["lambdaFunctionSucceededEventDetails"]
            )
        )
    if "lambdaFunctionTimedOutEventDetails" in data:
        import capo_sfn.types.lambda_function_timed_out_event_details

        out["lambda_function_timed_out_event_details"] = (
            capo_sfn.types.lambda_function_timed_out_event_details.deserialize_aws_json_1_0(
                data["lambdaFunctionTimedOutEventDetails"]
            )
        )
    if "stateEnteredEventDetails" in data:
        import capo_sfn.types.state_entered_event_details

        out["state_entered_event_details"] = (
            capo_sfn.types.state_entered_event_details.deserialize_aws_json_1_0(
                data["stateEnteredEventDetails"]
            )
        )
    if "stateExitedEventDetails" in data:
        import capo_sfn.types.state_exited_event_details

        out["state_exited_event_details"] = (
            capo_sfn.types.state_exited_event_details.deserialize_aws_json_1_0(
                data["stateExitedEventDetails"]
            )
        )
    if "mapRunStartedEventDetails" in data:
        import capo_sfn.types.map_run_started_event_details

        out["map_run_started_event_details"] = (
            capo_sfn.types.map_run_started_event_details.deserialize_aws_json_1_0(
                data["mapRunStartedEventDetails"]
            )
        )
    if "mapRunFailedEventDetails" in data:
        import capo_sfn.types.map_run_failed_event_details

        out["map_run_failed_event_details"] = (
            capo_sfn.types.map_run_failed_event_details.deserialize_aws_json_1_0(
                data["mapRunFailedEventDetails"]
            )
        )
    if "mapRunRedrivenEventDetails" in data:
        import capo_sfn.types.map_run_redriven_event_details

        out["map_run_redriven_event_details"] = (
            capo_sfn.types.map_run_redriven_event_details.deserialize_aws_json_1_0(
                data["mapRunRedrivenEventDetails"]
            )
        )
    if "evaluationFailedEventDetails" in data:
        import capo_sfn.types.evaluation_failed_event_details

        out["evaluation_failed_event_details"] = (
            capo_sfn.types.evaluation_failed_event_details.deserialize_aws_json_1_0(
                data["evaluationFailedEventDetails"]
            )
        )
    return out
