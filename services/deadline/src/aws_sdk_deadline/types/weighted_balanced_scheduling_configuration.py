"""Generated from Smithy shape ``com.amazonaws.deadline#WeightedBalancedSchedulingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.scheduling_error_weight
    import aws_sdk_deadline.types.scheduling_max_priority_override
    import aws_sdk_deadline.types.scheduling_min_priority_override
    import aws_sdk_deadline.types.scheduling_priority_weight
    import aws_sdk_deadline.types.scheduling_rendering_task_buffer
    import aws_sdk_deadline.types.scheduling_rendering_task_weight
    import aws_sdk_deadline.types.scheduling_submission_time_weight


class WeightedBalancedSchedulingConfiguration(TypedDict):
    priority_weight: (
        "aws_sdk_deadline.types.scheduling_priority_weight.SchedulingPriorityWeight"
    )
    """<p>The weight applied to job priority in the scheduling formula. Higher values give more influence to job priority. A value of <code>0</code> means priority is ignored. The default value is <code>100.0</code>.</p>"""
    error_weight: "aws_sdk_deadline.types.scheduling_error_weight.SchedulingErrorWeight"
    """<p>The weight applied to the number of errors on a job. A negative value means jobs without errors are scheduled first. A value of <code>0</code> means errors are ignored. The default value is <code>-10.0</code>.</p>"""
    submission_time_weight: "aws_sdk_deadline.types.scheduling_submission_time_weight.SchedulingSubmissionTimeWeight"
    """<p>The weight applied to job submission time. A positive value means earlier jobs are scheduled first. A value of <code>0</code> means submission time is ignored. The default value is <code>3.0</code>.</p>"""
    rendering_task_weight: "aws_sdk_deadline.types.scheduling_rendering_task_weight.SchedulingRenderingTaskWeight"
    """<p>The weight applied to the number of tasks currently rendering on a job. A negative value means jobs that are not already rendering are scheduled next. A value of <code>0</code> means the rendering state is ignored. The default value is <code>-100.0</code>.</p>"""
    rendering_task_buffer: "aws_sdk_deadline.types.scheduling_rendering_task_buffer.SchedulingRenderingTaskBuffer"
    """<p>The rendering task buffer is subtracted from the number of rendering tasks before applying the rendering task weight. This creates a stickiness effect where workers prefer to stay with their current job. Higher values make workers stickier. The default value is <code>1</code>. The buffer is only applied in the weight calculation for a job if the worker is currently assigned to that job.</p>"""
    max_priority_override: NotRequired[
        "aws_sdk_deadline.types.scheduling_max_priority_override.SchedulingMaxPriorityOverride"
    ]
    """<p>Overrides the weighted scheduling formula for jobs at the maximum priority (100). When set, jobs with priority 100 are always scheduled first regardless of their calculated weight. When absent, maximum priority jobs use the standard weighted formula.</p>"""
    min_priority_override: NotRequired[
        "aws_sdk_deadline.types.scheduling_min_priority_override.SchedulingMinPriorityOverride"
    ]
    """<p>Overrides the weighted scheduling formula for jobs at the minimum priority (0). When set, jobs with priority 0 are always scheduled last regardless of their calculated weight. When absent, minimum priority jobs use the standard weighted formula.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WeightedBalancedSchedulingConfiguration) -> dict:
    out: dict = {}
    out["priorityWeight"] = value.get("priority_weight", 100.0)
    out["errorWeight"] = value.get("error_weight", -10.0)
    out["submissionTimeWeight"] = value.get("submission_time_weight", 3.0)
    out["renderingTaskWeight"] = value.get("rendering_task_weight", -100.0)
    out["renderingTaskBuffer"] = value.get("rendering_task_buffer", 1)
    if "max_priority_override" in value:
        import aws_sdk_deadline.types.scheduling_max_priority_override

        out["maxPriorityOverride"] = (
            aws_sdk_deadline.types.scheduling_max_priority_override.serialize_json(
                value["max_priority_override"]
            )
        )
    if "min_priority_override" in value:
        import aws_sdk_deadline.types.scheduling_min_priority_override

        out["minPriorityOverride"] = (
            aws_sdk_deadline.types.scheduling_min_priority_override.serialize_json(
                value["min_priority_override"]
            )
        )
    return out


def deserialize_json(data: dict) -> WeightedBalancedSchedulingConfiguration:
    out: WeightedBalancedSchedulingConfiguration = {}  # type: ignore[typeddict-item]
    if "priorityWeight" in data:
        out["priority_weight"] = data["priorityWeight"]
    else:
        out["priority_weight"] = 100.0
    if "errorWeight" in data:
        out["error_weight"] = data["errorWeight"]
    else:
        out["error_weight"] = -10.0
    if "submissionTimeWeight" in data:
        out["submission_time_weight"] = data["submissionTimeWeight"]
    else:
        out["submission_time_weight"] = 3.0
    if "renderingTaskWeight" in data:
        out["rendering_task_weight"] = data["renderingTaskWeight"]
    else:
        out["rendering_task_weight"] = -100.0
    if "renderingTaskBuffer" in data:
        out["rendering_task_buffer"] = data["renderingTaskBuffer"]
    else:
        out["rendering_task_buffer"] = 1
    if "maxPriorityOverride" in data:
        import aws_sdk_deadline.types.scheduling_max_priority_override

        out["max_priority_override"] = (
            aws_sdk_deadline.types.scheduling_max_priority_override.deserialize_json(
                data["maxPriorityOverride"]
            )
        )
    if "minPriorityOverride" in data:
        import aws_sdk_deadline.types.scheduling_min_priority_override

        out["min_priority_override"] = (
            aws_sdk_deadline.types.scheduling_min_priority_override.deserialize_json(
                data["minPriorityOverride"]
            )
        )
    return out
