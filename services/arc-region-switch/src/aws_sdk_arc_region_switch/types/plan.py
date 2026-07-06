"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Plan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_arc_region_switch.types.account_id
    import aws_sdk_arc_region_switch.types.associated_alarm_map
    import aws_sdk_arc_region_switch.types.iam_role_arn
    import aws_sdk_arc_region_switch.types.plan_arn
    import aws_sdk_arc_region_switch.types.plan_name
    import aws_sdk_arc_region_switch.types.recovery_approach
    import aws_sdk_arc_region_switch.types.region
    import aws_sdk_arc_region_switch.types.region_list
    import aws_sdk_arc_region_switch.types.report_configuration
    import aws_sdk_arc_region_switch.types.trigger_list
    import aws_sdk_arc_region_switch.types.workflow_list


class Plan(TypedDict, closed=True):
    arn: "aws_sdk_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan.</p>"""
    description: NotRequired["str"]
    """<p>The description for a plan.</p>"""
    workflows: "aws_sdk_arc_region_switch.types.workflow_list.WorkflowList"
    """<p>The workflows for a plan.</p>"""
    execution_role: "aws_sdk_arc_region_switch.types.iam_role_arn.IamRoleArn"
    """<p>The execution role for a plan.</p>"""
    recovery_time_objective_minutes: NotRequired["int"]
    """<p>The recovery time objective for a plan.</p>"""
    associated_alarms: NotRequired[
        "aws_sdk_arc_region_switch.types.associated_alarm_map.AssociatedAlarmMap"
    ]
    """<p>The associated application health alarms for a plan.</p>"""
    triggers: NotRequired["aws_sdk_arc_region_switch.types.trigger_list.TriggerList"]
    """<p>The triggers for a plan.</p>"""
    report_configuration: NotRequired[
        "aws_sdk_arc_region_switch.types.report_configuration.ReportConfiguration"
    ]
    """<p>The report configuration for a plan.</p>"""
    name: "aws_sdk_arc_region_switch.types.plan_name.PlanName"
    """<p>The name for a plan.</p>"""
    regions: "aws_sdk_arc_region_switch.types.region_list.RegionList"
    """<p>The Amazon Web Services Regions for a plan.</p>"""
    recovery_approach: (
        "aws_sdk_arc_region_switch.types.recovery_approach.RecoveryApproach"
    )
    """<p>The recovery approach for a Region switch plan, which can be active/active (activeActive) or active/passive (activePassive).</p>"""
    primary_region: NotRequired["aws_sdk_arc_region_switch.types.region.Region"]
    """<p>The primary Region for a plan.</p>"""
    owner: "aws_sdk_arc_region_switch.types.account_id.AccountId"
    """<p>The owner of a plan.</p>"""
    version: NotRequired["str"]
    """<p>The version for the plan.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the plan was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Plan) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_arc_region_switch.types.workflow_list

    out["workflows"] = (
        aws_sdk_arc_region_switch.types.workflow_list.serialize_aws_json_1_0(
            value["workflows"]
        )
    )
    out["executionRole"] = value["execution_role"]
    if "recovery_time_objective_minutes" in value:
        out["recoveryTimeObjectiveMinutes"] = value["recovery_time_objective_minutes"]
    if "associated_alarms" in value:
        import aws_sdk_arc_region_switch.types.associated_alarm_map

        out["associatedAlarms"] = (
            aws_sdk_arc_region_switch.types.associated_alarm_map.serialize_aws_json_1_0(
                value["associated_alarms"]
            )
        )
    if "triggers" in value:
        import aws_sdk_arc_region_switch.types.trigger_list

        out["triggers"] = (
            aws_sdk_arc_region_switch.types.trigger_list.serialize_aws_json_1_0(
                value["triggers"]
            )
        )
    if "report_configuration" in value:
        import aws_sdk_arc_region_switch.types.report_configuration

        out["reportConfiguration"] = (
            aws_sdk_arc_region_switch.types.report_configuration.serialize_aws_json_1_0(
                value["report_configuration"]
            )
        )
    out["name"] = value["name"]
    import aws_sdk_arc_region_switch.types.region_list

    out["regions"] = aws_sdk_arc_region_switch.types.region_list.serialize_aws_json_1_0(
        value["regions"]
    )
    import aws_sdk_arc_region_switch.types.recovery_approach

    out["recoveryApproach"] = (
        aws_sdk_arc_region_switch.types.recovery_approach.serialize_aws_json_1_0(
            value["recovery_approach"]
        )
    )
    if "primary_region" in value:
        out["primaryRegion"] = value["primary_region"]
    out["owner"] = value["owner"]
    if "version" in value:
        out["version"] = value["version"]
    if "updated_at" in value:
        import aws_sdk_arc_region_switch.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Plan:
    out: Plan = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Plan.arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "workflows" in data:
        import aws_sdk_arc_region_switch.types.workflow_list

        out["workflows"] = (
            aws_sdk_arc_region_switch.types.workflow_list.deserialize_aws_json_1_0(
                data["workflows"]
            )
        )
    else:
        raise DeserializationError("Plan.workflows required")
    if "executionRole" in data:
        out["execution_role"] = data["executionRole"]
    else:
        raise DeserializationError("Plan.execution_role required")
    if "recoveryTimeObjectiveMinutes" in data:
        out["recovery_time_objective_minutes"] = data["recoveryTimeObjectiveMinutes"]
    if "associatedAlarms" in data:
        import aws_sdk_arc_region_switch.types.associated_alarm_map

        out["associated_alarms"] = (
            aws_sdk_arc_region_switch.types.associated_alarm_map.deserialize_aws_json_1_0(
                data["associatedAlarms"]
            )
        )
    if "triggers" in data:
        import aws_sdk_arc_region_switch.types.trigger_list

        out["triggers"] = (
            aws_sdk_arc_region_switch.types.trigger_list.deserialize_aws_json_1_0(
                data["triggers"]
            )
        )
    if "reportConfiguration" in data:
        import aws_sdk_arc_region_switch.types.report_configuration

        out["report_configuration"] = (
            aws_sdk_arc_region_switch.types.report_configuration.deserialize_aws_json_1_0(
                data["reportConfiguration"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Plan.name required")
    if "regions" in data:
        import aws_sdk_arc_region_switch.types.region_list

        out["regions"] = (
            aws_sdk_arc_region_switch.types.region_list.deserialize_aws_json_1_0(
                data["regions"]
            )
        )
    else:
        raise DeserializationError("Plan.regions required")
    if "recoveryApproach" in data:
        import aws_sdk_arc_region_switch.types.recovery_approach

        out["recovery_approach"] = (
            aws_sdk_arc_region_switch.types.recovery_approach.deserialize_aws_json_1_0(
                data["recoveryApproach"]
            )
        )
    else:
        raise DeserializationError("Plan.recovery_approach required")
    if "primaryRegion" in data:
        out["primary_region"] = data["primaryRegion"]
    if "owner" in data:
        out["owner"] = data["owner"]
    else:
        raise DeserializationError("Plan.owner required")
    if "version" in data:
        out["version"] = data["version"]
    if "updatedAt" in data:
        import aws_sdk_arc_region_switch.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    return out
