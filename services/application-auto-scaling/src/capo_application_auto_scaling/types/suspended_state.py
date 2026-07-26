"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#SuspendedState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.scaling_suspended


class SuspendedState(TypedDict, closed=True):
    dynamic_scaling_in_suspended: NotRequired[
        "capo_application_auto_scaling.types.scaling_suspended.ScalingSuspended"
    ]
    """<p>Whether scale in by a target tracking scaling policy or a step scaling policy is suspended. Set the value to <code>true</code> if you don't want Application Auto Scaling to remove capacity when a scaling policy is triggered. The default is <code>false</code>. </p>"""
    dynamic_scaling_out_suspended: NotRequired[
        "capo_application_auto_scaling.types.scaling_suspended.ScalingSuspended"
    ]
    """<p>Whether scale out by a target tracking scaling policy or a step scaling policy is suspended. Set the value to <code>true</code> if you don't want Application Auto Scaling to add capacity when a scaling policy is triggered. The default is <code>false</code>. </p>"""
    scheduled_scaling_suspended: NotRequired[
        "capo_application_auto_scaling.types.scaling_suspended.ScalingSuspended"
    ]
    """<p>Whether scheduled scaling is suspended. Set the value to <code>true</code> if you don't want Application Auto Scaling to add or remove capacity by initiating scheduled actions. The default is <code>false</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuspendedState) -> dict:
    out: dict = {}
    if "dynamic_scaling_in_suspended" in value:
        out["DynamicScalingInSuspended"] = value["dynamic_scaling_in_suspended"]
    if "dynamic_scaling_out_suspended" in value:
        out["DynamicScalingOutSuspended"] = value["dynamic_scaling_out_suspended"]
    if "scheduled_scaling_suspended" in value:
        out["ScheduledScalingSuspended"] = value["scheduled_scaling_suspended"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SuspendedState:
    out: SuspendedState = {}  # type: ignore[typeddict-item]
    if "DynamicScalingInSuspended" in data:
        out["dynamic_scaling_in_suspended"] = data["DynamicScalingInSuspended"]
    if "DynamicScalingOutSuspended" in data:
        out["dynamic_scaling_out_suspended"] = data["DynamicScalingOutSuspended"]
    if "ScheduledScalingSuspended" in data:
        out["scheduled_scaling_suspended"] = data["ScheduledScalingSuspended"]
    return out
