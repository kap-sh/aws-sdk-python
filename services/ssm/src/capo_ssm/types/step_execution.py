"""Generated from Smithy shape ``com.amazonaws.ssm#StepExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.alarm_state_information_list
    import capo_ssm.types.automation_action_name
    import capo_ssm.types.automation_execution_status
    import capo_ssm.types.automation_parameter_map
    import capo_ssm.types.boolean
    import capo_ssm.types.date_time
    import capo_ssm.types.failure_details
    import capo_ssm.types.integer
    import capo_ssm.types.long
    import capo_ssm.types.normal_string_map
    import capo_ssm.types.parent_step_details
    import capo_ssm.types.string
    import capo_ssm.types.target_location
    import capo_ssm.types.targets
    import capo_ssm.types.valid_next_step_list


class StepExecution(TypedDict, closed=True):
    step_name: NotRequired["capo_ssm.types.string.String"]
    """<p>The name of this execution step.</p>"""
    action: NotRequired["capo_ssm.types.automation_action_name.AutomationActionName"]
    """<p>The action this step performs. The action determines the behavior of the step.</p>"""
    timeout_seconds: NotRequired["capo_ssm.types.long.Long"]
    """<p>The timeout seconds of the step.</p>"""
    on_failure: NotRequired["capo_ssm.types.string.String"]
    """<p>The action to take if the step fails. The default value is <code>Abort</code>.</p>"""
    max_attempts: NotRequired["capo_ssm.types.integer.Integer"]
    """<p>The maximum number of tries to run the action of the step. The default value is <code>1</code>.</p>"""
    execution_start_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>If a step has begun execution, this contains the time the step started. If the step is in Pending status, this field isn't populated.</p>"""
    execution_end_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>If a step has finished execution, this contains the time the execution ended. If the step hasn't yet concluded, this field isn't populated.</p>"""
    step_status: NotRequired[
        "capo_ssm.types.automation_execution_status.AutomationExecutionStatus"
    ]
    """<p>The execution status for this step.</p>"""
    response_code: NotRequired["capo_ssm.types.string.String"]
    """<p>The response code returned by the execution of the step.</p>"""
    inputs: NotRequired["capo_ssm.types.normal_string_map.NormalStringMap"]
    """<p>Fully-resolved values passed into the step before execution.</p>"""
    outputs: NotRequired[
        "capo_ssm.types.automation_parameter_map.AutomationParameterMap"
    ]
    """<p>Returned values from the execution of the step.</p>"""
    response: NotRequired["capo_ssm.types.string.String"]
    """<p>A message associated with the response code for an execution.</p>"""
    failure_message: NotRequired["capo_ssm.types.string.String"]
    """<p>If a step failed, this message explains why the execution failed.</p>"""
    failure_details: NotRequired["capo_ssm.types.failure_details.FailureDetails"]
    """<p>Information about the Automation failure.</p>"""
    step_execution_id: NotRequired["capo_ssm.types.string.String"]
    """<p>The unique ID of a step execution.</p>"""
    overridden_parameters: NotRequired[
        "capo_ssm.types.automation_parameter_map.AutomationParameterMap"
    ]
    """<p>A user-specified list of parameters to override when running a step.</p>"""
    is_end: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>The flag which can be used to end automation no matter whether the step succeeds or fails.</p>"""
    next_step: NotRequired["capo_ssm.types.string.String"]
    """<p>The next step after the step succeeds.</p>"""
    is_critical: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>The flag which can be used to help decide whether the failure of current step leads to the Automation failure.</p>"""
    valid_next_steps: NotRequired[
        "capo_ssm.types.valid_next_step_list.ValidNextStepList"
    ]
    """<p>Strategies used when step fails, we support Continue and Abort. Abort will fail the automation when the step fails. Continue will ignore the failure of current step and allow automation to run the next step. With conditional branching, we add step:stepName to support the automation to go to another specific step.</p>"""
    targets: NotRequired["capo_ssm.types.targets.Targets"]
    """<p>The targets for the step execution.</p>"""
    target_location: NotRequired["capo_ssm.types.target_location.TargetLocation"]
    """<p>The combination of Amazon Web Services Regions and Amazon Web Services accounts targeted by the current Automation execution.</p>"""
    triggered_alarms: NotRequired[
        "capo_ssm.types.alarm_state_information_list.AlarmStateInformationList"
    ]
    """<p>The CloudWatch alarms that were invoked by the automation.</p>"""
    parent_step_details: NotRequired[
        "capo_ssm.types.parent_step_details.ParentStepDetails"
    ]
    """<p>Information about the parent step.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepExecution) -> dict:
    out: dict = {}
    if "step_name" in value:
        out["StepName"] = value["step_name"]
    if "action" in value:
        out["Action"] = value["action"]
    if "timeout_seconds" in value:
        out["TimeoutSeconds"] = value["timeout_seconds"]
    if "on_failure" in value:
        out["OnFailure"] = value["on_failure"]
    if "max_attempts" in value:
        out["MaxAttempts"] = value["max_attempts"]
    if "execution_start_time" in value:
        import capo_ssm.types.date_time

        out["ExecutionStartTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["execution_start_time"]
        )
    if "execution_end_time" in value:
        import capo_ssm.types.date_time

        out["ExecutionEndTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["execution_end_time"]
        )
    if "step_status" in value:
        import capo_ssm.types.automation_execution_status

        out["StepStatus"] = (
            capo_ssm.types.automation_execution_status.serialize_aws_json_1_1(
                value["step_status"]
            )
        )
    if "response_code" in value:
        out["ResponseCode"] = value["response_code"]
    if "inputs" in value:
        import capo_ssm.types.normal_string_map

        out["Inputs"] = capo_ssm.types.normal_string_map.serialize_aws_json_1_1(
            value["inputs"]
        )
    if "outputs" in value:
        import capo_ssm.types.automation_parameter_map

        out["Outputs"] = capo_ssm.types.automation_parameter_map.serialize_aws_json_1_1(
            value["outputs"]
        )
    if "response" in value:
        out["Response"] = value["response"]
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "failure_details" in value:
        import capo_ssm.types.failure_details

        out["FailureDetails"] = capo_ssm.types.failure_details.serialize_aws_json_1_1(
            value["failure_details"]
        )
    if "step_execution_id" in value:
        out["StepExecutionId"] = value["step_execution_id"]
    if "overridden_parameters" in value:
        import capo_ssm.types.automation_parameter_map

        out["OverriddenParameters"] = (
            capo_ssm.types.automation_parameter_map.serialize_aws_json_1_1(
                value["overridden_parameters"]
            )
        )
    if "is_end" in value:
        out["IsEnd"] = value["is_end"]
    if "next_step" in value:
        out["NextStep"] = value["next_step"]
    if "is_critical" in value:
        out["IsCritical"] = value["is_critical"]
    if "valid_next_steps" in value:
        import capo_ssm.types.valid_next_step_list

        out["ValidNextSteps"] = (
            capo_ssm.types.valid_next_step_list.serialize_aws_json_1_1(
                value["valid_next_steps"]
            )
        )
    if "targets" in value:
        import capo_ssm.types.targets

        out["Targets"] = capo_ssm.types.targets.serialize_aws_json_1_1(value["targets"])
    if "target_location" in value:
        import capo_ssm.types.target_location

        out["TargetLocation"] = capo_ssm.types.target_location.serialize_aws_json_1_1(
            value["target_location"]
        )
    if "triggered_alarms" in value:
        import capo_ssm.types.alarm_state_information_list

        out["TriggeredAlarms"] = (
            capo_ssm.types.alarm_state_information_list.serialize_aws_json_1_1(
                value["triggered_alarms"]
            )
        )
    if "parent_step_details" in value:
        import capo_ssm.types.parent_step_details

        out["ParentStepDetails"] = (
            capo_ssm.types.parent_step_details.serialize_aws_json_1_1(
                value["parent_step_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StepExecution:
    out: StepExecution = {}  # type: ignore[typeddict-item]
    if "StepName" in data:
        out["step_name"] = data["StepName"]
    if "Action" in data:
        out["action"] = data["Action"]
    if "TimeoutSeconds" in data:
        out["timeout_seconds"] = data["TimeoutSeconds"]
    if "OnFailure" in data:
        out["on_failure"] = data["OnFailure"]
    if "MaxAttempts" in data:
        out["max_attempts"] = data["MaxAttempts"]
    if "ExecutionStartTime" in data:
        import capo_ssm.types.date_time

        out["execution_start_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ExecutionStartTime"]
        )
    if "ExecutionEndTime" in data:
        import capo_ssm.types.date_time

        out["execution_end_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ExecutionEndTime"]
        )
    if "StepStatus" in data:
        import capo_ssm.types.automation_execution_status

        out["step_status"] = (
            capo_ssm.types.automation_execution_status.deserialize_aws_json_1_1(
                data["StepStatus"]
            )
        )
    if "ResponseCode" in data:
        out["response_code"] = data["ResponseCode"]
    if "Inputs" in data:
        import capo_ssm.types.normal_string_map

        out["inputs"] = capo_ssm.types.normal_string_map.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    if "Outputs" in data:
        import capo_ssm.types.automation_parameter_map

        out["outputs"] = (
            capo_ssm.types.automation_parameter_map.deserialize_aws_json_1_1(
                data["Outputs"]
            )
        )
    if "Response" in data:
        out["response"] = data["Response"]
    if "FailureMessage" in data:
        out["failure_message"] = data["FailureMessage"]
    if "FailureDetails" in data:
        import capo_ssm.types.failure_details

        out["failure_details"] = (
            capo_ssm.types.failure_details.deserialize_aws_json_1_1(
                data["FailureDetails"]
            )
        )
    if "StepExecutionId" in data:
        out["step_execution_id"] = data["StepExecutionId"]
    if "OverriddenParameters" in data:
        import capo_ssm.types.automation_parameter_map

        out["overridden_parameters"] = (
            capo_ssm.types.automation_parameter_map.deserialize_aws_json_1_1(
                data["OverriddenParameters"]
            )
        )
    if "IsEnd" in data:
        out["is_end"] = data["IsEnd"]
    if "NextStep" in data:
        out["next_step"] = data["NextStep"]
    if "IsCritical" in data:
        out["is_critical"] = data["IsCritical"]
    if "ValidNextSteps" in data:
        import capo_ssm.types.valid_next_step_list

        out["valid_next_steps"] = (
            capo_ssm.types.valid_next_step_list.deserialize_aws_json_1_1(
                data["ValidNextSteps"]
            )
        )
    if "Targets" in data:
        import capo_ssm.types.targets

        out["targets"] = capo_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if "TargetLocation" in data:
        import capo_ssm.types.target_location

        out["target_location"] = (
            capo_ssm.types.target_location.deserialize_aws_json_1_1(
                data["TargetLocation"]
            )
        )
    if "TriggeredAlarms" in data:
        import capo_ssm.types.alarm_state_information_list

        out["triggered_alarms"] = (
            capo_ssm.types.alarm_state_information_list.deserialize_aws_json_1_1(
                data["TriggeredAlarms"]
            )
        )
    if "ParentStepDetails" in data:
        import capo_ssm.types.parent_step_details

        out["parent_step_details"] = (
            capo_ssm.types.parent_step_details.deserialize_aws_json_1_1(
                data["ParentStepDetails"]
            )
        )
    return out
