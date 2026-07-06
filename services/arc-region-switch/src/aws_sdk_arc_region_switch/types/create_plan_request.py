"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#CreatePlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.associated_alarm_map
    import aws_sdk_arc_region_switch.types.iam_role_arn
    import aws_sdk_arc_region_switch.types.plan_name
    import aws_sdk_arc_region_switch.types.recovery_approach
    import aws_sdk_arc_region_switch.types.region
    import aws_sdk_arc_region_switch.types.region_list
    import aws_sdk_arc_region_switch.types.report_configuration
    import aws_sdk_arc_region_switch.types.tags
    import aws_sdk_arc_region_switch.types.trigger_list
    import aws_sdk_arc_region_switch.types.workflow_list


class CreatePlanRequest(TypedDict, closed=True):
    description: NotRequired["str"]
    """<p>The description of a Region switch plan.</p>"""
    workflows: "aws_sdk_arc_region_switch.types.workflow_list.WorkflowList"
    """<p>An array of workflows included in a Region switch plan.</p>"""
    execution_role: "aws_sdk_arc_region_switch.types.iam_role_arn.IamRoleArn"
    """<p>An execution role is a way to categorize a Region switch plan.</p>"""
    recovery_time_objective_minutes: NotRequired["int"]
    """<p>Optionally, you can specify an recovery time objective for a Region switch plan, in minutes.</p>"""
    associated_alarms: NotRequired[
        "aws_sdk_arc_region_switch.types.associated_alarm_map.AssociatedAlarmMap"
    ]
    """<p>The alarms associated with a Region switch plan.</p>"""
    triggers: NotRequired["aws_sdk_arc_region_switch.types.trigger_list.TriggerList"]
    """<p>The triggers associated with a Region switch plan.</p>"""
    report_configuration: NotRequired[
        "aws_sdk_arc_region_switch.types.report_configuration.ReportConfiguration"
    ]
    name: "aws_sdk_arc_region_switch.types.plan_name.PlanName"
    """<p>The name of a Region switch plan.</p>"""
    regions: "aws_sdk_arc_region_switch.types.region_list.RegionList"
    """<p>An array that specifies the Amazon Web Services Regions for a Region switch plan. Specify two Regions.</p>"""
    recovery_approach: (
        "aws_sdk_arc_region_switch.types.recovery_approach.RecoveryApproach"
    )
    """<p>The recovery approach for a Region switch plan, which can be active/active (activeActive) or active/passive (activePassive).</p>"""
    primary_region: NotRequired["aws_sdk_arc_region_switch.types.region.Region"]
    """<p>The primary Amazon Web Services Region for the application. This is the Region where the application normally runs before any Region switch occurs.</p>"""
    tags: NotRequired["aws_sdk_arc_region_switch.types.tags.Tags"]
    """<p>The tags to apply to the Region switch plan.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreatePlanRequest) -> dict:
    out: dict = {}
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
    if "tags" in value:
        import aws_sdk_arc_region_switch.types.tags

        out["tags"] = aws_sdk_arc_region_switch.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreatePlanRequest:
    out: CreatePlanRequest = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("CreatePlanRequest.workflows required")
    if "executionRole" in data:
        out["execution_role"] = data["executionRole"]
    else:
        raise DeserializationError("CreatePlanRequest.execution_role required")
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
        raise DeserializationError("CreatePlanRequest.name required")
    if "regions" in data:
        import aws_sdk_arc_region_switch.types.region_list

        out["regions"] = (
            aws_sdk_arc_region_switch.types.region_list.deserialize_aws_json_1_0(
                data["regions"]
            )
        )
    else:
        raise DeserializationError("CreatePlanRequest.regions required")
    if "recoveryApproach" in data:
        import aws_sdk_arc_region_switch.types.recovery_approach

        out["recovery_approach"] = (
            aws_sdk_arc_region_switch.types.recovery_approach.deserialize_aws_json_1_0(
                data["recoveryApproach"]
            )
        )
    else:
        raise DeserializationError("CreatePlanRequest.recovery_approach required")
    if "primaryRegion" in data:
        out["primary_region"] = data["primaryRegion"]
    if "tags" in data:
        import aws_sdk_arc_region_switch.types.tags

        out["tags"] = aws_sdk_arc_region_switch.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
