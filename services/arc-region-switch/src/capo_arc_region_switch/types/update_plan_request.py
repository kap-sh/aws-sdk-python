"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#UpdatePlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_arc_region_switch.types.associated_alarm_map
    import capo_arc_region_switch.types.iam_role_arn
    import capo_arc_region_switch.types.plan_arn
    import capo_arc_region_switch.types.report_configuration
    import capo_arc_region_switch.types.trigger_list
    import capo_arc_region_switch.types.workflow_list


class UpdatePlanRequest(TypedDict, closed=True):
    arn: "capo_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan.</p>"""
    description: NotRequired["str"]
    """<p>The updated description for the Region switch plan.</p>"""
    workflows: "capo_arc_region_switch.types.workflow_list.WorkflowList"
    """<p>The updated workflows for the Region switch plan.</p>"""
    execution_role: "capo_arc_region_switch.types.iam_role_arn.IamRoleArn"
    """<p>The updated IAM role ARN that grants Region switch the permissions needed to execute the plan steps.</p>"""
    recovery_time_objective_minutes: NotRequired["int"]
    """<p>The updated target recovery time objective (RTO) in minutes for the plan.</p>"""
    associated_alarms: NotRequired[
        "capo_arc_region_switch.types.associated_alarm_map.AssociatedAlarmMap"
    ]
    """<p>The updated CloudWatch alarms associated with the plan.</p>"""
    triggers: NotRequired["capo_arc_region_switch.types.trigger_list.TriggerList"]
    """<p>The updated conditions that can automatically trigger the execution of the plan.</p>"""
    report_configuration: NotRequired[
        "capo_arc_region_switch.types.report_configuration.ReportConfiguration"
    ]
    """<p>The updated report configuration for the plan.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePlanRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_arc_region_switch.types.workflow_list

    out["workflows"] = (
        capo_arc_region_switch.types.workflow_list.serialize_aws_json_1_0(
            value["workflows"]
        )
    )
    out["executionRole"] = value["execution_role"]
    if "recovery_time_objective_minutes" in value:
        out["recoveryTimeObjectiveMinutes"] = value["recovery_time_objective_minutes"]
    if "associated_alarms" in value:
        import capo_arc_region_switch.types.associated_alarm_map

        out["associatedAlarms"] = (
            capo_arc_region_switch.types.associated_alarm_map.serialize_aws_json_1_0(
                value["associated_alarms"]
            )
        )
    if "triggers" in value:
        import capo_arc_region_switch.types.trigger_list

        out["triggers"] = (
            capo_arc_region_switch.types.trigger_list.serialize_aws_json_1_0(
                value["triggers"]
            )
        )
    if "report_configuration" in value:
        import capo_arc_region_switch.types.report_configuration

        out["reportConfiguration"] = (
            capo_arc_region_switch.types.report_configuration.serialize_aws_json_1_0(
                value["report_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdatePlanRequest:
    out: UpdatePlanRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdatePlanRequest.arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "workflows" in data:
        import capo_arc_region_switch.types.workflow_list

        out["workflows"] = (
            capo_arc_region_switch.types.workflow_list.deserialize_aws_json_1_0(
                data["workflows"]
            )
        )
    else:
        raise DeserializationError("UpdatePlanRequest.workflows required")
    if "executionRole" in data:
        out["execution_role"] = data["executionRole"]
    else:
        raise DeserializationError("UpdatePlanRequest.execution_role required")
    if "recoveryTimeObjectiveMinutes" in data:
        out["recovery_time_objective_minutes"] = data["recoveryTimeObjectiveMinutes"]
    if "associatedAlarms" in data:
        import capo_arc_region_switch.types.associated_alarm_map

        out["associated_alarms"] = (
            capo_arc_region_switch.types.associated_alarm_map.deserialize_aws_json_1_0(
                data["associatedAlarms"]
            )
        )
    if "triggers" in data:
        import capo_arc_region_switch.types.trigger_list

        out["triggers"] = (
            capo_arc_region_switch.types.trigger_list.deserialize_aws_json_1_0(
                data["triggers"]
            )
        )
    if "reportConfiguration" in data:
        import capo_arc_region_switch.types.report_configuration

        out["report_configuration"] = (
            capo_arc_region_switch.types.report_configuration.deserialize_aws_json_1_0(
                data["reportConfiguration"]
            )
        )
    return out
