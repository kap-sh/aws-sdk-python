"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#GetPlanExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_arc_region_switch.types.duration
    import aws_sdk_arc_region_switch.types.execution_action
    import aws_sdk_arc_region_switch.types.execution_id
    import aws_sdk_arc_region_switch.types.execution_mode
    import aws_sdk_arc_region_switch.types.execution_state
    import aws_sdk_arc_region_switch.types.generated_report_details
    import aws_sdk_arc_region_switch.types.plan
    import aws_sdk_arc_region_switch.types.plan_arn
    import aws_sdk_arc_region_switch.types.step_states


class GetPlanExecutionResponse(TypedDict, closed=True):
    plan_arn: "aws_sdk_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan.</p>"""
    execution_id: "aws_sdk_arc_region_switch.types.execution_id.ExecutionId"
    """<p>The execution identifier of a plan execution.</p>"""
    version: NotRequired["str"]
    """<p>The version for the plan.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the plan execution was last updated.</p>"""
    comment: NotRequired["str"]
    """<p>A comment included on the plan execution.</p>"""
    start_time: "datetime.datetime"
    """<p>The time (UTC) when the plan execution started.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The time (UTC) when the plan execution ended.</p>"""
    mode: "aws_sdk_arc_region_switch.types.execution_mode.ExecutionMode"
    """<p>The plan execution mode. Valid values are <code>graceful</code>, for graceful executions, or <code>ungraceful</code>, for ungraceful executions.</p>"""
    execution_state: "aws_sdk_arc_region_switch.types.execution_state.ExecutionState"
    """<p>The plan execution state. Provides the state of a plan execution, for example, In Progress or Paused by Operator.</p>"""
    execution_action: "aws_sdk_arc_region_switch.types.execution_action.ExecutionAction"
    """<p>The plan execution action. Valid values are <code>activate</code>, to activate an Amazon Web Services Region, or <code>deactivate</code>, to deactivate a Region.</p>"""
    execution_region: "str"
    """<p>The Amazon Web Services Region for a plan execution.</p>"""
    recovery_execution_id: NotRequired["str"]
    """<p>The unique identifier of the most recent recovery execution. Required when starting a post-recovery execution.</p>"""
    step_states: NotRequired["aws_sdk_arc_region_switch.types.step_states.StepStates"]
    """<p>The states of the steps in the plan execution.</p>"""
    plan: NotRequired["aws_sdk_arc_region_switch.types.plan.Plan"]
    """<p>The details of the Region switch plan.</p>"""
    actual_recovery_time: NotRequired[
        "aws_sdk_arc_region_switch.types.duration.Duration"
    ]
    """<p>The actual recovery time that Region switch calculates for a plan execution. Actual recovery time includes the time for the plan to run added to the time elapsed until the application health alarms that you've specified are healthy again.</p>"""
    generated_report_details: NotRequired[
        "aws_sdk_arc_region_switch.types.generated_report_details.GeneratedReportDetails"
    ]
    """<p>Information about the location of a generated report, or the cause of its failure.</p>"""
    next_token: NotRequired["str"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPlanExecutionResponse) -> dict:
    out: dict = {}
    out["planArn"] = value["plan_arn"]
    out["executionId"] = value["execution_id"]
    if "version" in value:
        out["version"] = value["version"]
    if "updated_at" in value:
        import aws_sdk_arc_region_switch.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    if "comment" in value:
        out["comment"] = value["comment"]
    import aws_sdk_arc_region_switch.types._prelude.timestamp

    out["startTime"] = (
        aws_sdk_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
            value["start_time"]
        )
    )
    if "end_time" in value:
        import aws_sdk_arc_region_switch.types._prelude.timestamp

        out["endTime"] = (
            aws_sdk_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
                value["end_time"]
            )
        )
    import aws_sdk_arc_region_switch.types.execution_mode

    out["mode"] = aws_sdk_arc_region_switch.types.execution_mode.serialize_aws_json_1_0(
        value["mode"]
    )
    import aws_sdk_arc_region_switch.types.execution_state

    out["executionState"] = (
        aws_sdk_arc_region_switch.types.execution_state.serialize_aws_json_1_0(
            value["execution_state"]
        )
    )
    import aws_sdk_arc_region_switch.types.execution_action

    out["executionAction"] = (
        aws_sdk_arc_region_switch.types.execution_action.serialize_aws_json_1_0(
            value["execution_action"]
        )
    )
    out["executionRegion"] = value["execution_region"]
    if "recovery_execution_id" in value:
        out["recoveryExecutionId"] = value["recovery_execution_id"]
    if "step_states" in value:
        import aws_sdk_arc_region_switch.types.step_states

        out["stepStates"] = (
            aws_sdk_arc_region_switch.types.step_states.serialize_aws_json_1_0(
                value["step_states"]
            )
        )
    if "plan" in value:
        import aws_sdk_arc_region_switch.types.plan

        out["plan"] = aws_sdk_arc_region_switch.types.plan.serialize_aws_json_1_0(
            value["plan"]
        )
    if "actual_recovery_time" in value:
        out["actualRecoveryTime"] = value["actual_recovery_time"]
    if "generated_report_details" in value:
        import aws_sdk_arc_region_switch.types.generated_report_details

        out["generatedReportDetails"] = (
            aws_sdk_arc_region_switch.types.generated_report_details.serialize_aws_json_1_0(
                value["generated_report_details"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPlanExecutionResponse:
    out: GetPlanExecutionResponse = {}  # type: ignore[typeddict-item]
    if "planArn" in data:
        out["plan_arn"] = data["planArn"]
    else:
        raise DeserializationError("GetPlanExecutionResponse.plan_arn required")
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError("GetPlanExecutionResponse.execution_id required")
    if "version" in data:
        out["version"] = data["version"]
    if "updatedAt" in data:
        import aws_sdk_arc_region_switch.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    if "comment" in data:
        out["comment"] = data["comment"]
    if "startTime" in data:
        import aws_sdk_arc_region_switch.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("GetPlanExecutionResponse.start_time required")
    if "endTime" in data:
        import aws_sdk_arc_region_switch.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["endTime"]
            )
        )
    if "mode" in data:
        import aws_sdk_arc_region_switch.types.execution_mode

        out["mode"] = (
            aws_sdk_arc_region_switch.types.execution_mode.deserialize_aws_json_1_0(
                data["mode"]
            )
        )
    else:
        raise DeserializationError("GetPlanExecutionResponse.mode required")
    if "executionState" in data:
        import aws_sdk_arc_region_switch.types.execution_state

        out["execution_state"] = (
            aws_sdk_arc_region_switch.types.execution_state.deserialize_aws_json_1_0(
                data["executionState"]
            )
        )
    else:
        raise DeserializationError("GetPlanExecutionResponse.execution_state required")
    if "executionAction" in data:
        import aws_sdk_arc_region_switch.types.execution_action

        out["execution_action"] = (
            aws_sdk_arc_region_switch.types.execution_action.deserialize_aws_json_1_0(
                data["executionAction"]
            )
        )
    else:
        raise DeserializationError("GetPlanExecutionResponse.execution_action required")
    if "executionRegion" in data:
        out["execution_region"] = data["executionRegion"]
    else:
        raise DeserializationError("GetPlanExecutionResponse.execution_region required")
    if "recoveryExecutionId" in data:
        out["recovery_execution_id"] = data["recoveryExecutionId"]
    if "stepStates" in data:
        import aws_sdk_arc_region_switch.types.step_states

        out["step_states"] = (
            aws_sdk_arc_region_switch.types.step_states.deserialize_aws_json_1_0(
                data["stepStates"]
            )
        )
    if "plan" in data:
        import aws_sdk_arc_region_switch.types.plan

        out["plan"] = aws_sdk_arc_region_switch.types.plan.deserialize_aws_json_1_0(
            data["plan"]
        )
    if "actualRecoveryTime" in data:
        out["actual_recovery_time"] = data["actualRecoveryTime"]
    if "generatedReportDetails" in data:
        import aws_sdk_arc_region_switch.types.generated_report_details

        out["generated_report_details"] = (
            aws_sdk_arc_region_switch.types.generated_report_details.deserialize_aws_json_1_0(
                data["generatedReportDetails"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
