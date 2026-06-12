"""Generated from Smithy shape ``com.amazonaws.deadline#PriorityBalancedSchedulingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.scheduling_rendering_task_buffer


class PriorityBalancedSchedulingConfiguration(TypedDict):
    rendering_task_buffer: "aws_sdk_deadline.types.scheduling_rendering_task_buffer.SchedulingRenderingTaskBuffer"
    """<p>The rendering task buffer controls worker stickiness. A worker only switches from its current job to another job at the same priority if the other job has fewer rendering tasks by more than this buffer value. Higher values make workers stickier to their current jobs. The default value is <code>1</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PriorityBalancedSchedulingConfiguration) -> dict:
    out: dict = {}
    out["renderingTaskBuffer"] = value.get("rendering_task_buffer", 1)
    return out


def deserialize_json(data: dict) -> PriorityBalancedSchedulingConfiguration:
    out: PriorityBalancedSchedulingConfiguration = {}  # type: ignore[typeddict-item]
    if "renderingTaskBuffer" in data:
        out["rendering_task_buffer"] = data["renderingTaskBuffer"]
    else:
        out["rendering_task_buffer"] = 1
    return out
