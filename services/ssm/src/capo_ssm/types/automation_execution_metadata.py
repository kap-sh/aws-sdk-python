"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationExecutionMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.alarm_configuration
    import capo_ssm.types.alarm_state_information_list
    import capo_ssm.types.automation_execution_id
    import capo_ssm.types.automation_execution_status
    import capo_ssm.types.automation_parameter_key
    import capo_ssm.types.automation_parameter_map
    import capo_ssm.types.automation_subtype
    import capo_ssm.types.automation_type
    import capo_ssm.types.change_request_name
    import capo_ssm.types.date_time
    import capo_ssm.types.document_name
    import capo_ssm.types.document_version
    import capo_ssm.types.execution_mode
    import capo_ssm.types.max_concurrency
    import capo_ssm.types.max_errors
    import capo_ssm.types.resolved_targets
    import capo_ssm.types.runbooks
    import capo_ssm.types.string
    import capo_ssm.types.target_locations_url
    import capo_ssm.types.target_maps
    import capo_ssm.types.targets


class AutomationExecutionMetadata(TypedDict, closed=True):
    automation_execution_id: NotRequired[
        "capo_ssm.types.automation_execution_id.AutomationExecutionId"
    ]
    """<p>The execution ID.</p>"""
    document_name: NotRequired["capo_ssm.types.document_name.DocumentName"]
    """<p>The name of the Automation runbook used during execution.</p>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The document version used during the execution.</p>"""
    automation_execution_status: NotRequired[
        "capo_ssm.types.automation_execution_status.AutomationExecutionStatus"
    ]
    """<p>The status of the execution.</p>"""
    execution_start_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time the execution started.</p>"""
    execution_end_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time the execution finished. This isn't populated if the execution is still in progress.</p>"""
    executed_by: NotRequired["capo_ssm.types.string.String"]
    """<p>The IAM role ARN of the user who ran the automation.</p>"""
    log_file: NotRequired["capo_ssm.types.string.String"]
    """<p>An S3 bucket where execution information is stored.</p>"""
    outputs: NotRequired[
        "capo_ssm.types.automation_parameter_map.AutomationParameterMap"
    ]
    """<p>The list of execution outputs as defined in the Automation runbook.</p>"""
    mode: NotRequired["capo_ssm.types.execution_mode.ExecutionMode"]
    """<p>The Automation execution mode.</p>"""
    parent_automation_execution_id: NotRequired[
        "capo_ssm.types.automation_execution_id.AutomationExecutionId"
    ]
    """<p>The execution ID of the parent automation.</p>"""
    current_step_name: NotRequired["capo_ssm.types.string.String"]
    """<p>The name of the step that is currently running.</p>"""
    current_action: NotRequired["capo_ssm.types.string.String"]
    """<p>The action of the step that is currently running.</p>"""
    failure_message: NotRequired["capo_ssm.types.string.String"]
    """<p>The list of execution outputs as defined in the Automation runbook.</p>"""
    target_parameter_name: NotRequired[
        "capo_ssm.types.automation_parameter_key.AutomationParameterKey"
    ]
    """<p>The list of execution outputs as defined in the Automation runbook.</p>"""
    targets: NotRequired["capo_ssm.types.targets.Targets"]
    """<p>The targets defined by the user when starting the automation.</p>"""
    target_maps: NotRequired["capo_ssm.types.target_maps.TargetMaps"]
    """<p>The specified key-value mapping of document parameters to target resources.</p>"""
    resolved_targets: NotRequired["capo_ssm.types.resolved_targets.ResolvedTargets"]
    """<p>A list of targets that resolved during the execution.</p>"""
    max_concurrency: NotRequired["capo_ssm.types.max_concurrency.MaxConcurrency"]
    """<p>The <code>MaxConcurrency</code> value specified by the user when starting the automation.</p>"""
    max_errors: NotRequired["capo_ssm.types.max_errors.MaxErrors"]
    """<p>The <code>MaxErrors</code> value specified by the user when starting the automation.</p>"""
    target: NotRequired["capo_ssm.types.string.String"]
    """<p>The list of execution outputs as defined in the Automation runbook.</p>"""
    automation_type: NotRequired["capo_ssm.types.automation_type.AutomationType"]
    r"""<p>Use this filter with <a>DescribeAutomationExecutions</a>. Specify either Local or CrossAccount. CrossAccount is an Automation that runs in multiple Amazon Web Services Regions and Amazon Web Services accounts. For more information, see <a href=\"https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation-multiple-accounts-and-regions.html\">Running automations in multiple Amazon Web Services Regions and accounts</a> in the <i>Amazon Web Services Systems Manager User Guide</i>. </p>"""
    alarm_configuration: NotRequired[
        "capo_ssm.types.alarm_configuration.AlarmConfiguration"
    ]
    """<p>The details for the CloudWatch alarm applied to your automation.</p>"""
    triggered_alarms: NotRequired[
        "capo_ssm.types.alarm_state_information_list.AlarmStateInformationList"
    ]
    """<p>The CloudWatch alarm that was invoked by the automation.</p>"""
    target_locations_url: NotRequired[
        "capo_ssm.types.target_locations_url.TargetLocationsURL"
    ]
    """<p>A publicly accessible URL for a file that contains the <code>TargetLocations</code> body. Currently, only files in presigned Amazon S3 buckets are supported</p>"""
    automation_subtype: NotRequired[
        "capo_ssm.types.automation_subtype.AutomationSubtype"
    ]
    """<p>The subtype of the Automation operation. Currently, the only supported value is <code>ChangeRequest</code>.</p>"""
    scheduled_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date and time the Automation operation is scheduled to start.</p>"""
    runbooks: NotRequired["capo_ssm.types.runbooks.Runbooks"]
    """<p>Information about the Automation runbooks that are run during a runbook workflow in Change Manager.</p> <note> <p>The Automation runbooks specified for the runbook workflow can't run until all required approvals for the change request have been received.</p> </note>"""
    ops_item_id: NotRequired["capo_ssm.types.string.String"]
    """<p>The ID of an OpsItem that is created to represent a Change Manager change request.</p>"""
    association_id: NotRequired["capo_ssm.types.string.String"]
    """<p>The ID of a State Manager association used in the Automation operation.</p>"""
    change_request_name: NotRequired[
        "capo_ssm.types.change_request_name.ChangeRequestName"
    ]
    """<p>The name of the Change Manager change request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomationExecutionMetadata) -> dict:
    out: dict = {}
    if "automation_execution_id" in value:
        out["AutomationExecutionId"] = value["automation_execution_id"]
    if "document_name" in value:
        out["DocumentName"] = value["document_name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "automation_execution_status" in value:
        import capo_ssm.types.automation_execution_status

        out["AutomationExecutionStatus"] = (
            capo_ssm.types.automation_execution_status.serialize_aws_json_1_1(
                value["automation_execution_status"]
            )
        )
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
    if "executed_by" in value:
        out["ExecutedBy"] = value["executed_by"]
    if "log_file" in value:
        out["LogFile"] = value["log_file"]
    if "outputs" in value:
        import capo_ssm.types.automation_parameter_map

        out["Outputs"] = capo_ssm.types.automation_parameter_map.serialize_aws_json_1_1(
            value["outputs"]
        )
    if "mode" in value:
        import capo_ssm.types.execution_mode

        out["Mode"] = capo_ssm.types.execution_mode.serialize_aws_json_1_1(
            value["mode"]
        )
    if "parent_automation_execution_id" in value:
        out["ParentAutomationExecutionId"] = value["parent_automation_execution_id"]
    if "current_step_name" in value:
        out["CurrentStepName"] = value["current_step_name"]
    if "current_action" in value:
        out["CurrentAction"] = value["current_action"]
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "target_parameter_name" in value:
        out["TargetParameterName"] = value["target_parameter_name"]
    if "targets" in value:
        import capo_ssm.types.targets

        out["Targets"] = capo_ssm.types.targets.serialize_aws_json_1_1(value["targets"])
    if "target_maps" in value:
        import capo_ssm.types.target_maps

        out["TargetMaps"] = capo_ssm.types.target_maps.serialize_aws_json_1_1(
            value["target_maps"]
        )
    if "resolved_targets" in value:
        import capo_ssm.types.resolved_targets

        out["ResolvedTargets"] = capo_ssm.types.resolved_targets.serialize_aws_json_1_1(
            value["resolved_targets"]
        )
    if "max_concurrency" in value:
        out["MaxConcurrency"] = value["max_concurrency"]
    if "max_errors" in value:
        out["MaxErrors"] = value["max_errors"]
    if "target" in value:
        out["Target"] = value["target"]
    if "automation_type" in value:
        import capo_ssm.types.automation_type

        out["AutomationType"] = capo_ssm.types.automation_type.serialize_aws_json_1_1(
            value["automation_type"]
        )
    if "alarm_configuration" in value:
        import capo_ssm.types.alarm_configuration

        out["AlarmConfiguration"] = (
            capo_ssm.types.alarm_configuration.serialize_aws_json_1_1(
                value["alarm_configuration"]
            )
        )
    if "triggered_alarms" in value:
        import capo_ssm.types.alarm_state_information_list

        out["TriggeredAlarms"] = (
            capo_ssm.types.alarm_state_information_list.serialize_aws_json_1_1(
                value["triggered_alarms"]
            )
        )
    if "target_locations_url" in value:
        out["TargetLocationsURL"] = value["target_locations_url"]
    if "automation_subtype" in value:
        import capo_ssm.types.automation_subtype

        out["AutomationSubtype"] = (
            capo_ssm.types.automation_subtype.serialize_aws_json_1_1(
                value["automation_subtype"]
            )
        )
    if "scheduled_time" in value:
        import capo_ssm.types.date_time

        out["ScheduledTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["scheduled_time"]
        )
    if "runbooks" in value:
        import capo_ssm.types.runbooks

        out["Runbooks"] = capo_ssm.types.runbooks.serialize_aws_json_1_1(
            value["runbooks"]
        )
    if "ops_item_id" in value:
        out["OpsItemId"] = value["ops_item_id"]
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "change_request_name" in value:
        out["ChangeRequestName"] = value["change_request_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutomationExecutionMetadata:
    out: AutomationExecutionMetadata = {}  # type: ignore[typeddict-item]
    if "AutomationExecutionId" in data:
        out["automation_execution_id"] = data["AutomationExecutionId"]
    if "DocumentName" in data:
        out["document_name"] = data["DocumentName"]
    if "DocumentVersion" in data:
        out["document_version"] = data["DocumentVersion"]
    if "AutomationExecutionStatus" in data:
        import capo_ssm.types.automation_execution_status

        out["automation_execution_status"] = (
            capo_ssm.types.automation_execution_status.deserialize_aws_json_1_1(
                data["AutomationExecutionStatus"]
            )
        )
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
    if "ExecutedBy" in data:
        out["executed_by"] = data["ExecutedBy"]
    if "LogFile" in data:
        out["log_file"] = data["LogFile"]
    if "Outputs" in data:
        import capo_ssm.types.automation_parameter_map

        out["outputs"] = (
            capo_ssm.types.automation_parameter_map.deserialize_aws_json_1_1(
                data["Outputs"]
            )
        )
    if "Mode" in data:
        import capo_ssm.types.execution_mode

        out["mode"] = capo_ssm.types.execution_mode.deserialize_aws_json_1_1(
            data["Mode"]
        )
    if "ParentAutomationExecutionId" in data:
        out["parent_automation_execution_id"] = data["ParentAutomationExecutionId"]
    if "CurrentStepName" in data:
        out["current_step_name"] = data["CurrentStepName"]
    if "CurrentAction" in data:
        out["current_action"] = data["CurrentAction"]
    if "FailureMessage" in data:
        out["failure_message"] = data["FailureMessage"]
    if "TargetParameterName" in data:
        out["target_parameter_name"] = data["TargetParameterName"]
    if "Targets" in data:
        import capo_ssm.types.targets

        out["targets"] = capo_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if "TargetMaps" in data:
        import capo_ssm.types.target_maps

        out["target_maps"] = capo_ssm.types.target_maps.deserialize_aws_json_1_1(
            data["TargetMaps"]
        )
    if "ResolvedTargets" in data:
        import capo_ssm.types.resolved_targets

        out["resolved_targets"] = (
            capo_ssm.types.resolved_targets.deserialize_aws_json_1_1(
                data["ResolvedTargets"]
            )
        )
    if "MaxConcurrency" in data:
        out["max_concurrency"] = data["MaxConcurrency"]
    if "MaxErrors" in data:
        out["max_errors"] = data["MaxErrors"]
    if "Target" in data:
        out["target"] = data["Target"]
    if "AutomationType" in data:
        import capo_ssm.types.automation_type

        out["automation_type"] = (
            capo_ssm.types.automation_type.deserialize_aws_json_1_1(
                data["AutomationType"]
            )
        )
    if "AlarmConfiguration" in data:
        import capo_ssm.types.alarm_configuration

        out["alarm_configuration"] = (
            capo_ssm.types.alarm_configuration.deserialize_aws_json_1_1(
                data["AlarmConfiguration"]
            )
        )
    if "TriggeredAlarms" in data:
        import capo_ssm.types.alarm_state_information_list

        out["triggered_alarms"] = (
            capo_ssm.types.alarm_state_information_list.deserialize_aws_json_1_1(
                data["TriggeredAlarms"]
            )
        )
    if "TargetLocationsURL" in data:
        out["target_locations_url"] = data["TargetLocationsURL"]
    if "AutomationSubtype" in data:
        import capo_ssm.types.automation_subtype

        out["automation_subtype"] = (
            capo_ssm.types.automation_subtype.deserialize_aws_json_1_1(
                data["AutomationSubtype"]
            )
        )
    if "ScheduledTime" in data:
        import capo_ssm.types.date_time

        out["scheduled_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ScheduledTime"]
        )
    if "Runbooks" in data:
        import capo_ssm.types.runbooks

        out["runbooks"] = capo_ssm.types.runbooks.deserialize_aws_json_1_1(
            data["Runbooks"]
        )
    if "OpsItemId" in data:
        out["ops_item_id"] = data["OpsItemId"]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    if "ChangeRequestName" in data:
        out["change_request_name"] = data["ChangeRequestName"]
    return out
