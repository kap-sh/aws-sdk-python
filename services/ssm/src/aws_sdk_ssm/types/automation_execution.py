"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationExecution``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.alarm_configuration
    import aws_sdk_ssm.types.alarm_state_information_list
    import aws_sdk_ssm.types.automation_execution_id
    import aws_sdk_ssm.types.automation_execution_status
    import aws_sdk_ssm.types.automation_parameter_key
    import aws_sdk_ssm.types.automation_parameter_map
    import aws_sdk_ssm.types.automation_subtype
    import aws_sdk_ssm.types.boolean
    import aws_sdk_ssm.types.change_request_name
    import aws_sdk_ssm.types.date_time
    import aws_sdk_ssm.types.document_name
    import aws_sdk_ssm.types.document_version
    import aws_sdk_ssm.types.execution_mode
    import aws_sdk_ssm.types.max_concurrency
    import aws_sdk_ssm.types.max_errors
    import aws_sdk_ssm.types.progress_counters
    import aws_sdk_ssm.types.resolved_targets
    import aws_sdk_ssm.types.runbooks
    import aws_sdk_ssm.types.step_execution_list
    import aws_sdk_ssm.types.string
    import aws_sdk_ssm.types.target_locations
    import aws_sdk_ssm.types.target_locations_url
    import aws_sdk_ssm.types.target_maps
    import aws_sdk_ssm.types.targets


class AutomationExecution(TypedDict):
    automation_execution_id: NotRequired[
        "aws_sdk_ssm.types.automation_execution_id.AutomationExecutionId"
    ]
    """<p>The execution ID.</p>"""
    document_name: NotRequired["aws_sdk_ssm.types.document_name.DocumentName"]
    """<p>The name of the Automation runbook used during the execution.</p>"""
    document_version: NotRequired["aws_sdk_ssm.types.document_version.DocumentVersion"]
    """<p>The version of the document to use during execution.</p>"""
    execution_start_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The time the execution started.</p>"""
    execution_end_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The time the execution finished.</p>"""
    automation_execution_status: NotRequired[
        "aws_sdk_ssm.types.automation_execution_status.AutomationExecutionStatus"
    ]
    """<p>The execution status of the Automation.</p>"""
    step_executions: NotRequired[
        "aws_sdk_ssm.types.step_execution_list.StepExecutionList"
    ]
    """<p>A list of details about the current state of all steps that comprise an execution. An Automation runbook contains a list of steps that are run in order.</p>"""
    step_executions_truncated: "aws_sdk_ssm.types.boolean.Boolean"
    """<p>A boolean value that indicates if the response contains the full list of the Automation step executions. If true, use the DescribeAutomationStepExecutions API operation to get the full list of step executions.</p>"""
    parameters: NotRequired[
        "aws_sdk_ssm.types.automation_parameter_map.AutomationParameterMap"
    ]
    """<p>The key-value map of execution parameters, which were supplied when calling <a>StartAutomationExecution</a>.</p>"""
    outputs: NotRequired[
        "aws_sdk_ssm.types.automation_parameter_map.AutomationParameterMap"
    ]
    """<p>The list of execution outputs as defined in the Automation runbook.</p>"""
    failure_message: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>A message describing why an execution has failed, if the status is set to Failed.</p>"""
    mode: NotRequired["aws_sdk_ssm.types.execution_mode.ExecutionMode"]
    """<p>The automation execution mode.</p>"""
    parent_automation_execution_id: NotRequired[
        "aws_sdk_ssm.types.automation_execution_id.AutomationExecutionId"
    ]
    """<p>The AutomationExecutionId of the parent automation.</p>"""
    executed_by: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the user who ran the automation.</p>"""
    current_step_name: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>The name of the step that is currently running.</p>"""
    current_action: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>The action of the step that is currently running.</p>"""
    target_parameter_name: NotRequired[
        "aws_sdk_ssm.types.automation_parameter_key.AutomationParameterKey"
    ]
    """<p>The parameter name.</p>"""
    targets: NotRequired["aws_sdk_ssm.types.targets.Targets"]
    """<p>The specified targets.</p>"""
    target_maps: NotRequired["aws_sdk_ssm.types.target_maps.TargetMaps"]
    """<p>The specified key-value mapping of document parameters to target resources.</p>"""
    resolved_targets: NotRequired["aws_sdk_ssm.types.resolved_targets.ResolvedTargets"]
    """<p>A list of resolved targets in the rate control execution.</p>"""
    max_concurrency: NotRequired["aws_sdk_ssm.types.max_concurrency.MaxConcurrency"]
    """<p>The <code>MaxConcurrency</code> value specified by the user when the execution started.</p>"""
    max_errors: NotRequired["aws_sdk_ssm.types.max_errors.MaxErrors"]
    """<p>The MaxErrors value specified by the user when the execution started.</p>"""
    target: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>The target of the execution.</p>"""
    target_locations: NotRequired["aws_sdk_ssm.types.target_locations.TargetLocations"]
    """<p>The combination of Amazon Web Services Regions and/or Amazon Web Services accounts where you want to run the Automation.</p>"""
    progress_counters: NotRequired[
        "aws_sdk_ssm.types.progress_counters.ProgressCounters"
    ]
    """<p>An aggregate of step execution statuses displayed in the Amazon Web Services Systems Manager console for a multi-Region and multi-account Automation execution.</p>"""
    alarm_configuration: NotRequired[
        "aws_sdk_ssm.types.alarm_configuration.AlarmConfiguration"
    ]
    """<p>The details for the CloudWatch alarm applied to your automation.</p>"""
    triggered_alarms: NotRequired[
        "aws_sdk_ssm.types.alarm_state_information_list.AlarmStateInformationList"
    ]
    """<p>The CloudWatch alarm that was invoked by the automation.</p>"""
    target_locations_url: NotRequired[
        "aws_sdk_ssm.types.target_locations_url.TargetLocationsURL"
    ]
    """<p>A publicly accessible URL for a file that contains the <code>TargetLocations</code> body. Currently, only files in presigned Amazon S3 buckets are supported</p>"""
    automation_subtype: NotRequired[
        "aws_sdk_ssm.types.automation_subtype.AutomationSubtype"
    ]
    """<p>The subtype of the Automation operation. Currently, the only supported value is <code>ChangeRequest</code>.</p>"""
    scheduled_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The date and time the Automation operation is scheduled to start.</p>"""
    runbooks: NotRequired["aws_sdk_ssm.types.runbooks.Runbooks"]
    """<p>Information about the Automation runbooks that are run as part of a runbook workflow.</p> <note> <p>The Automation runbooks specified for the runbook workflow can't run until all required approvals for the change request have been received.</p> </note>"""
    ops_item_id: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>The ID of an OpsItem that is created to represent a Change Manager change request.</p>"""
    association_id: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>The ID of a State Manager association used in the Automation operation.</p>"""
    change_request_name: NotRequired[
        "aws_sdk_ssm.types.change_request_name.ChangeRequestName"
    ]
    """<p>The name of the Change Manager change request.</p>"""
    variables: NotRequired[
        "aws_sdk_ssm.types.automation_parameter_map.AutomationParameterMap"
    ]
    """<p>Variables defined for the automation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomationExecution) -> dict:
    out: dict = {}
    if "automation_execution_id" in value:
        out["AutomationExecutionId"] = value["automation_execution_id"]
    if "document_name" in value:
        out["DocumentName"] = value["document_name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "execution_start_time" in value:
        import aws_sdk_ssm.types.date_time

        out["ExecutionStartTime"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["execution_start_time"]
        )
    if "execution_end_time" in value:
        import aws_sdk_ssm.types.date_time

        out["ExecutionEndTime"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["execution_end_time"]
        )
    if "automation_execution_status" in value:
        import aws_sdk_ssm.types.automation_execution_status

        out["AutomationExecutionStatus"] = (
            aws_sdk_ssm.types.automation_execution_status.serialize_aws_json_1_1(
                value["automation_execution_status"]
            )
        )
    if "step_executions" in value:
        import aws_sdk_ssm.types.step_execution_list

        out["StepExecutions"] = (
            aws_sdk_ssm.types.step_execution_list.serialize_aws_json_1_1(
                value["step_executions"]
            )
        )
    out["StepExecutionsTruncated"] = value.get("step_executions_truncated", False)
    if "parameters" in value:
        import aws_sdk_ssm.types.automation_parameter_map

        out["Parameters"] = (
            aws_sdk_ssm.types.automation_parameter_map.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    if "outputs" in value:
        import aws_sdk_ssm.types.automation_parameter_map

        out["Outputs"] = (
            aws_sdk_ssm.types.automation_parameter_map.serialize_aws_json_1_1(
                value["outputs"]
            )
        )
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "mode" in value:
        import aws_sdk_ssm.types.execution_mode

        out["Mode"] = aws_sdk_ssm.types.execution_mode.serialize_aws_json_1_1(
            value["mode"]
        )
    if "parent_automation_execution_id" in value:
        out["ParentAutomationExecutionId"] = value["parent_automation_execution_id"]
    if "executed_by" in value:
        out["ExecutedBy"] = value["executed_by"]
    if "current_step_name" in value:
        out["CurrentStepName"] = value["current_step_name"]
    if "current_action" in value:
        out["CurrentAction"] = value["current_action"]
    if "target_parameter_name" in value:
        out["TargetParameterName"] = value["target_parameter_name"]
    if "targets" in value:
        import aws_sdk_ssm.types.targets

        out["Targets"] = aws_sdk_ssm.types.targets.serialize_aws_json_1_1(
            value["targets"]
        )
    if "target_maps" in value:
        import aws_sdk_ssm.types.target_maps

        out["TargetMaps"] = aws_sdk_ssm.types.target_maps.serialize_aws_json_1_1(
            value["target_maps"]
        )
    if "resolved_targets" in value:
        import aws_sdk_ssm.types.resolved_targets

        out["ResolvedTargets"] = (
            aws_sdk_ssm.types.resolved_targets.serialize_aws_json_1_1(
                value["resolved_targets"]
            )
        )
    if "max_concurrency" in value:
        out["MaxConcurrency"] = value["max_concurrency"]
    if "max_errors" in value:
        out["MaxErrors"] = value["max_errors"]
    if "target" in value:
        out["Target"] = value["target"]
    if "target_locations" in value:
        import aws_sdk_ssm.types.target_locations

        out["TargetLocations"] = (
            aws_sdk_ssm.types.target_locations.serialize_aws_json_1_1(
                value["target_locations"]
            )
        )
    if "progress_counters" in value:
        import aws_sdk_ssm.types.progress_counters

        out["ProgressCounters"] = (
            aws_sdk_ssm.types.progress_counters.serialize_aws_json_1_1(
                value["progress_counters"]
            )
        )
    if "alarm_configuration" in value:
        import aws_sdk_ssm.types.alarm_configuration

        out["AlarmConfiguration"] = (
            aws_sdk_ssm.types.alarm_configuration.serialize_aws_json_1_1(
                value["alarm_configuration"]
            )
        )
    if "triggered_alarms" in value:
        import aws_sdk_ssm.types.alarm_state_information_list

        out["TriggeredAlarms"] = (
            aws_sdk_ssm.types.alarm_state_information_list.serialize_aws_json_1_1(
                value["triggered_alarms"]
            )
        )
    if "target_locations_url" in value:
        out["TargetLocationsURL"] = value["target_locations_url"]
    if "automation_subtype" in value:
        import aws_sdk_ssm.types.automation_subtype

        out["AutomationSubtype"] = (
            aws_sdk_ssm.types.automation_subtype.serialize_aws_json_1_1(
                value["automation_subtype"]
            )
        )
    if "scheduled_time" in value:
        import aws_sdk_ssm.types.date_time

        out["ScheduledTime"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["scheduled_time"]
        )
    if "runbooks" in value:
        import aws_sdk_ssm.types.runbooks

        out["Runbooks"] = aws_sdk_ssm.types.runbooks.serialize_aws_json_1_1(
            value["runbooks"]
        )
    if "ops_item_id" in value:
        out["OpsItemId"] = value["ops_item_id"]
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "change_request_name" in value:
        out["ChangeRequestName"] = value["change_request_name"]
    if "variables" in value:
        import aws_sdk_ssm.types.automation_parameter_map

        out["Variables"] = (
            aws_sdk_ssm.types.automation_parameter_map.serialize_aws_json_1_1(
                value["variables"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutomationExecution:
    out: AutomationExecution = {}  # type: ignore[typeddict-item]
    if "AutomationExecutionId" in data:
        out["automation_execution_id"] = data["AutomationExecutionId"]
    if "DocumentName" in data:
        out["document_name"] = data["DocumentName"]
    if "DocumentVersion" in data:
        out["document_version"] = data["DocumentVersion"]
    if "ExecutionStartTime" in data:
        import aws_sdk_ssm.types.date_time

        out["execution_start_time"] = (
            aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
                data["ExecutionStartTime"]
            )
        )
    if "ExecutionEndTime" in data:
        import aws_sdk_ssm.types.date_time

        out["execution_end_time"] = (
            aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
                data["ExecutionEndTime"]
            )
        )
    if "AutomationExecutionStatus" in data:
        import aws_sdk_ssm.types.automation_execution_status

        out["automation_execution_status"] = (
            aws_sdk_ssm.types.automation_execution_status.deserialize_aws_json_1_1(
                data["AutomationExecutionStatus"]
            )
        )
    if "StepExecutions" in data:
        import aws_sdk_ssm.types.step_execution_list

        out["step_executions"] = (
            aws_sdk_ssm.types.step_execution_list.deserialize_aws_json_1_1(
                data["StepExecutions"]
            )
        )
    if "StepExecutionsTruncated" in data:
        out["step_executions_truncated"] = data["StepExecutionsTruncated"]
    else:
        out["step_executions_truncated"] = False
    if "Parameters" in data:
        import aws_sdk_ssm.types.automation_parameter_map

        out["parameters"] = (
            aws_sdk_ssm.types.automation_parameter_map.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if "Outputs" in data:
        import aws_sdk_ssm.types.automation_parameter_map

        out["outputs"] = (
            aws_sdk_ssm.types.automation_parameter_map.deserialize_aws_json_1_1(
                data["Outputs"]
            )
        )
    if "FailureMessage" in data:
        out["failure_message"] = data["FailureMessage"]
    if "Mode" in data:
        import aws_sdk_ssm.types.execution_mode

        out["mode"] = aws_sdk_ssm.types.execution_mode.deserialize_aws_json_1_1(
            data["Mode"]
        )
    if "ParentAutomationExecutionId" in data:
        out["parent_automation_execution_id"] = data["ParentAutomationExecutionId"]
    if "ExecutedBy" in data:
        out["executed_by"] = data["ExecutedBy"]
    if "CurrentStepName" in data:
        out["current_step_name"] = data["CurrentStepName"]
    if "CurrentAction" in data:
        out["current_action"] = data["CurrentAction"]
    if "TargetParameterName" in data:
        out["target_parameter_name"] = data["TargetParameterName"]
    if "Targets" in data:
        import aws_sdk_ssm.types.targets

        out["targets"] = aws_sdk_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if "TargetMaps" in data:
        import aws_sdk_ssm.types.target_maps

        out["target_maps"] = aws_sdk_ssm.types.target_maps.deserialize_aws_json_1_1(
            data["TargetMaps"]
        )
    if "ResolvedTargets" in data:
        import aws_sdk_ssm.types.resolved_targets

        out["resolved_targets"] = (
            aws_sdk_ssm.types.resolved_targets.deserialize_aws_json_1_1(
                data["ResolvedTargets"]
            )
        )
    if "MaxConcurrency" in data:
        out["max_concurrency"] = data["MaxConcurrency"]
    if "MaxErrors" in data:
        out["max_errors"] = data["MaxErrors"]
    if "Target" in data:
        out["target"] = data["Target"]
    if "TargetLocations" in data:
        import aws_sdk_ssm.types.target_locations

        out["target_locations"] = (
            aws_sdk_ssm.types.target_locations.deserialize_aws_json_1_1(
                data["TargetLocations"]
            )
        )
    if "ProgressCounters" in data:
        import aws_sdk_ssm.types.progress_counters

        out["progress_counters"] = (
            aws_sdk_ssm.types.progress_counters.deserialize_aws_json_1_1(
                data["ProgressCounters"]
            )
        )
    if "AlarmConfiguration" in data:
        import aws_sdk_ssm.types.alarm_configuration

        out["alarm_configuration"] = (
            aws_sdk_ssm.types.alarm_configuration.deserialize_aws_json_1_1(
                data["AlarmConfiguration"]
            )
        )
    if "TriggeredAlarms" in data:
        import aws_sdk_ssm.types.alarm_state_information_list

        out["triggered_alarms"] = (
            aws_sdk_ssm.types.alarm_state_information_list.deserialize_aws_json_1_1(
                data["TriggeredAlarms"]
            )
        )
    if "TargetLocationsURL" in data:
        out["target_locations_url"] = data["TargetLocationsURL"]
    if "AutomationSubtype" in data:
        import aws_sdk_ssm.types.automation_subtype

        out["automation_subtype"] = (
            aws_sdk_ssm.types.automation_subtype.deserialize_aws_json_1_1(
                data["AutomationSubtype"]
            )
        )
    if "ScheduledTime" in data:
        import aws_sdk_ssm.types.date_time

        out["scheduled_time"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ScheduledTime"]
        )
    if "Runbooks" in data:
        import aws_sdk_ssm.types.runbooks

        out["runbooks"] = aws_sdk_ssm.types.runbooks.deserialize_aws_json_1_1(
            data["Runbooks"]
        )
    if "OpsItemId" in data:
        out["ops_item_id"] = data["OpsItemId"]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    if "ChangeRequestName" in data:
        out["change_request_name"] = data["ChangeRequestName"]
    if "Variables" in data:
        import aws_sdk_ssm.types.automation_parameter_map

        out["variables"] = (
            aws_sdk_ssm.types.automation_parameter_map.deserialize_aws_json_1_1(
                data["Variables"]
            )
        )
    return out
