"""Generated from Smithy shape ``com.amazonaws.batch#ComputeScalingPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.integer


class ComputeScalingPolicy(TypedDict, closed=True):
    min_scale_down_delay_minutes: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The minimum time (in minutes) that Batch keeps instances running in the compute environment after their jobs complete. For each instance, the delay period begins when the last job finishes. If no new jobs are placed on the instance during this delay, Batch terminates the instance once the delay expires.</p> <p>Valid Range: Minimum value of 20. Maximum value of 10080. Use 0 to unset and disable the scale down delay.</p> <note> <p>Idle instances retained during the scale-down delay period are billable at standard EC2 pricing.</p> </note> <note> <p>The scale down delay does not apply to:</p> <ul> <li> <p>Instances being replaced during infrastructure updates</p> </li> <li> <p>Newly launched instances that have not yet run any jobs</p> </li> <li> <p>Spot instances reclaimed due to interruption</p> </li> </ul> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputeScalingPolicy) -> dict:
    out: dict = {}
    if "min_scale_down_delay_minutes" in value:
        out["minScaleDownDelayMinutes"] = value["min_scale_down_delay_minutes"]
    return out


def deserialize_json(data: dict) -> ComputeScalingPolicy:
    out: ComputeScalingPolicy = {}  # type: ignore[typeddict-item]
    if "minScaleDownDelayMinutes" in data:
        out["min_scale_down_delay_minutes"] = data["minScaleDownDelayMinutes"]
    return out
