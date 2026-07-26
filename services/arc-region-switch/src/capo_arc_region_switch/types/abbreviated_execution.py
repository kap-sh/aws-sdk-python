"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#AbbreviatedExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_arc_region_switch.types.duration
    import capo_arc_region_switch.types.execution_action
    import capo_arc_region_switch.types.execution_id
    import capo_arc_region_switch.types.execution_mode
    import capo_arc_region_switch.types.execution_state
    import capo_arc_region_switch.types.plan_arn


class AbbreviatedExecution(TypedDict, closed=True):
    plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan.</p>"""
    execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId"
    """<p>The execution identifier of a plan execution.</p>"""
    version: NotRequired["str"]
    """<p>The version for the plan.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the plan execution was last updated.</p>"""
    comment: NotRequired["str"]
    """<p>An optional comment about the plan execution.</p>"""
    start_time: "datetime.datetime"
    """<p>The timestamp when the plan execution was started.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The timestamp when the plan execution was ended.</p>"""
    mode: "capo_arc_region_switch.types.execution_mode.ExecutionMode"
    """<p>The plan execution mode. Valid values are <code>graceful</code>, for graceful executions, or <code>ungraceful</code>, for ungraceful executions.</p>"""
    execution_state: "capo_arc_region_switch.types.execution_state.ExecutionState"
    """<p>The plan execution state. Provides the state of a plan execution, for example, In Progress or Paused by Operator.</p>"""
    execution_action: "capo_arc_region_switch.types.execution_action.ExecutionAction"
    """<p>The plan execution action. Valid values are <code>activate</code>, to activate an Amazon Web Services Region, or <code>deactivate</code>, to deactivate a Region.</p>"""
    execution_region: "str"
    """<p>The Amazon Web Services Region for a plan execution.</p>"""
    recovery_execution_id: NotRequired["str"]
    """<p>The unique identifier of the most recent recovery execution. Required when starting a post-recovery execution.</p>"""
    actual_recovery_time: NotRequired["capo_arc_region_switch.types.duration.Duration"]
    """<p>The actual recovery time that Region switch calculates for a plan execution. Actual recovery time includes the time for the plan to run added to the time elapsed until the application health alarms that you've specified are healthy again.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AbbreviatedExecution) -> dict:
    out: dict = {}
    out["planArn"] = value["plan_arn"]
    out["executionId"] = value["execution_id"]
    if "version" in value:
        out["version"] = value["version"]
    if "updated_at" in value:
        import capo_arc_region_switch.types._prelude.timestamp

        out["updatedAt"] = (
            capo_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    if "comment" in value:
        out["comment"] = value["comment"]
    import capo_arc_region_switch.types._prelude.timestamp

    out["startTime"] = (
        capo_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
            value["start_time"]
        )
    )
    if "end_time" in value:
        import capo_arc_region_switch.types._prelude.timestamp

        out["endTime"] = (
            capo_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
                value["end_time"]
            )
        )
    import capo_arc_region_switch.types.execution_mode

    out["mode"] = capo_arc_region_switch.types.execution_mode.serialize_aws_json_1_0(
        value["mode"]
    )
    import capo_arc_region_switch.types.execution_state

    out["executionState"] = (
        capo_arc_region_switch.types.execution_state.serialize_aws_json_1_0(
            value["execution_state"]
        )
    )
    import capo_arc_region_switch.types.execution_action

    out["executionAction"] = (
        capo_arc_region_switch.types.execution_action.serialize_aws_json_1_0(
            value["execution_action"]
        )
    )
    out["executionRegion"] = value["execution_region"]
    if "recovery_execution_id" in value:
        out["recoveryExecutionId"] = value["recovery_execution_id"]
    if "actual_recovery_time" in value:
        out["actualRecoveryTime"] = value["actual_recovery_time"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AbbreviatedExecution:
    out: AbbreviatedExecution = {}  # type: ignore[typeddict-item]
    if "planArn" in data:
        out["plan_arn"] = data["planArn"]
    else:
        raise DeserializationError("AbbreviatedExecution.plan_arn required")
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError("AbbreviatedExecution.execution_id required")
    if "version" in data:
        out["version"] = data["version"]
    if "updatedAt" in data:
        import capo_arc_region_switch.types._prelude.timestamp

        out["updated_at"] = (
            capo_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    if "comment" in data:
        out["comment"] = data["comment"]
    if "startTime" in data:
        import capo_arc_region_switch.types._prelude.timestamp

        out["start_time"] = (
            capo_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("AbbreviatedExecution.start_time required")
    if "endTime" in data:
        import capo_arc_region_switch.types._prelude.timestamp

        out["end_time"] = (
            capo_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["endTime"]
            )
        )
    if "mode" in data:
        import capo_arc_region_switch.types.execution_mode

        out["mode"] = (
            capo_arc_region_switch.types.execution_mode.deserialize_aws_json_1_0(
                data["mode"]
            )
        )
    else:
        raise DeserializationError("AbbreviatedExecution.mode required")
    if "executionState" in data:
        import capo_arc_region_switch.types.execution_state

        out["execution_state"] = (
            capo_arc_region_switch.types.execution_state.deserialize_aws_json_1_0(
                data["executionState"]
            )
        )
    else:
        raise DeserializationError("AbbreviatedExecution.execution_state required")
    if "executionAction" in data:
        import capo_arc_region_switch.types.execution_action

        out["execution_action"] = (
            capo_arc_region_switch.types.execution_action.deserialize_aws_json_1_0(
                data["executionAction"]
            )
        )
    else:
        raise DeserializationError("AbbreviatedExecution.execution_action required")
    if "executionRegion" in data:
        out["execution_region"] = data["executionRegion"]
    else:
        raise DeserializationError("AbbreviatedExecution.execution_region required")
    if "recoveryExecutionId" in data:
        out["recovery_execution_id"] = data["recoveryExecutionId"]
    if "actualRecoveryTime" in data:
        out["actual_recovery_time"] = data["actualRecoveryTime"]
    return out
