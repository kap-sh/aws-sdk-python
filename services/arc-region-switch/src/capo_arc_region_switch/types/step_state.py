"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#StepState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_arc_region_switch.types.execution_mode
    import capo_arc_region_switch.types.step_name
    import capo_arc_region_switch.types.step_status


class StepState(TypedDict, closed=True):
    name: NotRequired["capo_arc_region_switch.types.step_name.StepName"]
    """<p>The name of a step in a workflow.</p>"""
    status: NotRequired["capo_arc_region_switch.types.step_status.StepStatus"]
    """<p>The status of a step in a workflow. For example, a status might be Completed or Pending Approval.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The timestamp when a step started execution.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The timestamp when a step endeded execution.</p>"""
    step_mode: NotRequired["capo_arc_region_switch.types.execution_mode.ExecutionMode"]
    """<p>The mode for a step execution. The mode can be Graceful or Ungraceful.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StepState) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        import capo_arc_region_switch.types.step_status

        out["status"] = capo_arc_region_switch.types.step_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "start_time" in value:
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
    if "step_mode" in value:
        import capo_arc_region_switch.types.execution_mode

        out["stepMode"] = (
            capo_arc_region_switch.types.execution_mode.serialize_aws_json_1_0(
                value["step_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StepState:
    out: StepState = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        import capo_arc_region_switch.types.step_status

        out["status"] = (
            capo_arc_region_switch.types.step_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "startTime" in data:
        import capo_arc_region_switch.types._prelude.timestamp

        out["start_time"] = (
            capo_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startTime"]
            )
        )
    if "endTime" in data:
        import capo_arc_region_switch.types._prelude.timestamp

        out["end_time"] = (
            capo_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["endTime"]
            )
        )
    if "stepMode" in data:
        import capo_arc_region_switch.types.execution_mode

        out["step_mode"] = (
            capo_arc_region_switch.types.execution_mode.deserialize_aws_json_1_0(
                data["stepMode"]
            )
        )
    return out
